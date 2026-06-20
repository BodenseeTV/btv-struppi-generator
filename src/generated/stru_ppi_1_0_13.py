from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

__NAMESPACE__ = "http://struppi.tv/xsd/"


class AblauftypSimpleType(Enum):
    ABLAUF = "ablauf"
    TVONDEMAND = "tvondemand"
    VIDEOONDEMAND = "videoondemand"


@dataclass(kw_only=True)
class AlternativComplexType:
    class Meta:
        name = "alternativComplexType"

    alternativ_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    alternativ: bool = field(
        metadata={
            "type": "Attribute",
        }
    )


class AltersfreigabeSimpleType(Enum):
    OHNE_ALTERSBESCHR_NKUNG = "Ohne Altersbeschränkung"
    AB_0 = "ab 0"
    AB_6 = "ab 6"
    AB_12 = "ab 12"
    AB_16 = "ab 16"
    AB_18 = "ab 18"
    KEINE_JUGENDFREIGABE = "Keine Jugendfreigabe"
    BEANTRAGT_OHNE_ALTERSBESCHR_NKUNG = "Beantragt: Ohne Altersbeschränkung"
    BEANTRAGT_AB_0 = "Beantragt: ab 0"
    BEANTRAGT_AB_6 = "Beantragt: ab 6"
    BEANTRAGT_AB_12 = "Beantragt: ab 12"
    BEANTRAGT_AB_16 = "Beantragt: ab 16"
    BEANTRAGT_AB_18 = "Beantragt: ab 18"
    UNBEKANNT = "Unbekannt"
    NICHT_VERGEBEN = "Nicht vergeben"


@dataclass(kw_only=True)
class AuszeichnungComplexType:
    class Meta:
        name = "auszeichnungComplexType"

    jahr: None | XmlPeriod = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    veranstalter: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bezeichnung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kategorie: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nominierung: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hinweis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BewertungComplexType:
    class Meta:
        name = "bewertungComplexType"

    kategorie: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    hoehe: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1}",
        }
    )
    quelle: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    highlight: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class BildmaterialtypSimpleType(Enum):
    LOGO = "Logo"
    TITELSCHRIFTZUG = "Titelschriftzug"
    SZENENBILD = "Szenenbild"
    GRUPPENBILD = "Gruppenbild"
    STANDFOTO = "Standfoto"
    PLAKATMOTIV = "Plakatmotiv"
    ARTWORK = "Artwork"
    AUSHANGFOTO = "Aushangfoto"
    MAKING_OF = "Making of"
    DOPPELPORTRAIT = "Doppelportrait"
    PORTRAIT = "Portrait"
    ANIMATIONSPORTRAIT = "Animationsportrait"
    MAZ_BILD = "MAZ-Bild"
    DVD_COVER = "DVD Cover"
    SONSTIGES = "Sonstiges"


class DateiformatBewegtbildSimpleType(Enum):
    OGG = "ogg"
    AVI = "avi"
    MPG = "mpg"
    XVID = "xvid"
    FLV = "flv"
    RM = "rm"
    WMV = "wmv"
    XAP = "xap"
    MOV = "mov"


class DateiformatBildSimpleType(Enum):
    JPG = "jpg"
    PNG = "png"
    GIF = "gif"
    TIFF = "tiff"
    EPS = "eps"


class DateiformatTextSimpleType(Enum):
    ODS = "ods"
    XML = "xml"
    TXT = "txt"
    RTF = "rtf"
    PDF = "pdf"
    DOC = "doc"


class DateiformatTonSimpleType(Enum):
    OGG = "ogg"
    MP3 = "mp3"
    WAV = "wav"
    ACC = "acc"
    FLAC = "flac"


