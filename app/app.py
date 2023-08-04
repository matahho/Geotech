from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QToolButton , QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog , QErrorMessage , QToolTip
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor , QPainter, QBrush , QPixmap , QIcon , QCursor





from PyQt5.QtCore import Qt , QSize
import sys , math



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure
from matplotlib.widgets import Cursor


from module7 import Module7
from module6 import Module6
from module5 import Module5
from module4 import Module4
from module3 import Module3
from module2 import Module2
from module1 import Module1
from Home import Home



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setStyleSheet("background-color:#fafcff;")
        self.title = 'GeOnin Software'
        self.setWindowTitle(self.title)
        



        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.module1 = Module1(self)
        self.module2 = Module2(self)
        self.module3 = Module3(self)
        self.module4 = Module4(self)
        self.module5 = Module5(self)
        self.module6 = Module6(self)
        self.module7 = Module7(self)
        self.home = Home(self)
        # Add tabs

        self.tabs.addTab(self.home , "Home")
        self.tabs.addTab(self.module1,"Shallow Foundation")
        self.tabs.addTab(self.module2 , "Pile")
        self.tabs.addTab(self.module3 ,"Liquefaction")
        self.tabs.addTab(self.module4 , "Settelment")
        self.tabs.addTab(self.module5 , "Retaining Wall")
        self.tabs.addTab(self.module6 , "Dam Uplift Force")
        self.tabs.addTab(self.module7 , "Stress Distribution")
        #self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.setTabShape(QTabWidget.Rounded)   


        #tooltip for tabs
        self.tabs.setTabToolTip(0, 'Home Page')
        self.tabs.setTabToolTip(1, 'Shallow Foundation Bearing Capacity')
        self.tabs.setTabToolTip(2, 'Pile Bearing Capacity')
        self.tabs.setTabToolTip(3, 'Liquefaction Calculation')
        self.tabs.setTabToolTip(4, 'Settelment Calculation')
        
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.show()
        
        self.showFullScreen()
        self.setFixedSize(self.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("""QLabel {
                            color :#146C94 ;
                        
                            }
                        """)
    ex = App()
    sys.exit(app.exec_())
