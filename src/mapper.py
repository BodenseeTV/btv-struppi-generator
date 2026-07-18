import math
from datetime import datetime, timedelta
from io import BytesIO
from zoneinfo import ZoneInfo

import pandas as pd
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from generated import SendungComplexType, TerminComplexType, TermintypSimpleType, TitelComplexType, InfosComplexType, \
    KlassifizierungComplexType, FormatgruppeSimpleType, AblauftypSimpleType, AblaufComplexType, LinkComplexType, \
    SenderComplexType, Programmdaten, AliasComplexType, TitelartSimpleType, MitwirkungComplexType, \
    MitwirkenderComplexType, MitwirkendertypComplexType, MitwirkendeFunktionSimpleType, \
    GruppeComplexType, WiederholungComplexType

TZ = ZoneInfo("Europe/Zurich")

def map_excel_to_xml(excel: BytesIO, start_date: datetime, end_date: datetime):
    df = pd.read_excel(excel,
                       header=1,
                       sheet_name=str(start_date.year),
                       converters={
                           "Kategorie": str,
                       })

    if start_date.year != end_date.year:
        new_year_df = pd.read_excel(excel,
                                    header=1,
                                    sheet_name=str(end_date.year),
                                    converters={
                                        "Kategorie": str,
                                    })
        df = pd.concat([df, new_year_df])

    df = df.rename(columns={"Datum\n": "Datum"})
    df["Datum"] = pd.to_datetime(df["Datum"])
    df["Datum"] = df["Datum"].dt.tz_localize(TZ).dt.floor(freq="ms") + timedelta(hours=4, minutes=30)
    df["Datum"] = df["Datum"].ffill()
    df = df[df["Datum"] >= start_date]
    df = df[df["Datum"] <= end_date]

    df["Länge"] = pd.to_timedelta(df["Länge"].str.replace(r"(\d+):(\d+):(\d+):(\d+)", r"\1:\2:\3.\4", regex=True))

    df = df[df["Kategorie"].notna() & (df["Kategorie"].str.strip() != "")]
    df = df[df["Kategorie"].str.startswith("10")]

    struppi_sendungen: list[SendungComplexType] = []

    grouped_by = list(df.groupby("Datum"))
    enumerated = enumerate(grouped_by)

    for day_idx, (day_date, day_df) in enumerated:
        day_df["sendung_cumcount"] = (day_df["Kategorie"] == "10 - Sendung").shift(fill_value=False).cumsum()

        repeats_start: datetime = day_date

        if day_idx + 1 >= len(grouped_by):
            continue
        next_day = grouped_by[day_idx + 1]
        next_day_date = next_day[0]
        repeats_duration = next_day_date - day_date
        repeats_end = repeats_start + repeats_duration
        if end_date <= repeats_end:
            repeats_end = end_date

        print(f"{repeats_start} - {repeats_end} [{repeats_duration}]")

        additionals_df = day_df[day_df["Kategorie"] != "10 - Sendung"]
        additionals_duration = additionals_df["Länge"].sum(skipna=True)

        day_sendungen: dict[str, timedelta] = {}

        sendungen_df = day_df[day_df["Kategorie"] == "10 - Sendung"]
        for _, sendung_s in sendungen_df.iterrows():
            sendung_titel = sendung_s["Thema"]

            sendung_duration = timedelta(hours=1)
            if pd.notna(sendung_s["Länge"]):
                sendung_duration = sendung_s["Länge"] + additionals_duration

            print(f"- {sendung_titel} [{sendung_duration}]")
            day_sendungen[sendung_titel] = sendung_duration

        repeation_duration = sum(day_sendungen.values(), timedelta(0))
        repeats_count = math.ceil(repeats_duration / repeation_duration)

        print(f"{repeats_count}x {repeation_duration}")

        sendung_start = repeats_start
        for i in range(0, repeats_count):
            for sendung_titel, sendung_duration in day_sendungen.items():
                if sendung_start >= repeats_end:
                    continue

                sendung_end = sendung_start + sendung_duration
                if sendung_end > repeats_end:
                    sendung_end = repeats_end

                sendung_id = len(struppi_sendungen) + 1
                struppi_sendungen.append(SendungComplexType(
                    sendung_id=str(sendung_id),
                    termin=TerminComplexType(
                        termin_id=str(sendung_id),
                        reihenfolge=sendung_id,
                        termintyp=TermintypSimpleType.NEU,
                        start=XmlDateTime.from_datetime(sendung_start),
                        ende=XmlDateTime.from_datetime(sendung_end)
                    ),
                    titel=TitelComplexType(
                        termintitel=sendung_titel,
                        alias=[
                            AliasComplexType(
                                titelart=TitelartSimpleType.TITEL,
                                aliastitel=sendung_titel,
                            )
                        ]
                    ),
                    infos=InfosComplexType(
                        klassifizierung=KlassifizierungComplexType(
                            formatgruppe=FormatgruppeSimpleType.SONSTIGES
                        )
                    ),
                    mitwirkende=MitwirkungComplexType(
                        mitwirkender=[
                            MitwirkenderComplexType(
                                funktion=MitwirkendeFunktionSimpleType.PRODUKTIONSFIRMA,
                                reihenfolge=1,
                                mitwirkendentyp=MitwirkendertypComplexType(
                                    gruppe=GruppeComplexType(
                                        name="Lokalfernsehen Steckborn",
                                        aliasname=["LFS"],
                                    )
                                )
                            )
                        ]
                    )
                ))

                sendung_start = sendung_end
        print()

    programm_daten = Programmdaten(
        generierungsdatum=XmlDateTime.from_datetime(datetime.now(TZ)),
        sender=[
            SenderComplexType(
                sendername="BodenseeTV",
                vps=False,
                kontaktdaten="redaktion.steckborn@bodenseetv.ch",
                senderlogo=[
                    LinkComplexType(
                        link="https://struppi.bodenseetv.ch/images/logo.jpg"
                    )
                ],
                ablauf=[
                    AblaufComplexType(
                        ablauftyp=AblauftypSimpleType.ABLAUF,
                        ablaufstart=XmlDateTime.from_datetime(start_date),
                        ablaufende=XmlDateTime.from_datetime(end_date),
                        sendung=struppi_sendungen
                    )
                ]
            )
        ]
    )

    config = SerializerConfig(
        pretty_print=True,
        xml_declaration=False
    )
    serializer = XmlSerializer(config=config)
    return serializer.render(programm_daten, {
        None: "http://struppi.tv/xsd/",
        "xsd": "http://www.w3.org/2001/XMLSchema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance"
    })
