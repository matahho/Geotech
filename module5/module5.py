from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog , QErrorMessage , QToolButton
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor , QPixmap
from PyQt5.QtCore import Qt , QSize
import sys , math



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure






class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Module 5'
        self.setWindowTitle(self.title)
        
        self.table_widget = Module5(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
        self.showFullScreen()
        self.setFixedSize(self.size())
    
class Module5(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        self.tabs = QTabWidget()
        self.module5 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.module5,"Module 5")
        
        # Create first tab
        self.module5.layout = QVBoxLayout(self)
        self.addModule5HelpToLayout(self.module5.layout )
        self.input_datas(self.module5.layout)
        self.embedImage(self.module5.layout)
        

        self.ButtonLayout = QHBoxLayout()
        self.processButtonFunction(self.ButtonLayout)
        self.resetButtonFunction(self.ButtonLayout)
        self.module5.layout.addLayout(self.ButtonLayout)

    
        self.module5.setLayout(self.module5.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.pixmap = self.pixmap.scaled(600,600) 
        self.logo.setPixmap(self.pixmap)

        #self.logo.resize(self.pixmap.width(),self.pixmap.height())
        self.layout.addWidget(self.logo)

        
    # This part wat the loading inputs like : q (بازگذاری قائم)



    # def __loadingToLayouts (self , inputsLayout , i , j ):

    #     loadingBox = QGroupBox("Loading")
    #     loadingPart = QFormLayout()

    #     self.q = QLineEdit()
    #     self.q.setFixedWidth(50)
    #     self.q.setValidator(QDoubleValidator())
    #     self.q.textChanged.connect(self.enButton)
    #     self.q.setPlaceholderText("kN/m")
    #     qLabel = QLabel("q (kN/m) ")
    #     qLabel.setToolTip("بارگذاری قائم")
    #     loadingPart.addRow (qLabel , self.q)
    #     loadingBox.setLayout(loadingPart)
    #     inputsLayout.addWidget(loadingBox , i , j )

    def addModule5HelpToLayout(self , layout):
        self.module5Help = QToolButton()
        self.module5Help.setText("Help")  
        self.module5Help.setIconSize(QSize(20 , 20))
        layout.addWidget(self.module5Help ,alignment = Qt.AlignRight)
        self.module5Help.clicked.connect(self.module5HelpFunction)


    def module5HelpFunction(self):
        message_box = QMessageBox()

        message_box.setWindowTitle('Module 5 Help')
        about = "شما در حال استفاده از ماژول محاسبات دیوار حائل از نرم افزار GeOnion هستید."
        about2 = "سازه های عمودی پایداری خود را تا حد زیادی از وزن خود به دست می آورند. خرابی ناشی از واژگونی زمانی اتفاق می‌افتد که لنگر واژگونی ناشی از نیروها بیشتر از لنگر ناشی از وزن سازه باشد."
        about3 = " لغزش زمانی اتفاق می افتد که مقاومت اصطکاکی بین سازه و فونداسیون برای مقاومت در برابر نیروهای وارد شده کافی نباشد. ضریب اطمینان در برابر لغزش دیوار باید در شرایط معمولی 1.2 یا بیشترو در شرایط زلزله 1.0 یا بیشتر باشد."
        about4 = " ضریب اطمینان در برابر واژگونی دیوار باید در شرایط عادی 1.2 یا بیشتر و در شرایط زلزله 1.1 یا بیشتر باشد."

        message_box.setText(about + "\n\n    " + about2 + "\n\n    " + about3 + about4 + "\n\n")
        message_box.exec_()



    def __GeneralToLayouts (self , inputsLayout , i , j ):
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


        GeneralBox = QGroupBox("GENERAL")
        GeneralBox.setStyleSheet(boxesStyle)
        GeneralPart = QFormLayout()
        GeneralBox.setAlignment(Qt.AlignCenter)

        self.delta = QLineEdit()
        self.delta.setFixedWidth(80)
        self.delta.setValidator(QDoubleValidator())
        self.delta.textChanged.connect(self.enButton)
        self.delta.setPlaceholderText("degree")
        deltaLabel = QLabel (u"\u03B4 (degree) ")
        #deltaLabel.setToolTip ("")
        GeneralPart.addRow (deltaLabel , self.delta)


        self.micro = QLineEdit()
        self.micro.setFixedWidth(80)
        self.micro.setValidator(QDoubleValidator())
        self.micro.textChanged.connect(self.enButton)
        microLabel = QLabel(u"\u00B5 ")
        microLabel.setToolTip ("ضریب اصطکاک")
        GeneralPart.addRow (microLabel , self.micro)


        self.gammaConcrete = QLineEdit()
        self.gammaConcrete.setFixedWidth(80)
        self.gammaConcrete.setValidator(QDoubleValidator())
        self.gammaConcrete.textChanged.connect(self.enButton)
        self.gammaConcrete.setPlaceholderText("kN/m\N{SUPERSCRIPT THREE}")
        gammaConcreteLabel = QLabel(u"\u03B3 conc (kN/m\N{SUPERSCRIPT THREE}) ")
        gammaConcreteLabel.setToolTip ("وزن مخصوص بتن")
        GeneralPart.addRow (gammaConcreteLabel , self.gammaConcrete)


        self.gammaW = QLineEdit()
        self.gammaW.setFixedWidth(80)
        self.gammaW.setValidator(QDoubleValidator())
        self.gammaW.textChanged.connect(self.enButton)
        self.gammaW.setPlaceholderText("kN/m\N{SUPERSCRIPT THREE}")
        gammaWLabel = QLabel(u"\u03B3 w (kN/m\N{SUPERSCRIPT THREE}) ")
        gammaWLabel.setToolTip ("وزن مخصوص آب")
        GeneralPart.addRow (gammaWLabel , self.gammaW)


        self.MLLW = QLineEdit()
        self.MLLW.setFixedWidth(80)
        self.MLLW.setValidator(QDoubleValidator())
        self.MLLW.textChanged.connect(self.enButton)
        self.MLLW.setPlaceholderText("m")
        MLLWLabel = QLabel("MLLW (m) ")
        MLLWLabel.setToolTip("Mean Lower Low Water")
        GeneralPart.addRow (MLLWLabel , self.MLLW)


        self.q = QLineEdit()
        self.q.setFixedWidth(80)
        self.q.setValidator(QDoubleValidator())
        self.q.textChanged.connect(self.enButton)
        self.q.setPlaceholderText("kN/m")
        qLabel = QLabel("Loading (kN/m) ")
        qLabel.setToolTip("بارگذاری قائم")
        GeneralPart.addRow (qLabel , self.q)



        GeneralBox.setLayout(GeneralPart)
        #GeneralBox.setAlignment(Qt.AlignCenter)
        inputsLayout.addWidget(GeneralBox , i , j )

    # This was the palce for inputs of Water like : MHHW , MLLW , MSL


    # def __WATER (self , inputsLayout , i , j ):
        
    #     waterBox = QGroupBox("Water")
    #     waterPart = QFormLayout()



    #     self.MHHW = QLineEdit()
    #     self.MHHW.setFixedWidth(30)
    #     self.MHHW.setValidator(QDoubleValidator())
    #     self.MHHW.textChanged.connect(self.enButton)
    #     self.MHHW.setPlaceholderText("m")
    #     MHHWLabel = QLabel("MHHW (m) ")
    #     MHHWLabel.setToolTip("Mean Higher High Water")
    #     waterPart.addRow (MHHWLabel , self.MHHW)


    #     self.MLLW = QLineEdit()
    #     self.MLLW.setFixedWidth(30)
    #     self.MLLW.setValidator(QDoubleValidator())
    #     self.MLLW.textChanged.connect(self.enButton)
    #     self.MLLW.setPlaceholderText("m")
    #     MLLWLabel = QLabel("MLLW (m) ")
    #     MLLWLabel.setToolTip("Mean Lower Low Water")
    #     waterPart.addRow (MLLWLabel , self.MLLW)


    #     self.MSL = QLineEdit()
    #     self.MSL.setFixedWidth(30)
    #     self.MSL.setValidator(QDoubleValidator())
    #     self.MSL.textChanged.connect(self.enButton)
    #     self.MSL.setPlaceholderText("m")
    #     MSLLabel = QLabel("MSL (m) ")
    #     MSLLabel.setToolTip("Mean Sea Level")
    #     waterPart.addRow (MSLLabel , self.MSL)

    #     waterBox.setLayout(waterPart)
    #     inputsLayout.addWidget(waterBox , i , j )

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


        self.fi = QLineEdit()
        self.fi.setFixedWidth(80)
        self.fi.setValidator(QDoubleValidator())
        self.fi.textChanged.connect(self.enButton)
        self.fi.setPlaceholderText("degree")        
        fiLabel = QLabel(u"\u03C6 (degree) ")
        #fiLabel.setToolTip("")
        soilPart.addRow (fiLabel , self.fi)



        self.gammaWet = QLineEdit()
        self.gammaWet.setFixedWidth(80)
        self.gammaWet.setValidator(QDoubleValidator())
        self.gammaWet.textChanged.connect(self.enButton)
        self.gammaWet.setPlaceholderText("kN/m\N{SUPERSCRIPT THREE}")        
        gammaWetLabel = QLabel(u"\u03B3 wet (kN/m\N{SUPERSCRIPT THREE}) ")
        gammaWetLabel.setToolTip("وزن مخصوص خاک")
        soilPart.addRow (gammaWetLabel , self.gammaWet)



        self.gammaSat = QLineEdit()
        self.gammaSat.setFixedWidth(80)
        self.gammaSat.setValidator(QDoubleValidator())
        self.gammaSat.textChanged.connect(self.enButton)
        self.gammaSat.setPlaceholderText("kN/m\N{SUPERSCRIPT THREE}")        
        gammaSatLabel = QLabel(u"\u03B3 sat (kN/m\N{SUPERSCRIPT THREE}) ")
        gammaSatLabel.setToolTip("وزن مخصوص اشباع خاک")
        soilPart.addRow (gammaSatLabel , self.gammaSat)


        soilBox.setLayout(soilPart)
        inputsLayout.addWidget(soilBox , i , j )


    def __Geometry (self , inputsLayout , i , j ):
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


        GeometryBox = QGroupBox("GEOMETRY")
        GeometryBox.setStyleSheet(boxesStyle)
        GeometryPart = QFormLayout()
        GeometryBox.setAlignment(Qt.AlignCenter)

        self.Bt = QLineEdit()
        self.Bt.setFixedWidth(80)
        self.Bt.setValidator(QDoubleValidator())
        self.Bt.textChanged.connect(self.enButton)
        self.Bt.setPlaceholderText("m")
        BtLabel = QLabel("Bt (m) ")
        BtLabel.setToolTip("عرض بالای دیوار")
        GeometryPart.addRow (BtLabel , self.Bt)



        self.Bb = QLineEdit()
        self.Bb.setFixedWidth(80)
        self.Bb.setValidator(QDoubleValidator())
        self.Bb.textChanged.connect(self.enButton)
        self.Bb.setPlaceholderText("m")
        BbLabel = QLabel("Bb (m) ")
        BbLabel.setToolTip("عرض پایین دیوار")
        GeometryPart.addRow (BbLabel , self.Bb)

        self.Ht = QLineEdit()
        self.Ht.setFixedWidth(80)
        self.Ht.setValidator(QDoubleValidator())
        self.Ht.textChanged.connect(self.enButton)
        self.Ht.setPlaceholderText("m")
        HtLabel = QLabel("Ht (m) ")
        HtLabel.setToolTip("ارتفاع بالای دیوار")
        GeometryPart.addRow (HtLabel , self.Ht)

        
        self.Hw = QLineEdit()
        self.Hw.setFixedWidth(80)
        self.Hw.setValidator(QDoubleValidator())
        self.Hw.textChanged.connect(self.enButton)
        self.Hw.setPlaceholderText("m")
        HwLabel = QLabel("Hw (m) ")
        HwLabel.setToolTip("ارتفاع آب")
        GeometryPart.addRow (HwLabel , self.Hw)

        self.Hb = QLineEdit()
        self.Hb.setFixedWidth(80)
        self.Hb.setValidator(QDoubleValidator())
        self.Hb.textChanged.connect(self.enButton)
        self.Hb.setPlaceholderText("m")
        HbLabel = QLabel("Hb (m) ")
        HbLabel.setToolTip("ارتفاع پایین دیوار")
        GeometryPart.addRow (HbLabel , self.Hb)




        GeometryBox.setLayout(GeometryPart)
        inputsLayout.addWidget(GeometryBox , i , j )


   
   
    def input_datas (self,layout ):
        gridLayout = QGridLayout()
        # self.__loadingToLayouts(gridLayout , 1 , 0)
        self.__GeneralToLayouts(gridLayout , 0 , 0)
        self.__SoilCharacteristic(gridLayout , 0 , 1)
        self.__Geometry(gridLayout , 0 , 2)
        #self.__WATER (gridLayout , 1 , 2 )


        layout.addLayout(gridLayout)
    

    def embedImage (self , inputsLayout):
        gridLayout = QVBoxLayout()
        imageLabel = QLabel()
        pixmap = QPixmap('module5.png')
        imageLabel.setPixmap(pixmap)
        
        gridLayout.addWidget(imageLabel )



        inputsLayout.addLayout(gridLayout)
    



    def Ka (self):
        try:
            return ( (1 - math.sin(math.radians(float(self.fi.text())))) / (1 + math.sin(math.radians(float(self.fi.text()))) ) )
        except:
            raise Exception("fi")

    def omega (self):
        try:
            top = float(self.Bb.text()) - float(self.Bt.text())
            down = float(self.Ht.text()) - float(self.Hb.text())
            return math.degrees(math.atan((top/down)))
        except:
            raise Exception("Ht-Hb")

    def BOmega (self):
        omg = self.omega()
        return (float(self.Bt.text()) + (float(self.Ht.text()) - float(self.Hw.text())) * math.tan(math.radians(omg)))

    ##### ACTIVE EARTH PRESSURE ==> AEP #####

    def P1_AEP (self):
        if float(self.Ht.text()) <= float(self.Hb.text()):
            raise Exception("Ht-Hb")
        return 0
    
    def P2_AEP (self):
        k = self.Ka()
        return max(0, k * float(self.gammaWet.text()) * (float(self.Ht.text()) - float(self.Hw.text())))

    def P3_AEP (self):
        k = self.Ka()
        return max(0, k * float(self.gammaWet.text()) * (float(self.Ht.text()) - float(self.Hw.text())))

    def P4_AEP (self):
        k = self.Ka()
        return (max(0, k * float(self.gammaWet.text()) * (float(self.Ht.text()) - float(self.Hw.text()))) + max( 0 , k * (float(self.gammaSat.text()) - float (self.gammaW.text())) * (float(self.Hw.text()) - float(self.Hb.text()))))


    def FaboveWater_AEP (self):
        p1 = self.P1_AEP()
        p2 = self.P2_AEP()
        return (max(0 , 0.5 * (p1+p2) *(float(self.Ht.text()) - float(self.Hw.text()))))

    def FunderWater_AEP(self):
        p3 = self.P3_AEP()
        p4 = self.P4_AEP()
        return (max(0 , 0.5 * (p4+p3) *(float(self.Hw.text()) - float(self.Hb.text()))))
    
    def FhaboveWater_AEP(self):
        return self.FaboveWater_AEP() * math.cos(math.radians(self.omega() + float(self.delta.text())))
    
    def FhunderWater_AEP(self):
        return self.FunderWater_AEP() * math.cos(math.radians(self.omega() + float(self.delta.text())))

    def FvaboveWater_AEP (self):
        return self.FaboveWater_AEP() * math.sin(math.radians(self.omega() + float(self.delta.text())))
    
    def FvunderWater_AEP (self):
        return self.FunderWater_AEP() * math.sin(math.radians(self.omega() + float(self.delta.text())))
    
    def yaboveWater_AEP (self):
        a = float(self.Ht.text()) - float(self.Hb.text()) 
        b = float(self.Ht.text()) - float(self.Hw.text()) 
        return a - (2/3 * b)
    
    def yunderWater_AEP (self):
        try:
            return (2*self.P3_AEP()+self.P4_AEP()) * ((float(self.Hw.text()) - float(self.Hb.text())) / (3*(self.P3_AEP()+self.P4_AEP())))
        except:
            raise Exception ("P3+P4")

    def xaboveWater_AEP(self):
        return float(self.Bb.text()) - self.yaboveWater_AEP() * math.tan(math.radians(self.omega()))

    def xunderWater_AEP(self):
        return float(self.Bb.text()) - self.yunderWater_AEP() * math.tan(math.radians(self.omega()))

    ### ACTIVE q ==> Aq ###

    def P1_Aq (self):
        return (float(self.q.text()) * self.Ka())

    def P2_Aq (self):
        return (float(self.q.text()) * self.Ka())
    
    def P3_Aq (self):
        return (float(self.q.text()) * self.Ka())
    
    def P4_Aq (self):
        return (float(self.q.text()) * self.Ka())


    # This function will calculate the F above Water of part ACTIVE q 
    # The Formoula for it : maximum between 1. (1/2 * (P1 + P2) * (Ht - Hw) and 2. (0) 
    def FaboveWater_Aq (self):
        return max(0.5 * (self.P1_Aq() + self.P2_Aq()) * (float(self.Ht.text()) - float(self.Hw.text())) , 0 )

    # This function will calculate the F under Water of part ACTIVE q 
    # The Formoula for it : maximum between 1. (1/2 * (P3 + P4) * (Hw - Hb) and 2. (0) 
    def FunderWater_Aq (self):
        return max(0.5 * (float(self.P3_Aq()) + float(self.P4_Aq()))* (float(self.Hw.text()) - float(self.Hb.text())) , 0)
    
    # This function will calculate the Fh above Water of part ACTIVE q 
    # The Formoula for it : F above water of part ACTIVE q * (cos(Omega) + delta) 
    def FhaboveWater_Aq (self):
        return self.FaboveWater_Aq() * math.cos(math.radians(self.omega() + float(self.delta.text())))

    # This function will calculate the Fh under Water of part ACTIVE q 
    # The Formoula for it : F under water of part ACTIVE q * (cos(Omega) + delta) 
    def FhunderWater_Aq (self):
        return self.FunderWater_Aq() * math.cos(math.radians(self.omega() + float(self.delta.text())))
    

    # This function will calculate the Fv above Water of part ACTIVE q 
    # The Formoula for it : F above water of part ACTIVE q * (sin(Omega) + delta) 
    def FvaboveWater_Aq (self):
        return self.FaboveWater_Aq() * math.sin(math.radians(self.omega() + float(self.delta.text())))

    # This function will calculate the Fv under Water of part ACTIVE q 
    # The Formoula for it : F under water of part ACTIVE q * (sin(Omega) + delta) 
    def FvunderWater_Aq (self):
        return self.FunderWater_Aq() * math.sin(math.radians(self.omega() + float(self.delta.text())))


    # This function will calculate the y above Water of part ACTIVE q 
    # The Formoula for it : (Ht - Hb) - 1/2 * (Ht - Hw)
    def yaboveWater_Aq (self):
        a = float(self.Ht.text()) - float(self.Hb.text()) 
        b = float(self.Ht.text()) - float(self.Hw.text()) 
        return a - (0.5 * b)

    # This function will calculate the y under Water of part ACTIVE q 
    # The Formoula for it : 1/2 * (Hw - Hb)
    def yunderWater_Aq (self):
        return 0.5 * (float(self.Hw.text()) - float(self.Hb.text()))

    # This function will calculate the x above Water of part ACTIVE q 
    # The Formoula for it : (Bb - y above Water of part ACTIVE q) * tan(Omega)
    def xaboveWater_Aq(self):
        return float(self.Bb.text()) - self.yaboveWater_Aq() * math.tan(math.radians(self.omega()))
    
    # This function will calculate the x under Water of part ACTIVE q 
    # The Formoula for it : (Bb - y under Water of part ACTIVE q) * tan(Omega)
    def xunderWater_Aq(self):
        return float(self.Bb.text()) - self.yunderWater_Aq() * math.tan(math.radians(self.omega()))


    # This part is the calculation for part WATER PRESSURE 
    ### HINT : WATER PRESSURE ==> wp ###

    # This function will calculate the P1 of part WATER PRESSURE 
    # The Formoula for it : P1 in this section is always 0 
    def P1_wp (self):
        return 0 
    
    # This function will calculate the P2 of part WATER PRESSURE 
    # The Formoula for it : minimun between 1. (gamma W * (Hw - Hb)) and 2. (gamma W * (Hw - MLLW))  
    def P2_wp (self):
        return min( float (self.gammaW.text()) * (float(self.Hw.text()) - float (self.Hb.text()))  ,  float (self.gammaW.text()) * (float(self.Hw.text()) - float (self.MLLW.text())) )

    # This function will calculate the P3 of part WATER PRESSURE 
    # The Formoula for it : minimun between 1. (gamma W * (Hw - Hb)) and 2. (gamma W * (Hw - MLLW))  
    def P3_wp (self):
        return min ( float (self.gammaW.text()) * (float(self.Hw.text()) - float (self.Hb.text())) ,  float (self.gammaW.text()) * (float(self.Hw.text()) - float (self.MLLW.text())))

    # This function will calculate the Fh of part WATER PRESSURE 
    # The Formoula for it : Hb >= MLLW ? 1/2 * P1+P2 * Hw-Hb : 1/2 * P1+P2 * Hw-MLLW + P2 * MLLW-Hb
    def Fh_wp (self):   
        if float (self.Hb.text()) >= float (self.MLLW.text()) :
            return 0.5 * (self.P1_wp() + self.P2_wp()) * (float(self.Hw.text()) - float (self.Hb.text()))
        else :
            return 0.5 * (self.P1_wp() + self.P2_wp()) * (float(self.Hw.text()) - float (self.MLLW.text())) + self.P2_wp() * (float(self.MLLW.text()) - float (self.Hb.text()))


    def yWater_wp (self):
        try:
            if float (self.Hb.text()) >= float (self.MLLW.text()) :

                return 1/3 * (float(self.Hw.text()) - float (self.Hb.text()))
            else :
                a = 0.5 * self.P2_wp() * math.pow((float (self.MLLW.text()) - float (self.Hb.text())) , 2)
                b = 0.5 * (self.P1_wp() + self.P2_wp()) * (float(self.Hw.text()) - float (self.MLLW.text())) + self.P2_wp() * (float (self.MLLW.text()) - float (self.Hb.text()))
                return ((1/2 * (self.P1_wp() + self.P2_wp()) * (float (self.Hw.text()) - float (self.MLLW.text())) * (float(self.MLLW.text()) - float (self.Hb.text()) + 1/3*(float(self.Hw.text()) - float (self.MLLW.text()))) +a)/b)
        except:
            raise Exception("yWater waterPressure")

    ##### PASSIVE --> P #####

    def AaboveWater_p (self):
        return 0.5 * (float(self.Ht.text()) - float (self.Hw.text())) * (float (self.Bt.text()) + self.BOmega())

    def AunderWater_p (self):
        return 0.5 * (float (self.Hw.text()) - float(self.Hb.text())) * (self.BOmega() + float (self.Bb.text()))

    def WaboveWater_p (self):
        return self.AaboveWater_p() * float(self.gammaConcrete.text())
    
    def WunderWater_p (self):
        return self.AunderWater_p() * ( float(self.gammaConcrete.text()) - float(self.gammaW.text()))

    def xaboveWater_p (self):
        try:
            top = (float(self.Bt.text()) ** 2) + (self.BOmega() - float(self.Bt.text()))*(float(self.Bt.text()) + (self.BOmega() - float(self.Bt.text()))/3)
            down = self.BOmega() + float(self.Bt.text())
            return (top / down)
        except:
            raise Exception("xAboveWater Passive")
    def xunderWater_p (self):
        try:
            top = (self.BOmega() ** 2) + ((float(self.Bb.text()) - self.BOmega()) * (self.BOmega() + 1/3*(float(self.Bb.text())-self.BOmega())))
            down = self.BOmega() + float(self.Bb.text())
            return ( top / down )
        except:
            raise Exception("xAboveWater Passive")



    ### OVERTURNING ###
    def Mo (self):
        aep = self.FhaboveWater_AEP() * self.yaboveWater_AEP() + self.FhunderWater_AEP() * self.yunderWater_AEP()
        aq = self.FhaboveWater_Aq() * self.yaboveWater_Aq() + self.FhunderWater_Aq() * self.yunderWater_Aq()
        wp = self.Fh_wp() * self.yWater_wp()
        return (aep + aq + wp)


    def MR (self):
        aep = self.FvaboveWater_AEP() * self.xaboveWater_AEP() + self.FvunderWater_AEP() * self.xunderWater_AEP()
        passive = self.WaboveWater_p() * self.xaboveWater_p() + self.WunderWater_p() * self.xunderWater_p()
        return aep + passive
    
    def FOS_overturning (self):
        try:
            return self.MR()/self.Mo()
        except:
            raise Exception("Mo")
    ### SLIDING ###
    def Fo (self):
        aep = self.FhaboveWater_AEP() + self.FhunderWater_AEP()
        aq = self.FhaboveWater_Aq() + self.FhunderWater_Aq()
        wp = self.Fh_wp()
        return aep + aq + wp 

    def Fr (self):
        mm = float(self.micro.text())
        aep = self.FvaboveWater_AEP() + self.FvunderWater_AEP() 
        passive = self.WaboveWater_p() + self.WunderWater_p()
        return (mm * (aep + passive))

    def FOS_sliding (self):
        try:
            return (self.Fr() / self.Fo())
        except:
            raise Exception("Fo")

    ### OVERTURNING WITH qv ###
    def Mo_with_qv (self):
        aep = float(self.FhaboveWater_AEP()*self.yaboveWater_AEP() + self.FhunderWater_AEP() * self.yunderWater_AEP() )
        aq = float(self.FhaboveWater_Aq() * self.yaboveWater_Aq() + self.FhunderWater_Aq() * self.yunderWater_Aq())
        wp = float(self.Fh_wp() * self.yWater_wp())
        return aep + aq + wp 
    
    def MR_with_qv (self):
        aep = self.FvaboveWater_AEP() * self.xaboveWater_AEP() + self.FvunderWater_AEP() * self.xunderWater_AEP()
        aq = self.FvaboveWater_Aq() * self.xaboveWater_Aq() + self.FvunderWater_Aq() * self.xunderWater_Aq()
        passive = self.WaboveWater_p() * self.xaboveWater_p() + self.WunderWater_p() * self.xunderWater_p()
        return aep + aq + passive

    def FOS_overturning_with_qv (self):
        try:
            return self.MR_with_qv() / self.Mo_with_qv ()
        except:
            raise Exception("Mo with qv")

    def Fo_with_qv (self):
        aep = self.FhaboveWater_AEP() + self.FhunderWater_AEP() 
        aq = self.FhaboveWater_Aq() + self.FhunderWater_Aq()
        wp = self.Fh_wp()
        return aep + aq + wp 

    def Fr_with_qv (self):
        mm = float(self.micro.text())
        aep = self.FvaboveWater_AEP() + self.FvunderWater_AEP()
        aq = self.FvaboveWater_Aq() + self.FvunderWater_Aq()
        passive = self.WaboveWater_p() + self.WunderWater_p()
        return mm*(aep + aq + passive)
    
    def FOS_sliding_with_qv(self):
        try:
            return self.Fr_with_qv() / self.Fo_with_qv()
        except:
            raise Exception("Fo with qv")





    def processButtonFunction (self , layout):
        self.processButton = QPushButton ("Calculate" , self)
        self.processButton.setEnabled(False) 
        self.processButton.clicked.connect(self.process)
        layout.addWidget(self.processButton , alignment = Qt.AlignLeft)

    

    def resetButtonFunction (self , layout):
        self.resetButton = QPushButton ("Reset" , self)

        self.resetButton.clicked.connect(self.resetAll)
        layout.addWidget(self.resetButton , alignment = Qt.AlignRight)

    def resetAll(self):
        theInputs = [self.delta , self.micro , self.gammaConcrete , self.gammaW , self.MLLW , self.q , self.fi , self.gammaWet , self.gammaSat , self.Bt , self.Bb , self.Ht , self.Hw , self.Hb]

        for inp in theInputs:
            inp.clear()

        self.processButton.setEnabled(False)



    def enButton(self):
        if (self.delta.text() == '' or self.micro.text() == '' or self.gammaConcrete.text() == '' or self.gammaW.text() == '' or self.q.text() == '' or self.fi.text() == '' or self.gammaWet.text() == '' or self.gammaSat.text() == '' or self.Bt.text() == '' or self.Bb.text() == '' or self.Ht.text() == '' or self.Hw.text() == '' or self.Hb.text() == '' or self.MLLW.text() == ''):
            self.processButton.setEnabled(False)
        else :
            self.processButton.setEnabled(True)

    def process(self):

        layout = QGridLayout()

        table1 = QTableWidget()
        table2 = QTableWidget()

        # Set the number of rows and columns in the table
        num_rows = 3
        num_cols = 2
        table1.setRowCount(num_rows)
        table1.setColumnCount(num_cols)
        table1.setFixedWidth(num_cols * 117)
        table1.setFixedHeight(num_rows * 38)


        # Set the table headers
        table1.setHorizontalHeaderLabels(['Without qv', 'With qv'])
        table1.setVerticalHeaderLabels(['Mo', 'MR' , 'FOS'])
        
        # Populate the table with data
        try:
            data1 = [["{:.2f}".format(self.Mo()), "{:.2f}".format(self.Mo_with_qv())],
                    ["{:.2f}".format(self.MR()), "{:.2f}".format(self.MR_with_qv())],
                    ["{:.2f}".format(self.FOS_overturning()), "{:.2f}".format(self.FOS_overturning_with_qv())]]
 

            for i, row in enumerate(data1):
                for j, text in enumerate(row):
                    item = QTableWidgetItem(text)
                    table1.setItem(i, j, item)

            if float(table1.item(2,0).text()) < 1 :
                table1.item(2, 0).setBackground(QColor(208 , 54 ,3 ))
            else :
                table1.item(2, 0).setBackground(QColor(58 , 175 ,9 ))

            if float(table1.item(2,1).text()) < 1 :
                table1.item(2, 1).setBackground(QColor(208 , 54 ,3 ))
            else :
                table1.item(2, 1).setBackground(QColor(58 , 175 ,9 ))

            table2.setRowCount(num_rows)
            table2.setColumnCount(num_cols)
            table2.setFixedWidth(num_cols * 117)
            table2.setFixedHeight(num_rows * 38)



            # Set the table headers
            table2.setHorizontalHeaderLabels(['Without qv', 'With qv'])
            table2.setVerticalHeaderLabels(['Fo', 'Fr' , 'FOS'])
    



    # Populate the table with data

            data2 = [["{:.2f}".format(self.Fo()), "{:.2f}".format(self.Fo_with_qv())],
                    ["{:.2f}".format(self.Fr()), "{:.2f}".format(self.Fr_with_qv())],
                    ["{:.2f}".format(self.FOS_sliding()), "{:.2f}".format(self.FOS_sliding_with_qv())]]


            for i, row in enumerate(data2):
                for j, text in enumerate(row):
                    item = QTableWidgetItem(text)
                    table2.setItem(i, j, item)

            if float(table2.item(2,0).text()) < 1 :
                table2.item(2,0).setBackground(QColor(208 , 54 ,3 ))
            else :
                table2.item(2,0).setBackground(QColor(58 , 175 ,9 ))

            if float(table2.item(2,1).text()) < 1 :
                table2.item(2,1).setBackground(QColor(208 , 54 ,3 ))
            else :
                table2.item(2,1).setBackground(QColor(58 , 175 ,9 ))


            layout.addWidget(table1, 0 ,0)
            layout.addWidget(table2, 1 ,0)


            if self.layout.count() > 0:
                layout_item = self.layout.takeAt(1)
                if layout_item:
                    layout_item.widget().deleteLater()
                    

            self.layout.addLayout(layout)



        except Exception as e:
            self.inputError(str(e))      


    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
        error_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("""QLabel {
                        color :#146C94 ;
                    
                        }
                    """)
    ex = App()
    sys.exit(app.exec_())
