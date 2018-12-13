from Adafruit_Thermal import *
import sys

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=4,
)
qr.add_data(sys.argv[1])
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)
from sampleqr import *
printer.printBitmap(width, height, data)
#printer.printImage(img, True)
printer.feed(2)
