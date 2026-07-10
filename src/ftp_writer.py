import ftplib
import io


def write_file_to_ftp(content: str, file_name: str, url: str, user: str, password: str):
    file = io.BytesIO()

    file_wrapper = io.TextIOWrapper(file, encoding='utf-8')
    file_wrapper.write(content)
    file.seek(0)

    with ftplib.FTP() as ftp:
        ftp.connect(host=url, port=21)
        ftp.set_debuglevel(1)
        ftp.login(user=user, passwd=password)
        ftp.storbinary(f"STOR {file_name}", file)
        ftp.quit()
