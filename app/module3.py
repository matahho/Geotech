
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




class Module3(QWidget):


    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        


        # Initialize tab screen

        self.module3 = QWidget()
        # self.tabs.setStyleSheet(""" 
                                    

        #                             QTabBar::tab {
        #                                 padding: 5px;
        #                                 border: 2px solid #19A7CE;
        #                                 border-top-left-radius: 5px;
        #                                 border-top-right-radius: 5px;
        #                                 background-color: #19A7CE;
        #                                 color: #fff;
        #                             }

        #                             QTabBar::tab:selected {
        #                                 background-color: #fff;
        #                                 color: #19A7CE;
        #                             }
        # """)




        # Create first tab
        self.module3.layout = QGridLayout(self)


        self.input_datas (self.module3.layout)
        self.module3.setLayout(self.module3.layout)


        #Tab 2 
        
        # Add tabs to widget
        self.layout.addWidget(self.module3)
        
        self.setLayout(self.layout)
    
        self.whichRowsHasChanged = set()
    def cellChangedHandeler(self, item):
        self.whichRowsHasChanged.add(item.row())


    def input_datas (self,layout ):
        gridLayout = QGridLayout()
        verticalLayout = QVBoxLayout()
        
        #SEISMIC DATA
        #earthquakeMagnitude
        self.earthquakeMagnitude =  QLineEdit()
        self.earthquakeMagnitude.setFixedWidth(70)
        self.earthquakeMagnitude.setValidator(QDoubleValidator())
        self.earthquakeMagnitude.textChanged.connect(self.enButton)
        #amax/g
        self.amaxPerG =  QLineEdit()
        self.amaxPerG.setFixedWidth(70)
        self.amaxPerG.setValidator(QDoubleValidator())
        self.amaxPerG.textChanged.connect(self.enButton)
        #FOS
        self.FOS =  QLineEdit()
        self.FOS.setFixedWidth(70)
        self.FOS.setValidator(QDoubleValidator())
        self.FOS.textChanged.connect(self.enButton)

        #MSF
        self.MSF = QComboBox ()
        self.MSF.addItems(["NCEER U.B." , "NCEER L.B." , "Seed & Idriss"])
        self.MSF.setFixedWidth(100)
        self.MSFvalue = "NCEER U.B."
        self.MSF.currentTextChanged.connect(self.MSFmodeFunction)

        #SPT CORRECTION FACTOR
        #Cn 
        self.CNFormula = QComboBox ()
        self.CNFormula.addItems(["Seed & Idriss" , u"Kayen et al."])
        self.CNFormulaValue = "Seed & Idriss"
        self.CNFormula.currentTextChanged.connect (self.CNFormulaFunction)
        
        #SPT efficiency
        self.SPTEfficiency =  QLineEdit()
        self.SPTEfficiency.setFixedWidth(70)
        self.SPTEfficiency.setValidator(QDoubleValidator())
        self.SPTEfficiency.setPlaceholderText("%")
        self.SPTEfficiency.textChanged.connect(self.enButton)

        #apply CB 
        self.applyCB = QComboBox ()
        self.applyCB.addItems(["Yes" , "No"])
        self.applyCBValue = "Yes"
        self.applyCB.currentTextChanged.connect (self.applyCBFunction)
        #apply CR
        self.applyCR = QComboBox ()
        self.applyCR.addItems(["Yes" , "No"])
        self.applyCRValue = "Yes"
        self.applyCR.currentTextChanged.connect (self.applyCRFunction)
        #sampler Type
        self.samplerType = QComboBox ()
        self.samplerType.addItems(["Standard" , "without Liner"])
        self.samplerTypeValue = "Standard"
        self.samplerType.currentTextChanged.connect (self.samplerTypeFunction)



        #GEOMETRY & WATER TABLE
        #GroundElevation
        self.GroundElevation =  QLineEdit()
        self.GroundElevation.setFixedWidth(70)
        self.GroundElevation.setValidator(QDoubleValidator())
        self.GroundElevation.setPlaceholderText("meters")
        self.GroundElevation.textChanged.connect(self.enButton)

        #GroundWaterElevation
        self.GroundWaterElevation =  QLineEdit()
        self.GroundWaterElevation.setFixedWidth(70)
        self.GroundWaterElevation.setValidator(QDoubleValidator())
        self.GroundWaterElevation.setPlaceholderText("meters")
        self.GroundWaterElevation.textChanged.connect(self.enButton)

        #gammaWater
        self.gammaWater =  QLineEdit()
        self.gammaWater.setFixedWidth(70)
        self.gammaWater.setValidator(QDoubleValidator())
        self.gammaWater.setPlaceholderText(u"kN/m\u00B3")
        self.gammaWater.textChanged.connect(self.enButton)

        #Bore Hole dia
        self.boreHoleDiameter = QLineEdit()
        self.boreHoleDiameter.setFixedWidth(70)
        self.boreHoleDiameter.setValidator(QDoubleValidator())
        self.boreHoleDiameter.setPlaceholderText(u"mm")
        self.boreHoleDiameter.textChanged.connect(self.enButton)


        #SOIL CHARACTERISTICS
        self.soilChar = QLabel()
        self.soilChar.setToolTip("اطلاعات خاک")
        self.soilChar.setText("SOIL CHARACTERISTICS")  


        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(25)
        self.tableWidget.setColumnCount(8)
        for i in range (3):
            self.tableWidget.setColumnWidth(i , 80)

        for i in range (3 , self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(i , 65)
        
        

        self.tableWidget.setHorizontalHeaderLabels(["Depth(m)", "Measured(N)" , u"\u03B3 soil(kN/m\u00B3)" , 
            "F.C." , "CL.C." , "LL" , "PI" , u"\u03C9"])
        for j in range(0 , int(self.tableWidget.columnCount())):
            self.tableWidget.openPersistentEditor(self.tableWidget.itemAt(25, 8))
        
        #self.tableWidget.cellChanged.connect(self.enButton)


        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(

                )
                self.tableWidget.setItem(i, j, item)
        # tooltips for headers of table 
        tableColor = "#fafcff"
        itemTableColor = "#e6efff"
        tableHeaderColor = "#a6c6f7"
        tableTitleColor = "#146C94"

        self.tableWidget.horizontalHeaderItem(0).setToolTip("عمق")
        self.tableWidget.horizontalHeaderItem(1).setToolTip(" مقدار"+"SPT"+"برای هر عمق ")
        self.tableWidget.horizontalHeaderItem(2).setToolTip("وزن مخصوص خاک")
        self.tableWidget.horizontalHeaderItem(3).setToolTip("درصد ریزدانه")
        self.tableWidget.horizontalHeaderItem(4).setToolTip("درصد رس")
        self.tableWidget.horizontalHeaderItem(5).setToolTip("حد رواانی")
        self.tableWidget.horizontalHeaderItem(6).setToolTip("شاخص پلاستیسیته")
        self.tableWidget.horizontalHeaderItem(7).setToolTip("میزان رطوبت")

        
        self.tableWidget.setStyleSheet("""
                                QTableWidget {
                                    background-color: %s;
                                    alternate-background-color: %s;
                                    selection-background-color: %s;
                                    selection-color: #000000;
                                    border: 1px solid #cccccc;
                                }

                                QTableWidget QHeaderView::section {
                                    background-color: %s;
                                    color: %s;
                                    padding: 4px;
                                }

                                QTableWidget::item {
                                    padding: 4px;
                                    background-color:%s;
                                }
                                """ %(tableColor,tableHeaderColor ,tableHeaderColor,tableHeaderColor,tableTitleColor, itemTableColor) )

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

        self.tableWidget.itemChanged.connect(self.cellChangedHandeler)
        #start group 1 
        self.Seismic_Box = QGroupBox("SEISMIC DATA ")
        self.Seismic_Box.setStyleSheet(boxesStyle)
        self.Seismic_Part = QFormLayout()
        self.Seismic_Box.setAlignment(Qt.AlignCenter)

        r1Label = QLabel("E.M. ")
        r1Label.setToolTip("Earthquake Magnitude\nبزرگای زلزله (طرح) ریشتر")
        self.Seismic_Part.addRow (r1Label , self.earthquakeMagnitude)
        
        r2Label = QLabel(u"a\u2098\u2090\u2093/g ")
        r2Label.setToolTip("شتاب حداکثر در سطح زمین برمبنای شتاب جاذبه")
        self.Seismic_Part.addRow (r2Label , self.amaxPerG)

        r3Label = QLabel("FOS ")
        r3Label.setToolTip("ضریب اطمینان")
        self.Seismic_Part.addRow (r3Label , self.FOS)

        r4Label = QLabel("MSF " )
        r4Label.setToolTip("ضریب تصحیح بزرگای زلزله")
        self.Seismic_Part.addRow(r4Label, self.MSF)

        self.Seismic_Box.setLayout(self.Seismic_Part)
        # end of group 1 

        
        #start group 2 
        self.SPT_Box = QGroupBox("SPT CORRECTION FACTOR")
        self.SPT_Box.setStyleSheet(boxesStyle)
        self.SPT_Part = QFormLayout()
        self.SPT_Box.setAlignment(Qt.AlignCenter)
        self.SPT_Part.addRow (u"C\u2099 Formula " , self.CNFormula)

        g2r2Label = QLabel("SPT Efficiency (%) ")
        g2r2Label.setToolTip(" SPT بازده آزمایش")
        self.SPT_Part.addRow (g2r2Label , self.SPTEfficiency)

        
        self.SPT_Part.addRow (u"Apply C\u1D2E " , self.applyCB)
        self.SPT_Part.addRow ("Apply Cᴿ " , self.applyCR)     

        g2r5Label = QLabel("Sampler Type ")
        g2r5Label.setToolTip("نوع نمونه")
        self.SPT_Part.addRow (g2r5Label , self.samplerType)

        self.SPT_Box.setLayout(self.SPT_Part)
        #end of group 2




        self.Geo_Box = QGroupBox("GENERAL")
        self.Geo_Box.setStyleSheet(boxesStyle)
        self.Geo_Part = QFormLayout()
        self.Geo_Box.setAlignment(Qt.AlignCenter)

        g3r1Label = QLabel("G.E. (m) " )
        g3r1Label.setToolTip("Ground Elevation \n سطح زمین")
        self.Geo_Part.addRow (g3r1Label, self.GroundElevation )

        g3r2Label = QLabel("G.W.E (m) ")
        g3r2Label.setToolTip("Ground Water Elevation \nسطح آب زیرزمینی")
        self.Geo_Part.addRow (g3r2Label , self.GroundWaterElevation)

        g3r3Label = QLabel(u"\u03B3 \u1D65\u1D65 (kN/m\u00B3) ")
        g3r3Label.setToolTip("چگالی آب زیرزمینی")
        self.Geo_Part.addRow (g3r3Label , self.gammaWater)

        g3r4Label = QLabel("BH Dia(mm)")
        g3r4Label.setToolTip("Bore Hole Diameter\nقطر گمانه")
        self.Geo_Part.addRow (g3r4Label , self.boreHoleDiameter)


        self.Geo_Box.setLayout(self.Geo_Part)

        #end of group 3 



        
        gridLayout.addWidget(self.Seismic_Box , 0 , 0 )
        gridLayout.addWidget(self.SPT_Box , 0 , 1 )
        gridLayout.addWidget(self.Geo_Box , 0 , 2 )


        ButtonLayout = QHBoxLayout()
        self.graphButtonFunction(ButtonLayout)
        self.resetButtonFunction(ButtonLayout)




        verticalLayout.addLayout(gridLayout)
        verticalLayout.addWidget(self.soilChar , alignment = Qt.AlignCenter) 
        verticalLayout.addWidget(self.tableWidget)
        verticalLayout.addLayout(ButtonLayout)



        layout.addLayout(verticalLayout, 1, 0)
    

    def module3HelpFunction(self):
        pixmap = QPixmap('module3Help1.png')
        image_label = QLabel()
        image_label.setPixmap(pixmap)


        message_box = QMessageBox()
        #message_box.layout().addWidget(image_label)
        message_box.setWindowTitle('Module 3 Help')
        about = "شما در حال استفاده از ماژول روانگرایی از نرم افزار GeOnin هستید"
        about2 = "روانگرایی پدیده ای است که اغلب در خاک های ماسه ای مشاهده شده است . هر چند شواهدی از وقوع آن درخاکهای ریزدانه و حتی رسها هم وجود دارد . به طور کلی در خاک های ریزدانه با افزایش درصد رطوبت نسبت به رطوبت حالت روانی پتانسیل روانگرایی افزوده میشود . به عبارت دیگر خاک های ریزدانه باخاصیت خمیری زیاد معمولا استعداد روانگرایی ندارند . اما لای های غیر خمیری و لای ها و رس ها با خواص خمیری کم مستعد روانگرایی اند."
        about3 = "امروزه معیار های مختلفی جهت تعیین پتانسیل روانگرایی خاکهای دانه ای نظیر ماسه ها و استعداد روانگرایی خاک های ریزدانه ارائه شده است که معروف ترین آنها در NCEER منعکس شده است ."
        about4 = "پتانسیل وقوع روانگرایی در ماسه ها بر اساس روش نسبت تنش برشی متناوب انجام میپذیرد . در این روش ضریب اطمینان در مقابل روانگرایی از رابطه ی زیر تعیین میگردد : "
        about5 = "در رابطه فوق CRR مقاومت خاک جهت جلوگیری از روانگرایی هنگام وقوع زلزله بر اساس نسبت تنش میباشد ."
        about6 = "همچنین CSR نیز بارگذاری تناوبی ناشی از زلزله طرح برحسب نسبت تنش متناوب است "
        message_box.setText(about + "\n\n    " + about2 + "\n\n    " + about3 + "\n\n    " + about4 + "\n\n" + "SF = CRR / CSR" + "\n\n" + about5 + "\n" + about6)
        message_box.exec_()

    # def module3HelpFunction2(self):
    #     pixmap = QPixmap('Yukitake-Shioi-Fig1.png')
    #     image_label = QLabel()
    #     image_label.setPixmap(pixmap)
    #     message_box = QMessageBox()
    #     message_box.layout().addWidget(image_label)
    #     message_box.setWindowTitle('Module 3 Help')
    #     #message_box.setStandardButtons(QMessageBox.NoButton)
    #     message_box.exec_()

    def enButton(self):
        #TO DO : bayad check shavad ke row = 0 table filled bashad !
        if (self.gammaWater.text() == '' or self.GroundWaterElevation.text() == '' or self.GroundElevation.text() == '' or self.SPTEfficiency.text() == '' or self.FOS.text() == '' or self.amaxPerG.text() == '' or self.earthquakeMagnitude.text() == '' or self.boreHoleDiameter.text() == ''):
            self.graphButton.setEnabled(False)
        else :
            self.graphButton.setEnabled(True)
                
    def graphButtonFunction(self , layout):
        self.graphButton = QPushButton ("Graph" , self)
        self.graphButton.clicked.connect(self.drawGraph)
        self.graphButton.setEnabled(False)
        layout.addWidget(self.graphButton ,alignment = Qt.AlignLeft)

    def resetButtonFunction(self , layout):
        self.resetButton = QPushButton ("Reset" , self)
        self.resetButton.clicked.connect(self.resetAll)
        #self.resetButton.setEnabled(True)
        layout.addWidget(self.resetButton ,alignment = Qt.AlignRight)




    def MSFmodeFunction (self , s ):
        if (s == "NCEER U.B."):
            self.MSFmode = "NCEER U.B."
        elif (s == "NCEER L.B."):
            self.MSFmode = "NCEER L.B."
        elif (s == "Seed & Idriss"):
            self.MSFmode = "Seed & Idriss"

    def samplerTypeFunction (self , s ):
        if (s == "Standard"):
            self.samplerTypeValue = "Standard"
        elif (s == "without Liner"):
            self.samplerTypeValue = "without Liner"
        
    def CNFormulaFunction ( self , s):
        if (s == "Seed & Idriss"):
            self.CNFormulaValue = "Seed & Idriss"
        else :
            self.CNFormulaValue = u"Kayen et a\u2081\u2080"

    def applyCRFunction(self , s):
        if (s == "Yes"):
            self.applyCRValue = "Yes"
        else :
            self.applyCRValue = "No"

    def applyCBFunction(self , s):
        if (s == "Yes"):
            self.applyCBValue = "Yes"
        else :
            self.applyCBValue = "No"
    


    def calculate_MSF(self):

        try:
            if (self.MSFvalue == "NCEER U.B."):
                msf = 846.26 * math.pow(float(self.earthquakeMagnitude.text()),-3.349)
            elif (self.MSFvalue == "NCEER L.B."):
                msf = math.pow(10 , 2.24) / math.pow(float(self.earthquakeMagnitude.text()) , 2.56)
            elif (self.MSFvalue == "Seed & Idriss"):
                msf = 9.7841 * math.pow(float(self.earthquakeMagnitude.text()) , -1.128)
            return msf
        except:
            raise Exception("E.M.")



    def calculate_CE (self):
        return (float(self.SPTEfficiency.text())/60)

    def calculate_CS(self):
        if (self.samplerTypeValue == "Standard"):
            return 1
        if (self.samplerTypeValue == "without Liner"):
            return 1.1


    def category1 (self):
        cat1 = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):
            
            if (self.tableWidget.item(row , 0) != None):
                if (float(self.tableWidget.item(row , 5).text()) < 35 and float(self.tableWidget.item(row , 4).text()) < 15 and float(self.tableWidget.item(row , 7).text())>(0.9*float(self.tableWidget.item(row , 5).text()))):
                    cat1.append(["A"])
                else :
                    cat1.append(["C"])
            else :
                cat1.append("NULL")

        return cat1

    def category2(self , cat):
        rowCount = max(self.whichRowsHasChanged) + 1

        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (float(self.tableWidget.item(row , 5).text()) < 32 and float(self.tableWidget.item(row , 4).text()) < 10 ):
                    
                    cat[row].append("A")
                elif (float(self.tableWidget.item(row , 5).text()) < 32 and float(self.tableWidget.item(row , 4).text()) > 10 ):
                    cat[row].append("B")
                elif (float(self.tableWidget.item(row , 5).text()) > 32 and float(self.tableWidget.item(row , 4).text()) < 10 ):
                    cat[row].append("B")
                elif (float(self.tableWidget.item(row , 5).text()) > 32 and float(self.tableWidget.item(row , 4).text()) > 10 ):
                    cat[row].append("C")

    def category3 (self , cat ):
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0) ):
                if (float(self.tableWidget.item(row , 5).text()) < 37 and float(self.tableWidget.item(row , 6).text()) < 12 and
                 float(self.tableWidget.item(row , 7).text())>(0.8*float(self.tableWidget.item(row , 5).text()))):
                    cat[row].append("A")
                elif (float(self.tableWidget.item(row , 5).text()) < 47 and float(self.tableWidget.item(row , 6).text()) < 20 and
                 float(self.tableWidget.item(row , 7).text())>(0.85*float(self.tableWidget.item(row , 5).text()))):
                    cat[row].append("B")
                else :
                    cat[row].append("C")


    def categotyType(self , cat):
        types = []
        for item in cat :
            if (item.count("A") >= 2 ):
                types.append("A")
            elif (item.count("B") >= 2 ):
                types.append("B")
            elif (item.count("C") >= 2 ):
                types.append("C")
        return types

    def calculate_Pwi(self):
        pw = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):
            if (self.tableWidget.item(row , 0)):
                pw.append( max(0 , float(self.gammaWater.text())*(float(self.GroundWaterElevation.text())-float(self.GroundElevation.text())+
                 float(self.tableWidget.item(row , 0).text()))))
        return pw

    def calculate_sigmaV(self):
        sigmaV = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):
            if (self.tableWidget.item(row , 0)):
                if (row == 0 ):
                    sigmaV.append(float(self.tableWidget.item(row , 0).text()) * float(self.tableWidget.item(row , 2).text())) 
                else :
                    sigmaV.append((float(self.tableWidget.item(row , 0).text())-float(self.tableWidget.item(row-1 , 0).text()))*float(self.tableWidget.item(row , 2).text())+sigmaV[row-1])
        return sigmaV

    def calculate_sigmaPrimeV(self , sigmaV , pw ):
        sigmaPrimeV = []
        if float(self.tableWidget.item(0 , 0).text()) == 0 :
            raise Exception("Depth [1]")


        for i in range(0 , len(pw)):
            sigmaPrimeV.append(sigmaV[i] - pw[i])
        return sigmaPrimeV


    def calculate_CN (self , sigmaPrimeV):
        CN = []
        if (self.CNFormulaValue == "Seed & Idriss"):
            for i in range(0 , len(sigmaPrimeV)):
                CN.append(min(1.7 , math.sqrt(abs(100/sigmaPrimeV[i]))))
        else :
            for i in range(0 , len(sigmaPrimeV)):
                CN.append(2.2/(1.2+(sigmaPrimeV[i]/100)))
        return CN

    
    def calculate_CR (self):
        CR = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (self.applyCRValue == "Yes"):
                    if (float(self.tableWidget.item(row , 0).text()) < 3):
                        CR.append(0.75)
                    elif (3 <= float(self.tableWidget.item(row , 0).text()) and float(self.tableWidget.item(row , 0).text()) < 4):
                        CR.append(0.8)
                    elif (4 <= float(self.tableWidget.item(row , 0).text()) and float(self.tableWidget.item(row , 0).text()) < 6):
                        CR.append(0.85)
                    elif (6 <= float(self.tableWidget.item(row , 0).text()) and float(self.tableWidget.item(row , 0).text()) < 10):
                        CR.append(0.95)
                    else :
                        CR.append(1)
                else :
                    CR.append(1)
        return CR

    def calculate_CB(self):
        CB = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (self.applyCBValue == "Yes"):
                    if (float(self.boreHoleDiameter.text()) <= 115):
                        CB.append(1)
                    elif (115 < float(self.boreHoleDiameter.text()) and float(self.boreHoleDiameter.text()) <= 150):
                        CB.append(1.05)
                    else :
                        CB.append(1.15)
                else :
                    CB.append(1)

        return CB



    def calculate_N1sigma0(self , CN , CS , CR , CE):
        N1sigma0 = []
        for row in range(0 , len(CN)):
            if (self.tableWidget.item(row , 0)):
                N1sigma0.append(float(self.tableWidget.item(row , 1).text())*CN[row]*CS*CR[row]*CE)
        return N1sigma0


    def calculate_alpha(self):
        alpha = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (float(self.tableWidget.item(row , 3).text()) <= 5):
                    alpha.append(0)
                elif (5 < float(self.tableWidget.item(row , 3).text()) and float(self.tableWidget.item(row , 3).text()) <= 35 ):
                    alpha.append(math.pow(math.e , 1.76-(190/(float(self.tableWidget.item(row , 3).text())*float(self.tableWidget.item(row , 3).text())))))
                else:
                    alpha.append(5)
        return alpha


    def calculate_beta(self):
        beta = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (float(self.tableWidget.item(row , 3).text()) <= 5):
                    beta.append(1)
                elif (5 < float(self.tableWidget.item(row , 3).text()) and float(self.tableWidget.item(row , 3).text()) <= 35 ):
                    beta.append(0.99 + math.pow(float(self.tableWidget.item(row , 3).text()) , 1.5)/1000)
                else:
                    beta.append(1.2)
        return beta
    

    def calculate_N1sigma0CS(self , alpha , N1sigma0 , beta):
        N1sigma0CS = []
        for row in range(0 , len(N1sigma0)):
            N1sigma0CS.append(alpha[row] + N1sigma0[row]*beta[row])
        return N1sigma0CS


    def calculate_CRR7 (self , N1sigma0CS):
        CRR7 = []
        for row in range(0 , len(N1sigma0CS)):
            if (N1sigma0CS[row] >= 30 ):
                CRR7.append ("N/A")
            else :
                x = 1/(34 - N1sigma0CS[row]) + N1sigma0CS[row]/135 + 50/math.pow((10*N1sigma0CS[row]+45) , 2) - 1/200
                CRR7.append(x)
        return CRR7
    
    def calculate_FPI(self):
        FPI = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (float(self.tableWidget.item(row , 6).text()) <= 10):
                    FPI.append(1)
                else:
                    1 + 0.022*(float(self.tableWidget.item(row , 6).text())-10)
        return FPI

    def calculate_CRR(self , CRR7 , FPI , types , MSF):
        
        CRR = []
        rowCount = max(self.whichRowsHasChanged) + 1
        # TODO:Length of types is not equal to length of CRR7 and rowCount must be solve
        #print("----" , len(types) , len(CRR7) , rowCount)
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                if (CRR7[row] == "N/A" or types[row] == "C"):
                    CRR.append(1)
                else:
                    CRR.append(CRR7[row]*FPI[row]*MSF)
        return CRR

    

    def calculate_rd(self):
        rd = []
        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):

            if (self.tableWidget.item(row , 0)):
                up = 1 - 0.4113*math.sqrt(abs(float(self.tableWidget.item(row , 0).text()))) + 0.04052*float(self.tableWidget.item(row , 0).text()) + 0.001753*math.pow(float(self.tableWidget.item(row , 0).text()),1.5)
                down = 1 - 0.4177*math.sqrt(abs(float(self.tableWidget.item(row , 0).text()))) + 0.05729*float(self.tableWidget.item(row , 0).text()) - 0.006205*math.pow(float(self.tableWidget.item(row , 0).text()),1.5) + 0.00121*math.pow(float(self.tableWidget.item(row , 0).text()),2)
                rd.append(up/down)
        return rd


    def calculate_CSReq (self , sigmaPrimeV , sigmaV , rd):
        CSReq = []
        for row in range(0 , len(rd)):
            if (sigmaPrimeV[row] == 0 ):
                CSReq.append(0)
            else :
                CSReq.append(0.65*float(self.amaxPerG.text())*sigmaV[row]*rd[row]/sigmaPrimeV[row])
        return CSReq
    
    def calculate_SF(self , CRR , CSReq):
        SF = []
        for i in range (0 , len(CRR)):
            if (CRR[i] == "N/A" or CSReq[i] == 0):
                SF.append("Non-liq")
            else :
                SF.append(CRR[i]/CSReq[i])
        return SF

    def calculate_SFliq (self , SF):
        SFliq = []
        for i in range(0 , len(SF)):
            if (SF[i] == "Non-liq"):
                SFliq.append(2)
            else:
                SFliq.append(min(2 , SF[i]))
        return SFliq



    def charts (self , SFliq , CRR7 , CRR , CSReq):
  
        self.graphWindow = QDialog(self)
        self.graphWindow.setFixedSize(1000 ,650) 
        self.graphWindow.setWindowTitle("Graph")
        self.graphWindowLayout = QGridLayout()
        self.graphWindow.setLayout(self.graphWindowLayout)
        
        chartX =[]
        chartY = []
        chart2X = []
        chart3X = []
        chart4X = []
        
        for i in SFliq:
            if (i =="Non-liq"):
                chartX.append(None)
            else :
                chartX.append(i)
        
        for i in CRR7:
            if (i =="N/A"):
                chart2X.append(None)
            else :
                chart2X.append(i)
        
        for i in CRR:
            if (i =="N/A"):
                chart3X.append(None)
            else :
                chart3X.append(i)
        
        for i in CSReq:
            if (i =="N/A"):
                chart4X.append(None)
            else :
                chart4X.append(i)

        


        rowCount = max(self.whichRowsHasChanged) + 1
        for row in range(0 , rowCount):
            if (self.tableWidget.item(row , 0)):
                chartY.append(float(self.tableWidget.item(row , 0).text()))

      
      
        ch = Figure(figsize=(3, 10), dpi=100 )
        ch_axes = ch.add_subplot(111)
        ch_axes.set_ylabel ("Depth (m)")
        ch_axes.set_xlabel ("Safty Factor against liquefaction")
        ch_axes.plot(chartX, chartY, marker = "o" )
        ch_axes.invert_yaxis()
        #ch_axes.vlines(x=1,ymin=-10 , ymax=10 ,colors='r', linestyles='--', lw=2)
        ch_axes.axvline(x=1, color='Green', linestyle='--')
        ch_axes.grid(linewidth=0.5, alpha=0.5)
        #ch_axes.xaxis.tick_top()
        ch_shape = FigureCanvas(ch)
        
        #cursor = Cursor(ch_axes)
        
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        ch_shape.mpl_connect('motion_notify_event', on_mouse_move)


        tool = NavigationToolbar(ch_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 0)
        self.graphWindowLayout.addWidget(ch_shape , 1 , 0)

        
        
        # this line will show the figure of CRR7.5 in figure shape

        # ch2 = Figure(figsize=(3, 10), dpi=100 )
        # ch2_axes = ch2.add_subplot(111)
        # ch2_axes.set_ylabel ("Depth (m)")
        # ch2_axes.set_xlabel ("CRR7.5")
        # ch2_axes.plot(chart2X, chartY, marker = "o" )
        # ch2_axes.invert_yaxis()
        # ch2_axes.grid(linewidth=0.5, alpha=0.5)
        # #ch_axes.vlines(x=1,ymin=-10 , ymax=10 ,colors='r', linestyles='--', lw=2)
        # #ch_axes.xaxis.tick_top()
        # ch2_shape = FigureCanvas(ch2)


        # cursor = Cursor(ch2_axes)
        # ch2_shape.mpl_connect('motion_notify_event', on_mouse_move)


        # tool2 = NavigationToolbar(ch2_shape, self)
        # self.graphWindowLayout.addWidget(tool2, 0 , 1)
        # self.graphWindowLayout.addWidget(ch2_shape , 1 , 1)
        
        
        # this line will run the CRR in unmerged figure

        # ch3 = Figure(figsize=(3, 10), dpi=100 )
        # ch3_axes = ch3.add_subplot(111)
        # ch3_axes.set_ylabel ("Depth (m)")
        # ch3_axes.set_xlabel ("CRR")
        # ch3_axes.plot(chart3X, chartY, marker = "o" )
        # ch3_axes.invert_yaxis()
        # ch3_axes.grid(linewidth=0.5, alpha=0.5)
        # #ch_axes.vlines(x=1,ymin=-10 , ymax=10 ,colors='r', linestyles='--', lw=2)
        # #ch_axes.xaxis.tick_top()
        # ch3_shape = FigureCanvas(ch3)
        # tool3 = NavigationToolbar(ch3_shape, self)

        # cursor = Cursor(ch3_axes)
        # ch3_shape.mpl_connect('motion_notify_event', on_mouse_move)


        # self.graphWindowLayout.addWidget(tool3, 0 , 2)
        # self.graphWindowLayout.addWidget(ch3_shape , 1 , 2)
        


        
        
        ch4 = Figure(figsize=(3, 10), dpi=100 )
        ch4.tight_layout()
        ch4_axes = ch4.add_subplot(111)
        ch4_axes.set_ylabel ("Depth (m)")
        ch4_axes.set_xlabel ("Cyclic Stress Ratios")
        ch4_axes.plot(chart4X, chartY, marker = "o" , label ="CSR(Eq)")
        ch4_axes.plot(chart3X, chartY, marker = "o" , color="red" , label="CRR")
        ch4_axes.invert_yaxis()
        ch4_axes.grid(linewidth=0.5, alpha=0.5)
        ch4_axes.legend()
        #ch_axes.vlines(x=1,ymin=-10 , ymax=10 ,colors='r', linestyles='--', lw=2)
        #ch_axes.xaxis.tick_top()
        ch4_shape = FigureCanvas(ch4)
        tool4 = NavigationToolbar(ch4_shape, self)


        #cursor = Cursor(ch4_axes)
        ch4_shape.mpl_connect('motion_notify_event', on_mouse_move)


        self.graphWindowLayout.addWidget(tool4, 0 , 3)
        self.graphWindowLayout.addWidget(ch4_shape , 1 , 3)
        

        self.graphWindow.exec()


    
    

    def checkWhichRowsChanged (self):
        theMax = max(self.whichRowsHasChanged)
        colCount = self.tableWidget.columnCount()
        for row in range(0 , theMax+1):
            for col in range(0 , colCount):
                if self.tableWidget.item(row , col).text() == '':
                    self.tableWidget.setItem(row , col , QTableWidgetItem('0'))

    def resetAll(self):
        theInputs = [self.earthquakeMagnitude , self.amaxPerG , self.FOS ,self.SPTEfficiency , self.GroundElevation , self.GroundWaterElevation , self.gammaWater , self.boreHoleDiameter]
        

        for inp in theInputs:
            inp.clear()

        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(r , c , QTableWidgetItem(''))

        self.whichRowsHasChanged.clear()


        self.graphButton.setEnabled(False)

    def drawGraph(self):
        self.checkWhichRowsChanged()
        try:
            cat = self.category1()
            self.category2(cat)
            self.category3(cat)
            types = self.categotyType(cat)
            pw = self.calculate_Pwi()

            sigmaV = self.calculate_sigmaV()

            sigmaPrimeV = self.calculate_sigmaPrimeV(sigmaV , pw )

            CR = self.calculate_CR()

            CN = self.calculate_CN(sigmaPrimeV)

            N1sigma0 = self.calculate_N1sigma0(CN , self.calculate_CS() , self.calculate_CR() , self.calculate_CE())

            N1sigma0CS = self.calculate_N1sigma0CS(self.calculate_alpha() , N1sigma0 , self.calculate_beta())


            CRR7 = self.calculate_CRR7(N1sigma0CS)

            CRR = self.calculate_CRR(CRR7 , self.calculate_FPI() , types , self.calculate_MSF())

            rd = self.calculate_rd()

            CSReq = self.calculate_CSReq(sigmaPrimeV , sigmaV , rd)
            SFliq = self.calculate_SFliq(self.calculate_SF(CRR , CSReq))
            
        
            self.charts(SFliq , CRR7 , CRR , CSReq)
        except Exception as e:
       
            self.inputError(str(e))






    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
        error_dialog.exec_()

