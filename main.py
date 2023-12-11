import qrcode as qr
img=qr.make("https://www.amazon.com")
img.save("amazon.png")
