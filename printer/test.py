import adafruit_thermal_printer
import serial

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
 
printer = ThermalPrinter(uart)

printer.warm_up()