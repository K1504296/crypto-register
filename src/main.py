import sys
import os
sys.path.append("/home/noopur/kivy")
sys.path.append(os.getcwd() + "/src")
sys.path.append(os.getcwd() + "/src/APIs")
sys.path.append(os.getcwd() + "/src/demos")
sys.path.append(os.getcwd() + "/pyqt_stuff")
sys.path.append(os.getcwd() + "/tkinter")

from QuickDemo import quickDemo
from FullDemo import fullDemo
from LoginScreen import runLoginApp

def main():
    runLoginApp()
if __name__ == "__main__":
    main()