@dataclass(kw_only=True)
class DvbsigenreComplexType:
    class Meta:
        name = "dvbsigenreComplexType"

    dvbsi_content_nibble_level1: None | str = field(
        default=None,
        metadata={
            "name": "dvbsi_Content_nibble_level1",
            "type": "Attribute",
        },
    )
    dvbsi_content_nibble_level2: None | str = field(
        default=None,
        metadata={
            "name": "dvbsi_Content_nibble_level2",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EpisodeComplexType:
    class Meta:
        name = "episodeComplexType"

    episodentitel: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    sprache_episodentitel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    episodenreihenfolge: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    episodenoriginaltitel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache_episodenoriginaltitel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    episodentext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache_episodentext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ErweiterungenComplexType:
    """
    Geplant für VideoOnDemand, DVDs, Downloads etc.
    """

    class Meta:
        name = "erweiterungenComplexType"


@dataclass(kw_only=True)
class ExterneIdComplexType:
    class Meta:
        name = "externe_idComplexType"

    externe_id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    quelle: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class FilmmaterialtypSimpleType(Enum):
    AUSSCHNITTE = "Ausschnitte"
    TRAILER = "Trailer"
    TEASER = "Teaser"
    FEATURE = "Feature"
    SONSTIGES = "Sonstiges"


@dataclass(kw_only=True)
class FolgenangabenComplexType:
    class Meta:
        name = "folgenangabenComplexType"

    folgennummer: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    teil: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    folgenanzahl: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    folgengesamtanzahl: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    staffelfolgennummer: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    staffel: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    staffelanzahl: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    staffel_id: None | str = field(
        default=None,
        metadata={
            "name": "staffel_ID",
            "type": "Attribute",
        },
    )
    ausstrahlungsinfo: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    serien_id: None | str = field(
        default=None,
        metadata={
            "name": "serien_ID",
            "type": "Attribute",
        },
    )
    start: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    letzte_folge: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class FormatgruppeSimpleType(Enum):
    FILM = "Film"
    SERIE = "Serie"
    BUEHNE = "Buehne"
    DOKUMENTATION_REPORTAGE = "Dokumentation/Reportage"
    VERANSTALTUNG = "Veranstaltung"
    SHOW_UNTERHALTUNG = "Show/Unterhaltung"
    MAGAZIN_RATGEBER = "Magazin/Ratgeber"
    INFORMATION = "Information"
    GESPRAECH_VORTRAG = "Gespraech/Vortrag"
    WERBUNG = "Werbung"
    SONSTIGES = "Sonstiges"


class GeschlechtSimpleType(Enum):
    M = "m"
    W = "w"
    N = "n"
    UNBEKANNT = "unbekannt"


class GueltigkeitSimpleType(Enum):
    SENDUNG = "sendung"
    STAFFEL = "staffel"
    GESAMT = "gesamt"


@dataclass(kw_only=True)
class KlammerComplexType:
    class Meta:
        name = "klammerComplexType"

    unter_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "min_occurs": 1,
        },
    )
    inhalt: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    anzahl: int = field(
        metadata={
            "type": "Attribute",
        }
    )


class LaenderschemaSimpleType(Enum):
    PID = "pid"
    ISO = "iso"
    KFZ = "kfz"
    ANDERE = "andere"


