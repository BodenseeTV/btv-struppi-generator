import argparse

from datetime import datetime, timedelta

from excel_reader import read_excel
from ftp_writer import write_file_to_ftp
from mapper import map_excel_to_xml

parser = argparse.ArgumentParser()
parser.add_argument('--excel-path', dest='excel_path', type=str, required=True, help='Path to the Excel file')
parser.add_argument('--excel-password', dest='excel_password', type=str, help='Password to unlock the Excel')
parser.add_argument('--ftp-enabled', dest='ftp_enabled', type=bool, default=False, help='Uploads the XML via FTP')
parser.add_argument('--ftp-url', dest='ftp_url', type=str, help='The url to upload the file to')
parser.add_argument('--ftp-user', dest='ftp_user', type=str, help='The user with which to upload')
parser.add_argument('--ftp-password', dest='ftp_password', type=str, help='The password with which to upload')
args = parser.parse_args()

excel = read_excel(args.excel_path, args.excel_password)

start_date = datetime.today()
start_date = start_date.replace(hour=4, minute=30, second=0, microsecond=0)
end_date = start_date + timedelta(days=15)

xml_string = map_excel_to_xml(excel, start_date, end_date)

if args.ftp_enabled:
    write_file_to_ftp(xml_string, "btv.xml", args.ftp_url, args.ftp_user, args.ftp_password)

else:
    with open("btv.xml", "w") as file:
        file.write(xml_string)