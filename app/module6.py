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






class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Module 6'
        self.setWindowTitle(self.title)
        
        self.table_widget = Module6(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
        self.showFullScreen()
        self.setFixedSize(self.size())




class Module6(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        
        self.module6 = QWidget()


        
        # Create first tab
        self.module6.layout = QVBoxLayout(self)
        self.addModule6HelpToLayout(self.module6.layout )
        self.input_datas(self.module6.layout)
        
        

        self.ButtonLayout = QHBoxLayout()
        self.processButtonFunction(self.ButtonLayout)
        self.resetButtonFunction(self.ButtonLayout)
        self.module6.layout.addLayout(self.ButtonLayout)

    
        self.module6.setLayout(self.module6.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.module6)
        self.setLayout(self.layout)
        
        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.pixmap = self.pixmap.scaled(600,600) 
        self.logo.setPixmap(self.pixmap)

        #self.logo.resize(self.pixmap.width(),self.pixmap.height())
        self.layout.addWidget(self.logo)

    def addModule6HelpToLayout(self , layout):
        self.module6Help = QToolButton()
        self.module6Help.setText("Help")  
        self.module6Help.setIconSize(QSize(20 , 20))
        layout.addWidget(self.module6Help ,alignment = Qt.AlignRight)
        self.module6Help.clicked.connect(self.module6HelpFunction)
    def module6HelpFunction(self):
        message_box = QMessageBox()

        message_box.setWindowTitle('Module 6 Help')
        about = "شما در حال استفاده از ماژول  محاسبه نیروی بالابرنده سد بتنی  از نرم افزار GeOnion هستید"
        about2 = "از شبكه جريان می توان براي تعیین فشار برکنش در زير سازه هاي هیدرولیكی استفاده کرد. در این برنامه با حل معادله تراوش دو بعدی به روش تفاضلات محدود با تعداد تلاش بالا مقدار نیروی بالابرنده زیر سد محاسبه می گردد."
        about3 = "این ماژول ضمن محاسبه مجموع نیروی بالابرنده وارد بر سد بتنی، توزیع آن نیرو را در واحد سطح را ترسیم می نماید."

        txt = (about + "\n\n    " + about2 + "\n\n    " + about3 + "\n")
        message_box.setText(txt)
        message_box.exec_()
    def __ConcreteDamToLayouts (self , inputsLayout , i , j ):

        boxesColor = "#e6efff"
        borderColor = "#19A7CE"
        boxesTitleColor = "#146C94"
        boxesStyle = """QGroupBox {
                            background-color: %s;
                            border: 2px solid %s;
                            border-radius: 5px;
                            margin-top: 1em;
                            padding-top: 10px;
                        }
                        QGroupBox::title {
                            color: %s; 

                        }""" % (boxesColor , borderColor , boxesTitleColor) 


        ConcreteBox = QGroupBox("CONCRETE DAM")
        ConcreteBox.setStyleSheet(boxesStyle)
        ConcretePart = QFormLayout()
        ConcreteBox.setAlignment(Qt.AlignCenter)

        self.length = QLineEdit()
        self.length.setFixedWidth(80)
        self.length.setValidator(QIntValidator())
        self.length.textChanged.connect(self.enButton)
        self.length.setPlaceholderText("m")
        lengthLabel = QLabel (u"Length (m) ")
        lengthLabel.setToolTip ("طول سد بتنی")
        ConcretePart.addRow (lengthLabel , self.length)






        ConcreteBox.setLayout(ConcretePart)
        #GeneralBox.setAlignment(Qt.AlignCenter)
        inputsLayout.addWidget(ConcreteBox , i , j )
    def __SoilCharacteristic (self , inputsLayout , i , j):
        boxesColor = "#e6efff"
        borderColor = "#19A7CE"
        boxesTitleColor = "#146C94"
        boxesStyle = """QGroupBox {
                            background-color: %s;
                            border: 2px solid %s;
                            border-radius: 5px;
                            margin-top: 1em;
                            padding-top: 10px;
                        }
                        QGroupBox::title {
                            color: %s; 

                        }""" % (boxesColor , borderColor , boxesTitleColor) 


        soilBox = QGroupBox("SOIL CHARACTERISTIC")
        soilBox.setStyleSheet(boxesStyle)
        soilBox.setAlignment(Qt.AlignCenter)
        soilPart = QFormLayout()


        self.D1 = QLineEdit()
        self.D1.setFixedWidth(80)
        self.D1.setValidator(QIntValidator())
        self.D1.textChanged.connect(self.enButton)
        self.D1.setPlaceholderText("m")        
        D1Label = QLabel("D1 (m) ")
        D1Label.setToolTip("ضخامت لایه اول خاک")
        soilPart.addRow (D1Label , self.D1)



        self.D2 = QLineEdit()
        self.D2.setFixedWidth(80)
        self.D2.setValidator(QIntValidator())
        self.D2.textChanged.connect(self.enButton)
        self.D2.setPlaceholderText("m")        
        D2Label = QLabel("D2 (m) ")
        D2Label.setToolTip("ضخامت لایه دوم خاک")
        soilPart.addRow (D2Label , self.D2)



        self.K1 = QLineEdit()
        self.K1.setFixedWidth(80)
        self.K1.setValidator(QDoubleValidator())
        self.K1.textChanged.connect(self.enButton)
        self.K1.setPlaceholderText("m/s")        
        K1Label = QLabel("K1 (m/s)")
        K1Label.setToolTip("ضریب نفوذپذیری لایه اول خاک")
        soilPart.addRow (K1Label , self.K1)


        self.K2 = QLineEdit()
        self.K2.setFixedWidth(80)
        self.K2.setValidator(QDoubleValidator())
        self.K2.textChanged.connect(self.enButton)
        self.K2.setPlaceholderText("m/s")        
        K2Label = QLabel("K2 (m/s)")
        K2Label.setToolTip("ضریب نفوذپذیری لایه دوم خاک")
        soilPart.addRow (K2Label , self.K2)




        soilBox.setLayout(soilPart)
        inputsLayout.addWidget(soilBox , i , j )
    def __WaterHead (self , inputsLayout , i , j ):
        boxesColor = "#e6efff"
        borderColor = "#19A7CE"
        boxesTitleColor = "#146C94"
        boxesStyle = """QGroupBox {
                            background-color: %s;
                            border: 2px solid %s;
                            border-radius: 5px;
                            margin-top: 1em;
                            padding-top: 10px;
                        }
                        QGroupBox::title {
                            color: %s; 

                        }""" % (boxesColor , borderColor , boxesTitleColor) 


        WaterBox = QGroupBox("WATER HEAD")
        WaterBox.setStyleSheet(boxesStyle)
        WaterPart = QFormLayout()
        WaterBox.setAlignment(Qt.AlignCenter)

        self.Ht = QLineEdit()
        self.Ht.setFixedWidth(80)
        self.Ht.setValidator(QDoubleValidator())
        self.Ht.textChanged.connect(self.enButton)
        self.Ht.setPlaceholderText("m")
        HtLabel = QLabel("Ht (m) ")
        HtLabel.setToolTip("هد آب بالا دست")
        WaterPart.addRow (HtLabel , self.Ht)



        self.Hb = QLineEdit()
        self.Hb.setFixedWidth(80)
        self.Hb.setValidator(QDoubleValidator())
        self.Hb.textChanged.connect(self.enButton)
        self.Hb.setPlaceholderText("m")
        HbLabel = QLabel("Hb (m) ")
        HbLabel.setToolTip("هد آب  پایین دست")
        WaterPart.addRow (HbLabel , self.Hb)



        WaterBox.setLayout(WaterPart)
        inputsLayout.addWidget(WaterBox , i , j )
    def input_datas (self,layout ):
        gridLayout = QGridLayout()
        self.__ConcreteDamToLayouts(gridLayout , 0 , 0)
        self.__SoilCharacteristic(gridLayout , 1 , 0)
        self.__WaterHead(gridLayout , 2 , 0)
        layout.addLayout(gridLayout)
    
    def checkHtandHb(self):
        if float(self.Ht.text()) < float(self.Hb.text()):
            raise Exception ("مقدار Ht , Hb نامعتبر است")
        else :
            if float(self.Ht.text()) < 0 or float(self.Hb.text()) < 0 :
                raise Exception ("مقدار Ht , Hb نامعتبر است")
            else :
                pass
        
        
        

    def processButtonFunction (self , layout):
        self.processButton = QPushButton ("Calculate" , self)
        self.processButton.setEnabled(False) 



        self.processButton.clicked.connect(self.process)
        layout.addWidget(self.processButton , alignment = Qt.AlignLeft)

    

    def resetButtonFunction (self , layout):
        self.resetButton = QPushButton ("Reset" , self)

        self.resetButton.clicked.connect(self.resetAll)
        layout.addWidget(self.resetButton , alignment = Qt.AlignRight)



    def process(self):
        try:
            self.checkHtandHb()
            self.damMatrix()
        except Exception as e:
            self.inputError(str(e))




    def resetAll(self):
        theInputs = [self.length , self.D1 , self.D2 , self.K1 , self.K2 , self.Ht , self.Hb ]

        for inp in theInputs:
            inp.clear()

        self.processButton.setEnabled(False)
        
        
        if self.layout.count() > 0:
            layout_item = self.layout.takeAt(1)
            if layout_item:
                layout_item.widget().deleteLater()

                        
            self.logo = QLabel(self)
            self.pixmap = QPixmap('./logo.PNG')
            self.pixmap = self.pixmap.scaled(600,600) 
            self.logo.setPixmap(self.pixmap)

            self.layout.addWidget(self.logo)



    def enButton(self):
        if (self.length.text() == '' or self.D1.text() == '' or self.D2.text() == '' or self.K1.text() == '' or self.K2.text() == '' or self.Ht.text() == '' or self.Hb.text() == '' ):
            self.processButton.setEnabled(False)
        else :
            self.processButton.setEnabled(True)
        return 


    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
        error_dialog.exec_()


    def meanCalc(self , matrix):
        for r in range(1 , matrix.shape[0]):
            for c in range(0 , matrix.shape[1]):

                if c == 0 :
                    if r == matrix.shape[0]-1:
                        matrix[r][c] = (matrix[r-1][c] + matrix[r][c-1])/2
                    elif r == int (self.D1.text()):
                        matrix[r][c] = ((2*float(self.K1.text())/(float(self.K1.text()) + float(self.K2.text())) * matrix[r-1][c]) + (2*float(self.K2.text())/(float(self.K1.text()) + float(self.K2.text())) * matrix[r+1][c]) + 2 * matrix[r][c+1])/4
                    else :
                        matrix[r][c] = (matrix[r-1][c] + matrix[r+1][c] + 2*matrix[r][c+1])/4
                

                elif c == matrix.shape[1]-1:
                    if r == matrix.shape[0]-1:
                        matrix[r][c] = (matrix[r-1][c] + matrix[r][c-1])/2
                    
                    elif r == int (self.D1.text()):
                        matrix[r][c] = ((2*float(self.K1.text())/(float(self.K1.text()) + float(self.K2.text())) * matrix[r-1][c]) + (2*float(self.K2.text())/(float(self.K1.text()) + float(self.K2.text())) * matrix[r+1][c]) + 2 * matrix[r][c-1])/4
                    
                    else:
                        matrix[r][c] = (matrix[r-1][c] + matrix[r+1][c] + 2*matrix[r][c-1])/4
                

                elif r == matrix.shape[0]-1:
                    if c == matrix.shape[1]-1 or c == 0 :
                        pass
                    else :
                        matrix[r][c] = (matrix[r][c-1] + matrix[r][c+1] + 2*matrix[r-1][c])/4
                
                else:
                    if r == int (self.D1.text()):
                        matrix[r][c] = (matrix[r][c-1] + matrix[r][c+1] + (2*float(self.K1.text())/(float(self.K1.text()) + float(self.K2.text())))*matrix[r-1][c] + (2*float(self.K2.text())/(float(self.K1.text()) + float(self.K2.text())))*matrix[r+1][c])/4
                    else:
                        matrix[r][c] = (matrix[r-1][c] + matrix[r+1][c] + matrix[r][c-1] + matrix[r][c+1])/4

        return matrix
        
    def calcHp (self , matrix):
        Hp = np.sum(matrix, axis=0)
        zirSad = Hp[1+int(self.length.text())*2:1+int(self.length.text())*3]
        tension = 10 * zirSad 
        DeltaX = 1 
        forceInPlace = DeltaX * tension
        return forceInPlace
    


    def result (self , force , layout):

        # self.graphWindow = QDialog(self)
        # self.graphWindow.setWindowTitle("Graph")
        # self.graphWindowLayout = QVBoxLayout()
        # self.graphWindow.setLayout(self.graphWindowLayout)



        
        x = []
        for i in range(1 , len(force)+1):
            x.append (i)
        
        y = list (force)



        damShape = Figure(figsize=(7, 5), dpi=100 )
        damShape_axes = damShape.add_subplot(111)



        bars = damShape_axes.bar(x, y , color='#C24EE9')
        damShape_axes.invert_yaxis()
        damShape_shape = FigureCanvas(damShape)

        # for i, bar in enumerate(bars):
        #     value = y[i]
        #     damShape_axes.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')


        sumOfForce = QLabel("مجموع نیروی وارده = " + str(round(force.sum(), 2)) + (" (kN/m)"))
        font = QFont()
        font.setPointSize(20)
        sumOfForce.setFont(font)

        damShape_axes.set_title("Total Force =" + str(round(force.sum(), 2)) + (" (kN/m)"))
                
                
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        damShape_shape.mpl_connect('motion_notify_event', on_mouse_move)


        #theLayout.addWidget(sumOfForce)




        if self.layout.count() > 0:
            layout_item = self.layout.takeAt(1)
            if layout_item:
                layout_item.widget().deleteLater()
                

        layout.addWidget(damShape_shape)
        # self.graphWindowLayout.addWidget(sumOfForce , alignment=Qt.AlignCenter)


        # self.graphWindowLayout.addWidget(damShape_shape)
        

        # self.graphWindow.exec()

    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(theInput)
        error_dialog.exec_()

    def damMatrix(self):

        cols = 1 + int(self.length.text())*5
        rows = 1 + int(self.D2.text())
        dam = np.zeros((rows, cols))
        dam [0 , :1+int(self.length.text())*2] = float(self.Ht.text())
        dam [0 , 1+int(self.length.text())*2:1+int(self.length.text())*3] = 0
        dam [0 , 1+int(self.length.text())*3:] = float(self.Hb.text())
    

        for i in range (200):
            dam = self.meanCalc(dam)
        



        forceInPlace = self.calcHp(dam)
        
        self.result(forceInPlace , self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("""QLabel {
                        color :#146C94 ;
                    
                        }
                    """)
    ex = App()
    sys.exit(app.exec_())