@dataclass(kw_only=True)
class MediumfreigabeComplexType:
    class Meta:
        name = "mediumfreigabeComplexType"

    freigabeart: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nutzung_von: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nutzung_bis: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    veroeffentlichungshinweis: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MitwirkendeFunktionSimpleType(Enum):
    ANIMATION = "Animation"
    AUSSTATTUNG = "Ausstattung"
    AUTOR = "Autor"
    BAUTEN = "Bauten"
    BEARBEITUNG = "Bearbeitung"
    BETEILIGTE_FIRMEN = "Beteiligte Firmen"
    BILDREGIE = "Bildregie"
    BUCH = "Buch"
    CAMEOAUFTRITT = "Cameoauftritt"
    CASTING = "Casting"
    CHOREOGRAPHIE = "Choreographie"
    COACH = "Coach"
    CO_KOMMENTAR = "Co-Kommentar"
    CO_MODERATION = "Co-Moderation"
    DARSTELLER = "Darsteller"
    DIRIGENT = "Dirigent"
    DREHBUCH = "Drehbuch"
    ELEKTRIK = "Elektrik"
    EXPERTE = "Experte"
    FERNSEHREGIE = "Fernsehregie"
    FRISUREN = "Frisuren"
    GAST = "Gast"
    GASTGEBER = "Gastgeber"
    GASTSTAR = "Gaststar"
    HERSTELLUNGSLEITUNG = "Herstellungsleitung"
    INSZENIERUNG = "Inszenierung"
    INTERPRET = "Interpret"
    JURY = "Jury"
    KAMERA = "Kamera"
    KANDIDAT = "Kandidat"
    KOCH = "Koch"
    KOMMENTAR = "Kommentar"
    KOMPONIST = "Komponist"
    KOST_M = "Kostüm"
    LIBRETTIST = "Librettist"
    MASKE = "Maske"
    MITWIRKENDE = "Mitwirkende"
    MODERATION = "Moderation"
    MUSIK = "Musik"
    MUSIKALISCHE_LEITUNG = "Musikalische Leitung"
    ORIGINALSTIMME = "Originalstimme"
    PERSONENHINWEISE = "Personenhinweise"
    PRODUKTIONSDESIGN = "Produktionsdesign"
    PRODUKTIONSFIRMA = "Produktionsfirma"
    PRODUKTIONSLEITUNG = "Produktionsleitung"
    PRODUZENT = "Produzent"
    RATETEAM = "Rateteam"
    REDAKTION = "Redaktion"
    REDNER = "Redner"
    REGIE = "Regie"
    REGIE_ASSISTENZ = "Regie-Assistenz"
    REPORTER = "Reporter"
    SCHNITT = "Schnitt"
    SFX_FIRMEN = "SFX Firmen"
    SOLIST = "Solist"
    SOUND_MIX = "Sound-Mix"
    SPEZIALEFFEKTE = "Spezialeffekte"
    SPEZIALPERSONEN = "Spezialpersonen"
    SPRECHER = "Sprecher"
    STIMME = "Stimme"
    STUDIO = "Studio"
    STUNT = "Stunt"
    SZENEN_B_HNENBILD = "Szenen-/Bühnenbild"
    TEAM = "Team"
    TON = "Ton"
    VERANTWORTLICH = "Verantwortlich"
    VERLEIH = "Verleih"
    VERTRIEB = "Vertrieb"
    VISUELLE_EFFEKTE = "Visuelle Effekte"
    VORLAGE = "Vorlage"
    VORLESER = "Vorleser"
    SONSTIGES = "Sonstiges"


