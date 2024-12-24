import qrcode
from PIL import Image


data = "https://docs.google.com/document/d/1bEcSw-jE6D5NfAUqn4wvyyGECN2tTMRjTqb6kPQqk38/edit?usp=sharing"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("qrcode.png")


img.show()
