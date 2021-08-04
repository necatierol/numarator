import sys
import serial
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from form import Window
from data import Data

data = Data()


settings = data.getComportSettings()
commands = data.getCommands()

# serialport = serial.Serial(
#     settings["serial_name"],
#     settings["baud_rate"],
#     timeout=settings["timeout"])

App = QApplication(sys.argv)
window = Window()

def listener():
    # command = serialport.read()
    command = input("komut")
    cmd = command.decode('utf-8')
    # label.setText(commands[cmd]["message"])
    print (cmd)

timer = QTimer()
# timer.timeout.connect(listener)
timer.start(1000)  # milliseconds

sys.exit(App.exec())