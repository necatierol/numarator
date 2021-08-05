import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from data import Data

data = Data()

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.labels = data.getCommands()
		self.grouppedNumbers = data.getGrouppedNumbers()
		self.ui_settings = data.getUISettings()
		self.show_number_count = self.ui_settings["show_number_count"]

		self.setStyleSheet(open("style.qss", "r").read())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.initUI()

	def keyPressEvent(self, e):
		print(e.key())

	def initUI(self):
		 # Create widget
		widget = QWidget(self)
		self.setCentralWidget(widget)

		layout = QVBoxLayout()
		layout.addWidget(self.createBanner(), 0)
		layout.addWidget(self.createGridLayout(), 1)
		widget.setLayout(layout)
        
		self.showMaximized()
		self.show()

	def createBanner(self):
		label = QLabel(self)
		pixmap = QPixmap('./banner.png')
		label.setPixmap(pixmap)
		label.resize(pixmap.width(), pixmap.height())

		return label

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
			numberLabel.setAlignment(Qt.AlignCenter)
			layout.addWidget(numberLabel, 0)

		verticalLayout.addLayout(layout, 2)

		return verticalLayout



	def setMessageText(self, text):
		self.label_1.setText(text)
