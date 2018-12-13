import adafruit_thermal_printer
import serial

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
 
printer = ThermalPrinter(uart)

printer.warm_up()


printer.size = adafruit_thermal_printer.SIZE_MEDIUM
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
printer.print('Garam Market!')

printer.underline = None
printer.size = adafruit_thermal_printer.SIZE_SMALL
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print('9700 Gilman Dr')
printer.print('La Jolla, CA, 92093')

printer.feed(2)

#Month/Date/Year/Current Time

printer.feed(2)

printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
#Product	Price	Amount	Total_Price

printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT
---------------------------
printer.bold = True
printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print('Total: ')
printer.bold = False

printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT
#TotalPrice

printer.feed(2)

printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
printer.print('Phone: (858) 622-0067')
printer.print('Email: www.santoriniislandgrill.net')

printer.feed(2)

printer.print_barcode('123456789012', printer.UPC_A)

printer.feed(2)

#QR Code
