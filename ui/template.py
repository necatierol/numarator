import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer, QTime

from data import Data


data = Data()

class Template():
	def __init__(self):
		super().__init__()

	def header(self):
		layout = QHBoxLayout()

		logo = QLabel()
		pixmap = QPixmap('ui/logo.jpeg')
		logo.setPixmap(pixmap)
		logo.resize(pixmap.width(), pixmap.height())

		label = QLabel(data.getCompanyName())

		label.setAlignment(Qt.AlignCenter)

		layout.addWidget(logo, 0)
		layout.addWidget(label, 1)

		return layout
