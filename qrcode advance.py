import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://www.linkedin.com/posts/rajkiran-pund-354b11a2_entrepreneurship-entrepreneurshipopportunity-activity-7126552536462819328-iWta?utm_source=share&utm_medium=member_android")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="black")
img.save("amazon.png")

