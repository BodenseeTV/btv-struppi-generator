from io import BytesIO

import msoffcrypto


def read_excel(excel_path: str, excel_password: str):
    decrypted = BytesIO()

    with open(excel_path, "rb") as f:
        office_file = msoffcrypto.OfficeFile(f)
        office_file.load_key(password=excel_password)
        office_file.decrypt(decrypted)

    decrypted.seek(0)
    return decrypted
