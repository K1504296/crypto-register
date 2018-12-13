from Bill import bill
from User import user

import serial
import subprocess
import adafruit_thermal_printer

PORT = "/dev/ttyUSB0"
BAUDRATE = 9600
TIMEOUT = 3000


def printOutFinalBill():
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.67)
    uart = serial.Serial(PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    printer = ThermalPrinter(uart)
    printer.warm_up()


    printer.underline = None
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
    printer.print('Garam Market!')

    printer.print('9700 Gilman Dr')
    printer.print('La Jolla, CA, 92093')

    printer.feed(2)

    printer.print(' Product       Price    Quantity')
    printer.feed(1)
    # printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
    printer.print('-------------------------------')
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.print(bill.toString())
    printer.print('-------------------------------')

    printer.bold = True
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.print('Total: ')
    printer.bold = False

    printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT
    printer.print(str(round(bill.trxTotal(), 2)) + " TRX")

    printer.feed(2)
    script = ["python2.7", "src/PrintQRCode.py", user.address]
    process = subprocess.Popen(" ".join(script),
                               shell=True,
                               env={"PYTHONPATH": "."})