@dataclass(kw_only=True)
class OriginallaengeComplexType:
    class Meta:
        name = "originallaengeComplexType"

    kino: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vhs: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dvd: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tv_premiere: None | int = field(
        default=None,
        metadata={
            "name": "tv-premiere",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PersonennameComplexType:
    class Meta:
        name = "personennameComplexType"

    titel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vorname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    namensanhang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class QuelleComplexType:
    class Meta:
        name = "quelleComplexType"

    quelle: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    copyright: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    quelltext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SdzBildComplexTypeArt(Enum):
    SCHWARZWEI = "schwarzweiß"
    TEILWEISE_SCHWARZWEI = "teilweise schwarzweiß"
    RESTAURIERT = "restauriert"
    VIRAGIERT = "viragiert"
    COLORIERT = "coloriert"
    DREIDIMENSIONAL = "dreidimensional"
    D2MAC = "d2mac"


@dataclass(kw_only=True)
class SdzBildverhaeltnisComplexType:
    class Meta:
        name = "sdz_bildverhaeltnisComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    verhaeltnis: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    anamorph: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SdzDolbyComplexType:
    class Meta:
        name = "sdz_dolbyComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SdzHdComplexType:
    class Meta:
        name = "sdz_hdComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    aufloesung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SdzPremiereComplexTypeArt(Enum):
    PREMIERE = "Premiere"
    FREE_TV_PREMIERE = "Free-TV-Premiere"
    DEUTSCHLANDPREMIERE = "Deutschlandpremiere"
    WELTPREMIERE = "Weltpremiere"


@dataclass(kw_only=True)
class SdzSonstigeComplexType:
    class Meta:
        name = "sdz_sonstigeComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    art: str = field(
        metadata={
            "type": "Attribute",
        }
    )


class SdzTerminComplexTypeArt(Enum):
    LIVE = "Live"
    ZEITVERSETZT = "Zeitversetzt"
    NEU = "Neu"
    LETZTE_AUSSTRAHLUNG = "Letzte Ausstrahlung"
    JUGENDSCHUTZ_VORSPERRE = "Jugendschutz Vorsperre"
    VERSCHL_SSELT = "Verschlüsselt"
    UNVERSCHL_SSELT = "Unverschlüsselt"
    JUBIL_UM = "Jubiläum"
    INTERAKTIV = "Interaktiv"
    GEB_RDENSPRACHE = "Gebärdensprache"


class SdzTonComplexTypeArt(Enum):
    STUMMFILM = "Stummfilm"
    MONO = "Mono"
    NEUVERTONT = "neuvertont"
    RESTAURIERT = "restauriert"
    OM_U = "OmU"
    STEREO = "Stereo"
    MEHRKANAL = "Mehrkanal"
    AUDIODESCRIPTION = "Audiodescription"
    SURROUNDSOUND = "Surroundsound"
    SYNCHRONFASSUNG = "Synchronfassung"


@dataclass(kw_only=True)
class SdzUhdComplexType:
    class Meta:
        name = "sdz_uhdComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    aufloesung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SenderkategorieSimpleType(Enum):
    VOLLPROGRAMM = "Vollprogramm"
    FILME = "Filme"
    SERIE = "Serie"
    DOKUMENTATION_REPORTAGE = "Dokumentation/Reportage"
    NEWS = "News"
    SPORT = "Sport"
    MUSIK = "Musik"
    SONSTIGES = "Sonstiges"


class StreamformatSimpleType(Enum):
    OGG = "ogg"
    AVI = "avi"
    MPG = "mpg"
    XVID = "xvid"
    FLV = "flv"
    RM = "rm"
    WMV = "wmv"
    XAP = "xap"
    MOV = "mov"


@dataclass(kw_only=True)
class TeletextComplexType:
    class Meta:
        name = "teletextComplexType"

    tafel: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    beschreibung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TerminrechteBedingungComplexType:
    class Meta:
        name = "terminrechteBedingungComplexType"

    wert: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    operator: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    reihenfolge: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    erlaubt: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    wert_attribute: None | int = field(
        default=None,
        metadata={
            "name": "wert",
            "type": "Attribute",
        },
    )
    einheit: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TermintypSimpleType(Enum):
    NEU = "neu"
    LOESCHEN = "loeschen"
    WIEDERHERSTELLEN = "wiederherstellen"
    ERGAENZEN = "ergaenzen"
    ZEITAENDERUNG = "zeitaenderung"
    ZEITAENDERUNG_ERGAENZEN = "zeitaenderung_ergaenzen"
    WIE_GEPLANT = "wie geplant"


class TextartSimpleType(Enum):
    KURZTEXT = "Kurztext"
    VORSPANN = "Vorspann"
    BESCHREIBUNG = "Beschreibung"
    ALLGEMEIN = "Allgemein"
    HINTERGRUND = "Hintergrund"
    AUSZEICHNUNG = "Auszeichnung"
    KRITIK = "Kritik"
    HIGHLIGHT = "Highlight"
    BIOGRAPHIE = "Biographie"
    WERK = "Werk"


class TextmaterialtypSimpleType(Enum):
    PRESSEHEFT = "Presseheft"
    SONSTIGES = "Sonstiges"


@dataclass(kw_only=True)
class ThemenComplextype:
    class Meta:
        name = "themenComplextype"

    thementitel: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    sprache_thementitel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    themenreihenfolge: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    thementext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache_thementext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TitelartSimpleType(Enum):
    TITEL = "titel"
    UNTERTITEL = "untertitel"
    ORIGINALTITEL = "originaltitel"
    ORIGINALUNTERTITEL = "originaluntertitel"
    REIHENTITEL = "reihentitel"
    SENDEPLATZTITEL = "sendeplatztitel"
    SONSTIGER_TITEL = "sonstiger_titel"
    THEMENTITEL = "thementitel"


class TonmaterialtypSimpleType(Enum):
    O_TON = "O-Ton"
    INTERVIEW = "Interview"
    SONSTIGES = "Sonstiges"


@dataclass(kw_only=True)
class VpsComplexType:
    class Meta:
        name = "vpsComplexType"

    datum_zeit: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )
    showview_vps: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class WiederholungComplexType:
    class Meta:
        name = "wiederholungComplexType"

    datum: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    zeit: None | XmlTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sender: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bezug_id: None | str = field(
        default=None,
        metadata={
            "name": "bezugID",
            "type": "Attribute",
        },
    )
    erstausstrahlung: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    infotext: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ZeitbezugSimpleType(Enum):
    DAZWISCHEN = "dazwischen"
    ANSCHLIE_END = "anschließend"


