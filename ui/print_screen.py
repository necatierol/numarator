import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from data import Data
from ui.template import Template


data = Data()
template = Template()

class PrintScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.labels = data.getCommands()
		self.grouppedNumbers = data.getGrouppedNumbers()
		self.ui_settings = data.getUISettings()
		self.show_number_count = self.ui_settings["show_number_count"]

		self.setStyleSheet(open("ui/style.qss", "r").read())
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.initUI()

	def initUI(self):
		widget = QWidget(self)
		self.setCentralWidget(widget)

		layout = QGridLayout()

		printButton = QPushButton(data.getCreateNumberButtonMessage())
		printButton.clicked.connect(self.print_number)

		layout.addLayout(template.header(), 0, 0, 1, 0)
		layout.addWidget(printButton, 1, 0, 5, 0)
		printButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		widget.setLayout(layout)

		self.showMaximized()
		self.show()

	def print_number(self):
		new_number = data.createNumber()
		print("number {} is printing".format(new_number))