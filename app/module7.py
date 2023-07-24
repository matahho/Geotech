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








class Module7(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        self.layout = QHBoxLayout(self)

        self.module7 = QWidget()
        

        
        # Create first tab
        self.module7.layout = QVBoxLayout(self)
        self.addModule7HelpToLayout(self.module7.layout )
        self.input_datas(self.module7.layout)
        
        

        self.ButtonLayout = QHBoxLayout()
        self.processButtonFunction(self.ButtonLayout)
        self.resetButtonFunction(self.ButtonLayout)
        self.module7.layout.addLayout(self.ButtonLayout)

    
        self.layout.addWidget(self.module7)
        self.module7.setLayout(self.module7.layout)
        
        # Add tabs to widget

        self.setLayout(self.layout)
        
        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.pixmap = self.pixmap.scaled(600,600) 
        self.logo.setPixmap(self.pixmap)

        #self.logo.resize(self.pixmap.width(),self.pixmap.height())
        self.layout.addWidget(self.logo)

    def addModule7HelpToLayout(self , layout):
        self.module7Help = QToolButton()
        self.module7Help.setText("Help")  
        self.module7Help.setIconSize(QSize(20 , 20))
        layout.addWidget(self.module7Help ,alignment = Qt.AlignRight)
        self.module7Help.clicked.connect(self.module7HelpFunction)

    def module7HelpFunction(self):
        message_box = QMessageBox()

        message_box.setWindowTitle('Module 7 Help')
        about ="شما در حال استفاده از ماژول توزیع تنش از نرم افزار GeOnion هستید."
        about2 = "با قرار گرفتن سربار بر روی خاک به مقدار تنش موجود در خاک افزوده می شود و هرچه در جهت افقی و قائم از محل اثر بار فاصله بگیریم، مشاهده می شود که از تاثیر سربار کاسته خواهد شد."
        about3 = "اثر سربار در حالت های مختلفی نظیر بار نقطه ای، بار خطی، بار نواری، بار گسترده، بر روی سطح دایره ای و بار گسترده بر روی سطح مستطیلی را می توان با استفاده از تئوری الاستیسیته مشخص نمود."
        about4 = "بوسینسک برای محاسبه تنش در توده خاک، فرضیات زیر را در نظر گرفت:"
        about5 = "۱.خاک بدون وزن است"
        about6 = "۲.تغییر حجم خاک قابل اغماض است"
        about7 = "۳.قبل از اعمال سربار، خاک تحت تنش دیگری قرار نداشته است"
        about8 = "۴.خاک الاستیک، همگن، نیمه بینهایت و ایزوتروپیک بوده و تابع قانون هوک می باشد"
        about9 = "۵.توزیع تنش نسبت به محور قائم تقارن دارد"
        about10 = "۶.تنش ممتد و پیوسته است"
        txt = (about + "\n\n    " + about2 + "\n\n    " + about3 + "\n\n    " + about4 + "\n            " +about5+ "\n            " +about6+ "\n            " +about7+ "\n            " +about8+ "\n            " +about9+ "\n            " +about10)
        message_box.setText(txt)
        message_box.exec_()

    def choosingLoadType(self , s):
        if (s == "Point Load"):
            self.LoadType_string = "Point Load"
            self.PointLoadBox.setEnabled(True)
            self.LineLoadBox.setEnabled(False)
            self.StripLoadBox.setEnabled(False)
            self.UniformLoadBox.setEnabled(False)


        elif (s == "Line Load"):
            self.LoadType_string = "Line Load"
            self.PointLoadBox.setEnabled(False)
            self.LineLoadBox.setEnabled(True)
            self.StripLoadBox.setEnabled(False)
            self.UniformLoadBox.setEnabled(False)


        elif (s == "Strip Load"):
            self.LoadType_string = "Strip Load"
            self.PointLoadBox.setEnabled(False)
            self.LineLoadBox.setEnabled(False)
            self.StripLoadBox.setEnabled(True)
            self.UniformLoadBox.setEnabled(False)



        elif (s == "Uniform Load"):
            self.LoadType_string = "Uniform Load"
            self.PointLoadBox.setEnabled(False)
            self.LineLoadBox.setEnabled(False)
            self.StripLoadBox.setEnabled(False)
            self.UniformLoadBox.setEnabled(True)

        
        
    def __GeneralAndChart (self , inputsLayout , i , j ):

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


        self.GeneralBox = QGroupBox("GENERAL + CHART")
        self.GeneralBox.setStyleSheet(boxesStyle)
        GeneralPart = QFormLayout()
        self.GeneralBox.setAlignment(Qt.AlignCenter)


        ### load type part 
        self.LoadType = QComboBox()
        self.LoadType.addItems(["Point Load", "Line Load" , "Strip Load" , "Uniform Load"])
        self.LoadType.currentTextChanged.connect(self.choosingLoadType)
        self.LoadType_string = "Point Load"
        LoadTypeLabel = QLabel (u"Load type")
        LoadTypeLabel.setToolTip ("نوع بارگذاری")
        GeneralPart.addRow (LoadTypeLabel , self.LoadType)

        # max Expexted Depth part
        self.maxExpextedDepth = QLineEdit()
        self.maxExpextedDepth.setFixedWidth(80)
        self.maxExpextedDepth.setValidator(QDoubleValidator())
        self.maxExpextedDepth.textChanged.connect(self.enButton)
        self.maxExpextedDepth.setPlaceholderText("m")        
        maxExpextedDepthLabel = QLabel("Max Expected Depth (m) ")
        maxExpextedDepthLabel.setToolTip("آخرین عمق موردنظر برای تحلیل")
        GeneralPart.addRow (maxExpextedDepthLabel , self.maxExpextedDepth)

        # Depth inc
        self.depthIncrement = QComboBox ()
        self.depthIncrement.addItems(["0.25 m" , "0.5 m" , "1.0 m"])
        self.depthIncrement.currentTextChanged.connect (self.depthIncrement_calculator)
        self.depthIncrement_string = 0.25
        depthIncrementLabel = QLabel (u"Depth Increament (m) ")
        depthIncrementLabel.setToolTip ("گام های تغییر عمق")
        GeneralPart.addRow (depthIncrementLabel , self.depthIncrement)



        self.GeneralBox.setLayout(GeneralPart)
        inputsLayout.addWidget(self.GeneralBox , i , j )

    def depthIncrement_calculator(self, s ):
        if s == "0.25 m":
            self.depthIncrement_string = 0.25
        if s == "0.5 m":
            self.depthIncrement_string = 0.5
        if s == "1.0 m":
            self.depthIncrement_string = 1.0



    def __PointLoad (self , inputsLayout , i , j):

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


        self.PointLoadBox = QGroupBox("POINT LOAD")
        self.PointLoadBox.setStyleSheet(boxesStyle)
        self.PointLoadBox.setAlignment(Qt.AlignCenter)
        PointLoadPart = QFormLayout()


        self.q_pointLoad = QLineEdit()
        self.q_pointLoad.setFixedWidth(80)
        self.q_pointLoad.setValidator(QDoubleValidator())
        self.q_pointLoad.textChanged.connect(self.enButton)
        self.q_pointLoad.setPlaceholderText("ton")        
        q_pointLoadLabel = QLabel("q (ton) ")
        q_pointLoadLabel.setToolTip("مقدار بار")
        PointLoadPart.addRow (q_pointLoadLabel , self.q_pointLoad)







        self.x_pointLoad = QLineEdit()
        self.x_pointLoad.setFixedWidth(80)
        self.x_pointLoad.setValidator(QDoubleValidator())
        self.x_pointLoad.textChanged.connect(self.enButton)
        self.x_pointLoad.setPlaceholderText("m")        
        x_pointLoadLabel = QLabel("x (m) ")
        x_pointLoadLabel.setToolTip("")
        PointLoadPart.addRow (x_pointLoadLabel , self.x_pointLoad)





        self.y_pointLoad = QLineEdit()
        self.y_pointLoad.setFixedWidth(80)
        self.y_pointLoad.setValidator(QDoubleValidator())
        self.y_pointLoad.textChanged.connect(self.enButton)
        self.y_pointLoad.setPlaceholderText("m")        
        y_pointLoadLabel = QLabel("y (m)")
        y_pointLoadLabel.setToolTip("ضریب نفوذپذیری لایه اول خاک")
        PointLoadPart.addRow (y_pointLoadLabel , self.y_pointLoad)



        self.PointLoadBox.setLayout(PointLoadPart)
        inputsLayout.addWidget(self.PointLoadBox , i , j )




    def __LineLoad (self , inputsLayout , i , j):

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


        self.LineLoadBox = QGroupBox("LINE LOAD")
        self.LineLoadBox.setStyleSheet(boxesStyle)
        self.LineLoadBox.setAlignment(Qt.AlignCenter)
        LineLoadPart = QFormLayout()





        self.direction_lineLoad = QComboBox()
        self.direction_lineLoad.addItems(["Vertical", "Horizontal"])
        self.direction_lineLoad.currentTextChanged.connect(self.choosingDirection_lineLoad)
        self.direction_lineLoad_string = "Vertical"
        direction_lineLoadLabel = QLabel (u"Direction")
        direction_lineLoadLabel.setToolTip ("جهت بارگذاری")
        LineLoadPart.addRow (direction_lineLoadLabel , self.direction_lineLoad)



        self.q_lineLoad = QLineEdit()
        self.q_lineLoad.setFixedWidth(80)
        self.q_lineLoad.setValidator(QDoubleValidator())
        self.q_lineLoad.textChanged.connect(self.enButton)
        self.q_lineLoad.setPlaceholderText("ton/m")        
        q_lineLoadLabel = QLabel("q (ton/m) ")
        q_lineLoadLabel.setToolTip("مقدار بار")
        LineLoadPart.addRow (q_lineLoadLabel , self.q_lineLoad)







        self.x_lineLoad = QLineEdit()
        self.x_lineLoad.setFixedWidth(80)
        self.x_lineLoad.setValidator(QDoubleValidator())
        self.x_lineLoad.textChanged.connect(self.enButton)
        self.x_lineLoad.setPlaceholderText("m")        
        x_lineLoadLabel = QLabel("x (m) ")
        x_lineLoadLabel.setToolTip("")
        LineLoadPart.addRow (x_lineLoadLabel , self.x_lineLoad)







        self.LineLoadBox.setLayout(LineLoadPart)
        inputsLayout.addWidget(self.LineLoadBox , i , j )
    
    def __StripLoad (self , inputsLayout , i , j):

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


        self.StripLoadBox = QGroupBox("STRIP LOAD")
        self.StripLoadBox.setStyleSheet(boxesStyle)
        self.StripLoadBox.setAlignment(Qt.AlignCenter)
        StripLoadPart = QFormLayout()





        self.direction_stripLoad = QComboBox()
        self.direction_stripLoad.addItems(["Vertical", "Horizontal"])
        self.direction_stripLoad.currentTextChanged.connect(self.choosingDirection_stripLoad)
        self.direction_stripLoad_string = "Vertical"
        direction_stripLoadLabel = QLabel (u"Direction")
        direction_stripLoadLabel.setToolTip ("جهت بارگذاری")
        StripLoadPart.addRow (direction_stripLoadLabel , self.direction_stripLoad)



        self.q_stripLoad = QLineEdit()
        self.q_stripLoad.setFixedWidth(80)
        self.q_stripLoad.setValidator(QDoubleValidator())
        self.q_stripLoad.textChanged.connect(self.enButton)
        self.q_stripLoad.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")        
        q_stripLoadLabel = QLabel("q (ton/m\N{SUPERSCRIPT TWO}) ")
        q_stripLoadLabel.setToolTip("مقدار بار")
        StripLoadPart.addRow (q_stripLoadLabel , self.q_stripLoad)




        self.B_stripLoad = QLineEdit()
        self.B_stripLoad.setFixedWidth(80)
        self.B_stripLoad.setValidator(QDoubleValidator())
        self.B_stripLoad.textChanged.connect(self.enButton)
        self.B_stripLoad.setPlaceholderText("m")        
        B_stripLoadLabel = QLabel("B (m) ")
        B_stripLoadLabel.setToolTip("عرض بار نواری")
        StripLoadPart.addRow (B_stripLoadLabel , self.B_stripLoad)






        self.x_stripLoad = QLineEdit()
        self.x_stripLoad.setFixedWidth(80)
        self.x_stripLoad.setValidator(QDoubleValidator())
        self.x_stripLoad.textChanged.connect(self.enButton)
        self.x_stripLoad.setPlaceholderText("m")        
        x_stripLoadLabel = QLabel("x (m) ")
        x_stripLoadLabel.setToolTip("")
        StripLoadPart.addRow (x_stripLoadLabel , self.x_stripLoad)







        self.StripLoadBox.setLayout(StripLoadPart)
        inputsLayout.addWidget(self.StripLoadBox , i , j )



    def __UniformLoad (self , inputsLayout , i , j):

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


        self.UniformLoadBox = QGroupBox("UNIFORM LOAD")
        self.UniformLoadBox.setStyleSheet(boxesStyle)
        self.UniformLoadBox.setAlignment(Qt.AlignCenter)
        UniformLoadPart = QFormLayout()





        self.AreaType = QComboBox()
        self.AreaType.addItems(["Circular", "Rectangular"])
        self.AreaType.currentTextChanged.connect(self.choosingAreaType)
        self.AreaType_string = "Circular"
        AreaTypeLabel = QLabel (u"Area Type")
        AreaTypeLabel.setToolTip ("سطح بارگذاری")
        UniformLoadPart.addRow (AreaTypeLabel , self.AreaType)




        self.q_uniformLoad = QLineEdit()
        self.q_uniformLoad.setFixedWidth(80)
        self.q_uniformLoad.setValidator(QDoubleValidator())
        self.q_uniformLoad.textChanged.connect(self.enButton)
        self.q_uniformLoad.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")        
        q_uniformLoadLabel = QLabel("q (ton/m\N{SUPERSCRIPT TWO}) ")
        q_uniformLoadLabel.setToolTip("مقدار بار")
        UniformLoadPart.addRow (q_uniformLoadLabel , self.q_uniformLoad)


        self.R_uniformLoad = QLineEdit()
        self.R_uniformLoad.setFixedWidth(80)
        self.R_uniformLoad.setValidator(QDoubleValidator())
        self.R_uniformLoad.textChanged.connect(self.enButton)
        self.R_uniformLoad.setPlaceholderText("m")        
        R_uniformLoadLabel = QLabel("R (m) ")
        R_uniformLoadLabel.setToolTip("شعاع بارگذاری دایروی")
        UniformLoadPart.addRow (R_uniformLoadLabel , self.R_uniformLoad)


        self.L_uniformLoad = QLineEdit()
        self.L_uniformLoad.setFixedWidth(80)
        self.L_uniformLoad.setValidator(QDoubleValidator())
        self.L_uniformLoad.textChanged.connect(self.enButton)
        self.L_uniformLoad.setPlaceholderText("m")        
        L_uniformLoadLabel = QLabel("L (m) ")
        L_uniformLoadLabel.setToolTip("طول بارگذاری مستطیل")
        UniformLoadPart.addRow (L_uniformLoadLabel , self.L_uniformLoad)



        self.B_uniformLoad = QLineEdit()
        self.B_uniformLoad.setFixedWidth(80)
        self.B_uniformLoad.setValidator(QDoubleValidator())
        self.B_uniformLoad.textChanged.connect(self.enButton)
        self.B_uniformLoad.setPlaceholderText("m")        
        B_uniformLoadLabel = QLabel("B (m) ")
        B_uniformLoadLabel.setToolTip("عرض بارگذاری مستطیل")
        UniformLoadPart.addRow (B_uniformLoadLabel , self.B_uniformLoad)


        self.B_uniformLoad.setEnabled(False)
        self.L_uniformLoad.setEnabled(False)
        self.R_uniformLoad.setEnabled(True)

        self.UniformLoadBox.setLayout(UniformLoadPart)
        inputsLayout.addWidget(self.UniformLoadBox , i , j )


    def choosingAreaType(self , s):
        if s == "Circular":
            self.AreaType_string = "Circular"
            self.B_uniformLoad.setEnabled(False)
            self.L_uniformLoad.setEnabled(False)
            self.R_uniformLoad.setEnabled(True)
        if s == "Rectangular":
            self.AreaType_string = "Rectangular"
            self.B_uniformLoad.setEnabled(True)
            self.L_uniformLoad.setEnabled(True)
            self.R_uniformLoad.setEnabled(False)
            
        
    def choosingDirection_lineLoad(self, s ):

        if s == "Vertical":
            self.direction_lineLoad_string = "Vertical"
        else :
            self.direction_lineLoad_string = "Horizontal"


    def choosingDirection_stripLoad(self , s ):
        if s == "Vertical":
            self.direction_stripLoad_string = "Vertical"
        else :
            self.direction_stripLoad_string = "Horizontal"

       
    



    def input_datas (self,layout ):
        gridLayout = QGridLayout()
        self.__GeneralAndChart(gridLayout , 0 , 0)
        self.__PointLoad(gridLayout , 0 , 1)
        self.__LineLoad(gridLayout , 0 , 2)
        self.__StripLoad(gridLayout , 1 , 1 )
        self.__UniformLoad(gridLayout , 1 , 2 )
        self.PointLoadBox.setEnabled(True)
        self.LineLoadBox.setEnabled(False)
        self.StripLoadBox.setEnabled(False)
        self.UniformLoadBox.setEnabled(False)

        layout.addLayout(gridLayout)


    def processButtonFunction (self , layout):
        self.processButton = QPushButton ("Calculate" , self)
        self.processButton.setEnabled(False) 
        self.processButton.clicked.connect(self.process)
        layout.addWidget(self.processButton , alignment = Qt.AlignLeft)

    

    def resetButtonFunction (self , layout):
        self.resetButton = QPushButton ("Reset" , self)
        self.resetButton.clicked.connect(self.resetAll)
        layout.addWidget(self.resetButton , alignment = Qt.AlignRight)


    def calculatePointLoad(self):
        z = 0 
        zArr = []
        deltaArr = []
        try:
            while (z <= float(self.maxExpextedDepth.text())):
                delta = 3 * float (self.q_pointLoad.text())/(2 * math.pi) * math.pow(z , 3) / math.pow(float (self.x_pointLoad.text())**2 + float (self.y_pointLoad.text())**2 + z**2 , 2.5)
                zArr.append(z)
                deltaArr.append(delta)
                
                z += float(self.depthIncrement_string)

            return zArr , deltaArr
        except:
            raise Exception("x , y")
        

    def calculateLineLoadVertical(self):
        z = 0 
        zArr = []
        deltaArr = []
        try:
            while (z <= float(self.maxExpextedDepth.text())):
                delta = 2 * float (self.q_lineLoad.text())* math.pow(z , 3) /(math.pi * math.pow(float (self.x_lineLoad.text())**2 + z**2 , 2))
                zArr.append(z)
                deltaArr.append(delta)

                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("x")


    def calculateLineLoadHorizontal(self):
        z = 0 
        zArr = []
        deltaArr = []
        try:
            while (z <= float(self.maxExpextedDepth.text())):
                delta = 2 * float (self.q_lineLoad.text())*float (self.x_lineLoad.text())* math.pow(float (self.q_lineLoad.text()) , 2) /(math.pi * math.pow(float (self.x_lineLoad.text())**2 + z**2 , 2))
                zArr.append(z)
                deltaArr.append(delta)
                
                
                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("x")


    def calculateStripLoadVertical(self):
        z = 0 
        zArr = []
        deltaArr = []


        try:
            
            while (z <= float(self.maxExpextedDepth.text())):
                A =  math.pi + math.radians (math.atan(z /(float(self.x_stripLoad.text()) - float(self.B_stripLoad.text())/2) ))
                if 0 < float(self.x_stripLoad.text()) and float(self.x_stripLoad.text()) < float(self.B_stripLoad.text())/2:
                    pass 
                else : 
                    A -= math.pi
                
                M =  math.radians (math.atan(z /(float(self.x_stripLoad.text()) + float(self.B_stripLoad.text())/2) ))
            
                delta = float(self.q_stripLoad.text())/math.pi * (A - M - float(self.B_stripLoad.text()) * z * (float(self.x_stripLoad.text())**2 - z**2 - (float(self.B_stripLoad.text())**2)/4))/(math.pow((float(self.x_stripLoad.text())**2 - z**2 - (float(self.B_stripLoad.text())**2)/4) , 2) + math.pow(float(self.B_stripLoad.text()),2) * math.pow(z , 2))
                zArr.append(z)
                deltaArr.append(delta)
                
                
                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("B , x")

    def calculateStripLoadHorizontal(self):
        z = 0 
        zArr = []
        deltaArr = []


        try:
            while (z <= float(self.maxExpextedDepth.text())):
                delta = 2 * float(self.B_stripLoad.text()) * float(self.q_stripLoad.text()) * float(self.x_stripLoad.text()) * math.pow(z , 2)/ (math.pi * (math.pow((float(self.x_stripLoad.text())**2 - z**2 - (float(self.B_stripLoad.text())**2)/4) , 2) + math.pow(float(self.B_stripLoad.text()),2) * math.pow(z , 2)))
                zArr.append(z)
                deltaArr.append(delta)
              

                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("x")
        
    def calculateUnifromLoadCircural(self):
        z = float(self.depthIncrement_string)
        zArr = []
        deltaArr = []

        try:
            while (z <= float(self.maxExpextedDepth.text())):
                delta = float(self.q_uniformLoad.text()) *(1 - 1 /(math.pow (math.pow(float(self.R_uniformLoad.text())/z ,2) , 1.5)))
                deltaArr.append(delta)
                zArr.append(z)


                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("R")
        
    
    
    def calculateUnifromLoadRect(self):
        z = float(self.depthIncrement_string)
        


        zArr = []
        deltaArr = []

        try:
            while (z <= float(self.maxExpextedDepth.text())):
                m = float(self.B_uniformLoad.text())/(2*z)
                n = float(self.L_uniformLoad.text())/(2*z)

                F = math.radians(math.atan(2 * m * n * math.sqrt(math.pow(m , 2) + math.pow(n , 2) + 1))/(math.pow(m ,2) + math.pow(n , 2) - math.pow(m*n , 2) + 1))
                if (math.pow(m,2) + math.pow(n,2) + 1 < math.pow(m*n , 2)):
                    pass
                else :
                    F += math.pi
                
                I = 1/(4*math.pi) * (F + 2*m*n*math.sqrt(m**2 + n**2 + 1)/(math.pow(m,2)+math.pow(n,2)+math.pow(m*n,2)+1)* (math.pow(m,2) + math.pow(n,2)+2)/(math.pow(m,2) + math.pow(n,2)+1))
                


                delta = I * 4 * float(self.q_uniformLoad.text())
                deltaArr.append(delta)
                zArr.append (z)
              
                
                z += float(self.depthIncrement_string)
            return zArr , deltaArr
        except:
            raise Exception("L , B")




    def process(self):
        z = []
        deltaSigma = [] 
        try:
            if (self.LoadType_string == "Point Load"):
                z , deltaSigma = self.calculatePointLoad ()
                



            elif (self.LoadType_string == "Line Load"):
                if (self.direction_lineLoad_string == "Vertical"):
                    z , deltaSigma = self.calculateLineLoadVertical ()
                else :
                    
                    z , deltaSigma = self.calculateLineLoadHorizontal ()




            elif (self.LoadType_string == "Strip Load"):
                if (self.direction_stripLoad_string == "Vertical"):
                    z , deltaSigma = self.calculateStripLoadVertical ()
                    
                else :
                    z , deltaSigma = self.calculateStripLoadHorizontal ()


            elif (self.LoadType_string == "Uniform Load"):
                if (self.AreaType_string == "Circular" ):
                    z , deltaSigma = self.calculateUnifromLoadCircural ()
                    
                else:
                    z , deltaSigma = self.calculateUnifromLoadRect ()

            self.addResultToWindow(z , deltaSigma , self.layout)
        except Exception as e :
            self.inputError(str(e))
    

    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
        error_dialog.exec_()



    def addResultToWindow (self ,z , sigma, layout):
        SigmaPerZ = Figure (figsize=(10 , 12) , dpi=100)
        theAxes = SigmaPerZ.add_subplot(111)
        
        theAxes.plot ( sigma,z , marker = '.' , label="Delta Simga Z")

        theAxes.legend()


        theAxes.invert_yaxis()
        theAxes.xaxis.tick_top()
        theShape = FigureCanvas(SigmaPerZ)
        tool = NavigationToolbar(theShape, self)

        theAxes.grid(linewidth=0.5, alpha=0.5)
        theAxes.set_ylabel('Z (m)')
        theAxes.xaxis.set_label_position('top')
        theAxes.set_xlabel('Delta Simga Z(ton/m\N{SUPERSCRIPT TWO})')



        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        theShape.mpl_connect('motion_notify_event', on_mouse_move)




        if self.layout.count() > 0:
            layout_item = self.layout.takeAt(1)
            if layout_item:
                layout_item.widget().deleteLater()
                

        layout.addWidget(theShape)


    def resetAll(self):
        theInputs = [self.maxExpextedDepth , self.q_pointLoad , self.x_pointLoad , self.y_pointLoad , self.q_lineLoad , self.x_lineLoad , self.q_stripLoad, self.B_stripLoad, self.x_stripLoad , self.q_uniformLoad,self.B_uniformLoad, self.R_uniformLoad, self.L_uniformLoad ]

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
                
        pass



    def enButton(self):

        if (self.maxExpextedDepth.text() == ''):
            self.processButton.setEnabled(False)
            return
        else :
            if self.LoadType_string == "Point Load":
                if self.q_pointLoad.text() == '' or self.x_pointLoad.text() == '' or self.y_pointLoad.text() == '' :
                    self.processButton.setEnabled(False)
                    return

            elif self.LoadType_string == "Line Load":
                if self.q_lineLoad.text() == '' or self.x_lineLoad.text() == ''  :
                    self.processButton.setEnabled(False)
                    return

            elif self.LoadType_string == "Strip Load":
                if self.q_stripLoad.text() == '' or self.B_stripLoad.text() == '' or self.x_stripLoad.text() == '' :
                    self.processButton.setEnabled(False)
                    return

            elif self.LoadType_string == "Uniform Load":
                if self.AreaType_string == "Circular" :

                    if self.q_uniformLoad.text() == '' or self.R_uniformLoad.text() == '' :
                        self.processButton.setEnabled(False)
                        return
                elif self.AreaType_string == "Rectangular" :
                    if self.q_uniformLoad.text() == '' or self.L_uniformLoad.text() == '' or self.B_uniformLoad.text() == '' :
                        self.processButton.setEnabled(False)
                        return

        self.processButton.setEnabled(True)



    # def inputError(self , theInput):
    #     error_dialog = QErrorMessage()
    #     error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
    #     error_dialog.exec_()





