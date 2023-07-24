from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QMessageBox , QToolTip
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog , QErrorMessage , QToolButton
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor , QPixmap , QCursor
from PyQt5.QtCore import Qt , QSize
import sys , math
import numpy as np



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure
import copy





class Home(QWidget):

    def __init__(self, parent):
        super(Home, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.HomeHelp = QToolButton()
        self.HomeHelp.setText("Help")
        self.HomeHelp.setIconSize(QSize(20, 20))

        self.Home = QWidget()
        self.Home.layout = QGridLayout(self)

        self.HomeHelp.clicked.connect(self.HomeHelpFunction)

        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.Home.layout.addWidget(self.HomeHelp, 0, 0, alignment=Qt.AlignRight)
        self.Home.layout.addWidget(self.logo, 1, 0, alignment=Qt.AlignCenter)

        self.Home.setLayout(self.Home.layout)

        self.layout.addWidget(self.Home)

        self.setLayout(self.layout)

    
    def HomeHelpFunction(self):
        message_box = QMessageBox()
        message_box.setWindowTitle('Home Help')
        about = "GeOnion Software\n\nClient: Dr Khaleghi\n\nRelease Date: May 2023\n\nVersion:1.0.0"
        message_box.setText(about)
        message_box.exec_()