@dataclass(kw_only=True)
class ZeitraumComplexType:
    class Meta:
        name = "zeitraumComplexType"

    jahr: None | ZeitraumComplexType.Jahr = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    jahrspezial: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )

    @dataclass(kw_only=True)
    class Jahr:
        von: XmlPeriod = field(
            metadata={
                "type": "Attribute",
            }
        )
        bis: None | XmlPeriod = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class AliasComplexType:
    class Meta:
        name = "aliasComplexType"

    aliastitel: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    titelzusatz: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    titelart: TitelartSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    titelreihenfolge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AltersangabenComplexType:
    class Meta:
        name = "altersangabenComplexType"

    fsk: None | AltersfreigabeSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fsf: None | AltersfreigabeSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    jk: None | bool = field(
        default=None,
        metadata={
            "name": "JK",
            "type": "Attribute",
        },
    )
    empfehlung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,2}",
        },
    )


@dataclass(kw_only=True)
class BildmaterialComplexType:
    class Meta:
        name = "bildmaterialComplexType"

    person_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gruppe_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    dateiformat: None | DateiformatBildSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hoehe: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    breite: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aufloesung: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bildmaterialtyp: None | BildmaterialtypSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bildunterschrift: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fotograf: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ErstausstrahlungComplexType:
    class Meta:
        name = "erstausstrahlungComplexType"

    erstausstrahlungzeitraum: None | ZeitraumComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gueltigkeit: GueltigkeitSimpleType = field(
        default=GueltigkeitSimpleType.SENDUNG,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class GruppenmitgliedComplexType:
    class Meta:
        name = "gruppenmitgliedComplexType"

    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    von: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bis: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    gruppen_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    funktion: None | MitwirkendeFunktionSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class KlassifizierungComplexType:
    class Meta:
        name = "klassifizierungComplexType"

    genre: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    schlagwort: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    dvbsigenre: None | DvbsigenreComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    formatgruppe: FormatgruppeSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    kategorie: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hauptgenre: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LandComplexType:
    class Meta:
        name = "landComplexType"

    laendername: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    laenderabkuerzung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    laender_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    laenderschema: None | LaenderschemaSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    laenderreihenfolge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LinkComplexType:
    class Meta:
        name = "linkComplexType"

    link: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    streamformat: None | StreamformatSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    titel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    beschreibung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    verfuegbarkeit: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MitgliederComplexType:
    class Meta:
        name = "mitgliederComplexType"

    name: PersonennameComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    person_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    von: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bis: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SdzBildComplexType:
    class Meta:
        name = "sdz_bildComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    art: SdzBildComplexTypeArt = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SdzPremiereComplexType:
    class Meta:
        name = "sdz_premiereComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    art: SdzPremiereComplexTypeArt = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SdzTerminComplexType:
    class Meta:
        name = "sdz_terminComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    art: SdzTerminComplexTypeArt = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SdzTonComplexType:
    class Meta:
        name = "sdz_tonComplexType"

    vorhanden: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    art: SdzTonComplexTypeArt = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SonderzeitComplexType:
    class Meta:
        name = "sonderzeitComplexType"

    zeitbezug: ZeitbezugSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    bezugid: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class TerminrechteComplexType:
    class Meta:
        name = "terminrechteComplexType"

    wert: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bedingung: list[TerminrechteBedingungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    rechteart: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    provider: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    erlaubt: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    wert_attribute: None | int = field(
        default=None,
        metadata={
            "name": "wert",
            "type": "Attribute",
        },
    )
    einheit: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TextComplexType:
    class Meta:
        name = "textComplexType"

    value: str = field(default="")
    textart: TextartSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    quelle: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    laenge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    erstellung: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    letzte_aenderung: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TextmaterialComplexType:
    class Meta:
        name = "textmaterialComplexType"

    dateiformat: None | DateiformatTextSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    textmaterialtyp: None | TextmaterialtypSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FilmmaterialComplexType:
    class Meta:
        name = "filmmaterialComplexType"

    person_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gruppe_id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    ton: list[SdzTonComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    dolby: None | SdzDolbyComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bild: list[SdzBildComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    hd: None | SdzHdComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    uhd: None | SdzUhdComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bildverhaeltnis: None | SdzBildverhaeltnisComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sonstige: list[SdzSonstigeComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    dateiformat: None | DateiformatBewegtbildSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    filmmaterialtyp: None | FilmmaterialtypSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    laenge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hoehe: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    breite: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fps: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class GruppeComplexType:
    class Meta:
        name = "gruppeComplexType"

    aliasname: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    mitglieder: list[MitgliederComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    gruppen_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    gruendung: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aufloesung: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OnlinearchivComplexType:
    class Meta:
        name = "onlinearchivComplexType"

    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    verfuegbar: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    verfuegbar_von: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    verfuegbar_bis: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    info: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrtComplexType:
    class Meta:
        name = "ortComplexType"

    land: list[LandComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    ort: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stadt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    info: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PersonComplexType:
    class Meta:
        name = "personComplexType"

    name: PersonennameComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    aliasname: list[PersonennameComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    geburtsname: None | PersonennameComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    geburtsland: None | LandComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gruppenmitglied: list[GruppenmitgliedComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    person_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    geschlecht: GeschlechtSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    geburtsdatum: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    geburtsstadt: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    todesdatum: None | XmlPeriod | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ServiceComplexType:
    class Meta:
        name = "serviceComplexType"

    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    logo: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    presselounge: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    kuerzel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    copyright: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kostenpflicht: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kosteninfos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kontaktdaten: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sonstige_infos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SonderzeichenComplexType:
    class Meta:
        name = "sonderzeichenComplexType"

    ton: list[SdzTonComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    dolby: None | SdzDolbyComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bild: list[SdzBildComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    hd: None | SdzHdComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    uhd: None | SdzUhdComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bildverhaeltnis: None | SdzBildverhaeltnisComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    premiere: None | SdzPremiereComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    termin: list[SdzTerminComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sonstige: list[SdzSonstigeComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )


@dataclass(kw_only=True)
class TerminartComplexType:
    class Meta:
        name = "terminartComplexType"

    klammer: None | KlammerComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sonderzeit: None | SonderzeitComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    alternativ: None | AlternativComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    klammer_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    regional: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TippComplexType:
    class Meta:
        name = "tippComplexType"

    text: list[TextComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    art: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    quelle: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    genre: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TitelComplexType:
    class Meta:
        name = "titelComplexType"

    alias: list[AliasComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    themen: list[ThemenComplextype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    episoden: list[EpisodeComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    termintitel: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    titelzusatz: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TonmaterialComplexType:
    class Meta:
        name = "tonmaterialComplexType"

    ton: SdzTonComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    dateiformat: None | DateiformatTonSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tonmaterialtyp: None | TonmaterialtypSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MediumtypComplexType:
    class Meta:
        name = "mediumtypComplexType"

    textmaterial: None | TextmaterialComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bildmaterial: None | BildmaterialComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    filmmaterial: None | FilmmaterialComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    tonmaterial: None | TonmaterialComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )


@dataclass(kw_only=True)
class MitwirkendertypComplexType:
    class Meta:
        name = "mitwirkendertypComplexType"

    person: None | PersonComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gruppe: None | GruppeComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )


@dataclass(kw_only=True)
class ProduktionComplexType:
    class Meta:
        name = "produktionComplexType"

    produktionsland: list[LandComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    produktionszeitraum: None | ZeitraumComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    produktionsort: list[OrtComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gueltigkeit: GueltigkeitSimpleType = field(
        default=GueltigkeitSimpleType.SENDUNG,
        metadata={
            "type": "Attribute",
        },
    )
    europaeischeproduktion: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TerminComplexType:
    class Meta:
        name = "terminComplexType"

    externe_id: list[ExterneIdComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    vps: None | VpsComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    terminrechte: list[TerminrechteComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    terminart: None | TerminartComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    wiederholung: list[WiederholungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    termintyp: TermintypSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    termin_id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    reihenfolge: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    start: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )
    exakt: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    exaktende: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    circa: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ende: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )
    programmtag: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nettolaenge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    showview: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vorprogramm: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ersatzprogramm: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bestellnummer: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class InfosComplexType:
    class Meta:
        name = "infosComplexType"

    altersangaben: None | AltersangabenComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    produktion: list[ProduktionComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "max_occurs": 3,
        },
    )
    erstausstrahlung: list[ErstausstrahlungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "max_occurs": 3,
        },
    )
    klassifizierung: KlassifizierungComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    originallaenge: None | OriginallaengeComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    veranstaltung: None | OrtComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sonderzeichen: None | SonderzeichenComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sprache: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    untertitelung: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    teletext: list[TeletextComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    tipp: list[TippComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    bewertung: list[BewertungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    folge: None | FolgenangabenComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    download: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    onlinearchiv: list[OnlinearchivComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    kinostart: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dvd_veroeffentlichung: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DVD_veroeffentlichung",
            "type": "Attribute",
        },
    )
    zusatzinfo: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MediumComplexType:
    class Meta:
        name = "mediumComplexType"

    quelle: list[QuelleComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "min_occurs": 1,
        },
    )
    schlagwort: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    freigabe: list[MediumfreigabeComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    altersangabe: None | AltersangabenComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    untertitelung: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    mediumtyp: MediumtypComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    dateiname: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    medium_id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dateigroesse: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reihenfolge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    titel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    beschreibung: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    gueltigkeit: GueltigkeitSimpleType = field(
        default=GueltigkeitSimpleType.SENDUNG,
        metadata={
            "type": "Attribute",
        },
    )
    letzte_aenderung: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MitwirkenderComplexType:
    class Meta:
        name = "mitwirkenderComplexType"

    mitwirkendentyp: MitwirkendertypComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    texte: list[TextComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    auszeichnung: list[AuszeichnungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    medium: list[MediumComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    funktion: MitwirkendeFunktionSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    reihenfolge: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    rolle: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    themenreihenfolge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    episodenreihenfolge: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    gueltigkeit: GueltigkeitSimpleType = field(
        default=GueltigkeitSimpleType.SENDUNG,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MitwirkungComplexType:
    class Meta:
        name = "mitwirkungComplexType"

    mitwirkender: list[MitwirkenderComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SendungComplexType:
    class Meta:
        name = "sendungComplexType"

    externe_id: list[ExterneIdComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    termin: TerminComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    titel: TitelComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    infos: InfosComplexType = field(
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        }
    )
    auszeichnung: list[AuszeichnungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    mitwirkende: None | MitwirkungComplexType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    text: list[TextComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    medium: list[MediumComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sendung_id: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class AblaufComplexType:
    class Meta:
        name = "ablaufComplexType"

    plattform: list[ServiceComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    stream: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    sendung: list[SendungComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "min_occurs": 1,
        },
    )
    ablauftyp: AblauftypSimpleType = field(
        metadata={
            "type": "Attribute",
        }
    )
    ablaufstart: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )
    ablaufende: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class SenderComplexType:
    class Meta:
        name = "senderComplexType"

    showview: list[SenderComplexType.Showview] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    url: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    senderlogo: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    gruppe: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    presselounge: list[LinkComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
        },
    )
    ablauf: list[AblaufComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://struppi.tv/xsd/",
            "min_occurs": 1,
        },
    )
    sender_id: None | str = field(
        default=None,
        metadata={
            "name": "sender_ID",
            "type": "Attribute",
        },
    )
    nit: None | str = field(
        default=None,
        metadata={
            "name": "NIT",
            "type": "Attribute",
        },
    )
    lcn: None | str = field(
        default=None,
        metadata={
            "name": "LCN",
            "type": "Attribute",
        },
    )
    sendername: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    senderkuerzel: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    senderkategorie: None | SenderkategorieSimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vps: bool = field(
        metadata={
            "type": "Attribute",
        }
    )
    sprache: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    empfang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    kontaktdaten: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sonstige_senderinfos: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Showview:
        land: None | LandComplexType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://struppi.tv/xsd/",
            },
        )
        kanal: int = field(
            metadata={
                "type": "Attribute",
            }
        )


@dataclass(kw_only=True)
class Programmdaten:
    class Meta:
        name = "programmdaten"
        namespace = "http://struppi.tv/xsd/"

    lieferant: None | ServiceComplexType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    erweiterungen: list[ErweiterungenComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sender: list[SenderComplexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    generierungsdatum: XmlDateTime = field(
        metadata={
            "type": "Attribute",
        }
    )
