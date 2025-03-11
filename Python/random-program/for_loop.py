# generate qr code
import pyqrcode
from PIL import Image
link = input("Enter anything to generate QR code: ")
qrCode = pyqrcode.create(link)
qrCode.png("QRcode.png", scale=5)
Image.open("QRcode.png")