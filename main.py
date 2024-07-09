import qrcode
import datetime


data = "https://drive.google.com/drive/folders/1wv3uN03ZnRQq1MqzfftlQrd6Ys2-nujb?usp=sharing"

current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"qr_code/qrcode_{current_time}.png"

def create_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)
    print(f"QR-код успешно создан и сохранен как {file_name}")

create_qr_code(data, file_name)
