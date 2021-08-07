from playsound import playsound

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from data import Data
from ui.template import Template

data = Data()
template = Template()

keys = {
	65: "A",
	66: "B"
}

class ShowScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.labels = data.getCommands()
		self.grouppedNumbers = data.getGrouppedNumbers()
		self.ui_settings = data.getUISettings()
		self.show_number_count = self.ui_settings["show_number_count"]

		self.setStyleSheet(open("ui/style.qss", "r").read())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.initUI()

	def keyPressEvent(self, e):
		if(e.key() in keys):
			key = keys[e.key()]
			next_number = data.getNextNumber(key)
			if(next_number != 0):
				self.setNumbers(key, next_number)
				self.playNotificationSound()
			else:
				print("next number is not found")
		else:
			print("invalid key... please press A or B")

	def initUI(self):
		 # Create widget
		widget = QWidget(self)
		self.setCentralWidget(widget)

		layout = QVBoxLayout()
		layout.addLayout(template.header(), 0)
		layout.addWidget(self.createGridLayout(), 1)
		widget.setLayout(layout)
        
		self.showMaximized()
		self.show()

	def createGridLayout(self):
		horizontalGroupBox = QGroupBox()
		horizontalLayout = QHBoxLayout()

		for key in list(self.labels):
			horizontalLayout.addLayout(self.createNumberColumn(key))

		horizontalGroupBox.setLayout(horizontalLayout)
		
		return horizontalGroupBox

	def createNumberColumn(self, key):
		verticalLayout = QVBoxLayout()
		titleLabel = QLabel(self.labels[key]["title"])
		titleLabel.setAlignment(Qt.AlignCenter)
		verticalLayout.addWidget(titleLabel, 1)

		layout = QVBoxLayout()
		numbers = self.grouppedNumbers[key]
		numbers.reverse()

		for i in range(self.show_number_count):
			number = numbers[i] if len(numbers) > i else ''
			numberLabel = QLabel("{}".format(number))
			numberLabel.setObjectName("{}_{}".format(key, "active" if i == 0 else "old"))
			numberLabel.setAlignment(Qt.AlignCenter)
			layout.addWidget(numberLabel, 0)

		verticalLayout.addLayout(layout, 2)

		return verticalLayout

	def setNumbers(self, key, number):
		oldNumberLabel = self.findChild(QLabel, "{}_old".format(key))
		activeNumberLabel = self.findChild(QLabel, "{}_active".format(key))

		oldNumberLabel.setText(activeNumberLabel.text())
		activeNumberLabel.setText(str(number))

	def playNotificationSound(self):
		playsound("ui/notification.wav")
