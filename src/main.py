import argparse
import ftplib
import io
from datetime import datetime, timedelta

from mapper import map_excel_to_xml

# TODO: unencrypt excel with password

parser = argparse.ArgumentParser()
parser.add_argument('--excel-path', dest='excel_path', type=str, required=True, help='Path to the Excel file')
parser.add_argument('--excel-password', dest='excel_password', type=str, help='Password to unlock the Excel')
parser.add_argument('--ftp-enabled', dest='ftp_enabled', type=bool, default=False, help='Uploads the XML via FTP')
parser.add_argument('--ftp-url', dest='ftp_url', type=str, help='The url to upload the file to')
parser.add_argument('--ftp-user', dest='ftp_user', type=str, help='The user with which to upload')
parser.add_argument('--ftp-password', dest='ftp_password', type=str, help='The password with which to upload')
args = parser.parse_args()

start_date = datetime.today()
start_date = start_date.replace(hour=4, minute=30, second=0, microsecond=0)
end_date = start_date + timedelta(days=15)

xml_string = map_excel_to_xml(args.excel_path, start_date, end_date)

if args.ftp_enabled:
    file = io.BytesIO()

    file_wrapper = io.TextIOWrapper(file, encoding='utf-8')
    file_wrapper.write(xml_string)
    file.seek(0)

    with ftplib.FTP() as ftp:
        ftp.connect(host=args.ftp_url, port=21)
        ftp.set_debuglevel(1)
        ftp.login(user=args.ftp_user, passwd=args.ftp_password)
        ftp.storbinary("STOR btv.xml", file)
        ftp.quit()

else:
    with open("../output/btv.xml", "w") as file:
        file.write(xml_string)