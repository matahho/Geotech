from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QToolButton , QMessageBox 
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog , QErrorMessage
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor ,QPixmap

from PyQt5.QtCore import Qt ,QSize
import sys , math


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure




        


class Module4(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        
        # Initialize tab screen

        self.module4 = QWidget()
 

        # Create first tab
        self.module4.layout = QGridLayout(self)



        self.module4Help = QToolButton()
        self.module4Help.setText("Help") 
        self.module4Help.setIconSize(QSize(20 , 20))
        self.module4Help.clicked.connect(self.module4HelpFunction)
        self.module4.layout.addWidget(self.module4Help ,0 , 0 , alignment = Qt.AlignRight)

        self.input_datas (self.module4.layout)
        self.layout.addWidget(self.module4)

        self.module4.setLayout(self.module4.layout)


        self.setLayout(self.layout)
    
        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.pixmap = self.pixmap.scaled(600,600) 
        self.logo.setPixmap(self.pixmap)

        #self.logo.resize(self.pixmap.width(),self.pixmap.height())
        self.layout.addWidget(self.logo)


    def input_datas (self,layout ):
        gridLayout = QGridLayout()
        verticalLayout = QVBoxLayout()
        

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


        #FOUNDATION DIMENTION 
        # B value 
        self.B =  QLineEdit()
        self.B.setValidator(QDoubleValidator())
        self.B.setPlaceholderText("meters")
        self.B.setFixedWidth(85)
        self.B.textChanged.connect(self.enButton)

        # L value
        self.L =  QLineEdit()
        self.L.setValidator(QDoubleValidator())
        self.L.setPlaceholderText("meters")
        self.L.setFixedWidth(85)
        self.L.textChanged.connect(self.enButton)
        

        #Df value
        self.Df =  QLineEdit()
        self.Df.setValidator(QDoubleValidator())
        self.Df.setPlaceholderText("meters")
        self.Df.setFixedWidth(85)
        self.Df.textChanged.connect(self.enButton)
        
        #t value
        self.t =  QLineEdit()
        self.t.setValidator(QDoubleValidator())
        self.t.setPlaceholderText("meters")
        self.t.setFixedWidth(85)
        self.t.textChanged.connect(self.enButton)

 
        #Efoundation value
        self.Efoundation =  QLineEdit()
        self.Efoundation.setValidator(QDoubleValidator())
        self.Efoundation.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.Efoundation.setFixedWidth(85)
        self.Efoundation.textChanged.connect(self.enButton)


        #I f value 
        self.If = QComboBox ()
        self.If.addItems(["Fox 1948" , u"Mayne & Polous"])
        self.IfValue = "Fox 1948"
        self.If.setFixedWidth(85)
        self.If.currentTextChanged.connect (self.IfFunction)
        
        #FoundationRigidity Value 
        self.FoundationRigidity = QComboBox ()
        self.FoundationRigidity.addItems(["Flexible" , "Rigid" , "Intermediate"])
        self.FoundationRigidityValue = "Flexible"
        self.FoundationRigidity.setFixedWidth(85)
        self.FoundationRigidity.currentTextChanged.connect (self.FoundationRigidityFunction)


        #FOUNDATION DIMENTION BOX CREATOR
        self.foundationDimention_Box = QGroupBox("FOUNDATION DIMENTION")
        self.foundationDimention_Box.setStyleSheet(boxesStyle)
        self.foundationDimention_Part = QFormLayout()
        BLabel = QLabel("B(m)")
        BLabel.setToolTip("عرض پی سطحی")
        self.foundationDimention_Part.addRow (BLabel , self.B)

        LLabel = QLabel ("L(m)")
        LLabel.setToolTip("طول پی سطحی")
        self.foundationDimention_Part.addRow (LLabel , self.L)

        DfLabel = QLabel (u"Dᶠ(m)")
        DfLabel.setToolTip("عمق استقرار پی سطحی")
        self.foundationDimention_Part.addRow (DfLabel , self.Df)

        tLabel = QLabel ("t(m)")
        tLabel.setToolTip("ضخامت پی سطحی") 
        self.foundationDimention_Part.addRow(tLabel , self.t)

        EfLabel = QLabel(u"Eᶠ (ton/m\N{SUPERSCRIPT TWO})")
        tLabel.setToolTip("مدول الاستیسیته پی سطحی") 
        self.foundationDimention_Part.addRow (EfLabel , self.Efoundation)

        IfLabel = QLabel (u"Iᶠ")
        IfLabel.setToolTip("ضریب تاثیر")
        self.foundationDimention_Part.addRow(IfLabel , self.If)

        FoundationRigLabel = QLabel ("F.R.")    
        FoundationRigLabel.setToolTip("Foundation Rigidity\nصلبیت فونداسیون")
        self.foundationDimention_Part.addRow(FoundationRigLabel , self.FoundationRigidity)

        self.foundationDimention_Box.setLayout(self.foundationDimention_Part)

        #--------------------------------------------------------------------

        #GENERAL + LOADING :
        #qPrimNet
        self.qPrimNet =  QLineEdit()
        self.qPrimNet.setValidator(QDoubleValidator())
        self.qPrimNet.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.qPrimNet.setFixedWidth(85)
        self.qPrimNet.textChanged.connect(self.enButton)


        #eBPerB
        self.eBPerB =  QLineEdit()
        self.eBPerB.setValidator(QDoubleValidator())
        self.eBPerB.setFixedWidth(85)
        self.eBPerB.textChanged.connect(self.enButton)

        #eLPerL
        self.eLPerL =  QLineEdit()
        self.eLPerL.setValidator(QDoubleValidator())
        self.eLPerL.setFixedWidth(85)
        self.eLPerL.textChanged.connect(self.enButton)


        #number of layers :
        self.numberOfLayers = QComboBox ()
        self.numberOfLayers.addItems(["1" , "2" , "3" , "4"])
        self.numberOfLayersValue = "1"
        self.numberOfLayers.setFixedWidth(85)
        self.numberOfLayers.currentTextChanged.connect (self.numberOfLayersFunction)

        

        #Q.W.L
        self.G_W_L = QLineEdit()
        self.G_W_L.setValidator(QDoubleValidator())
        self.G_W_L.setPlaceholderText("meter")
        self.G_W_L.setFixedWidth(85)
        self.G_W_L.textChanged.connect(self.enButton)
        
        #Ground water
        self.gammaWat = QLineEdit()
        self.gammaWat.setValidator(QDoubleValidator())
        self.gammaWat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.gammaWat.setFixedWidth(85)

        self.gammaWat.textChanged.connect(self.enButton)



        #Pa
        self.Pa =  QLineEdit()
        self.Pa.setValidator(QDoubleValidator())
        self.Pa.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.Pa.setFixedWidth(85)
        self.Pa.textChanged.connect(self.enButton)
        



        
        self.FoundationLoad_Box = QGroupBox("GENERAL + LOADING")
        self.FoundationLoad_Box.setStyleSheet(boxesStyle)
        self.FoundationLoad_Part = QFormLayout()

        NoofLayerLabel = QLabel ("No. of layers")
        NoofLayerLabel.setToolTip("تعداد لایه های خاک")
        self.FoundationLoad_Part.addRow (NoofLayerLabel , self.numberOfLayers)

        GWLLabel = QLabel ("G.W.E.(m)")
        GWLLabel.setToolTip("Ground Water Elevation\nتراز آب زیرزمینی ")
        self.FoundationLoad_Part.addRow ( GWLLabel, self.G_W_L)

        gammaWatLabel = QLabel(u"\u03B3 wat(ton/m\N{SUPERSCRIPT THREE})" )
        gammaWatLabel.setToolTip("وزن مخصوص آب")
        self.FoundationLoad_Part.addRow (gammaWatLabel , self.gammaWat)

        atmpressLabel = QLabel ("Atm. Press.(ton/m\N{SUPERSCRIPT TWO})")
        atmpressLabel.setToolTip("فشار جو")
        self.FoundationLoad_Part.addRow (atmpressLabel , self.Pa)

        qprimNetLabel = QLabel ("q' net(ton/m\N{SUPERSCRIPT TWO})")
        qprimNetLabel.setToolTip("بار خالص گسترده روی پی سطحی")
        self.FoundationLoad_Part.addRow (qprimNetLabel , self.qPrimNet)

        ebperbLabel = QLabel ("eᴮ/B")
        ebperbLabel.setToolTip("")
        self.FoundationLoad_Part.addRow (ebperbLabel , self.eBPerB)

        elperlLabel = QLabel ("eᴸ/L")
        elperlLabel.setToolTip("")
        self.FoundationLoad_Part.addRow (elperlLabel , self.eLPerL)
        self.FoundationLoad_Box.setLayout(self.FoundationLoad_Part)


        #-------------------------------------------------------------------


        #Sehmertmann:
        #t value for sehmertmann
        self.t_Sehmertmann =  QLineEdit()
        self.t_Sehmertmann.setValidator(QDoubleValidator())
        self.t_Sehmertmann.setPlaceholderText("year")
        self.t_Sehmertmann.setFixedWidth(85)

        self.t_Sehmertmann.textChanged.connect(self.enButton)
        
        #E value for sehmertmann
        self.E = QComboBox ()
        self.E.addItems(["Constant" ,"Func. of stress"])
        self.EValue = "Flexible"
        self.E.setFixedWidth(85)
        self.E.currentTextChanged.connect (self.EFunction)



        
        self.sehmertmann_Box = QGroupBox("SCHMERTMANN")
        self.sehmertmann_Box.setStyleSheet(boxesStyle)

        self.sehmertmann_Part = QFormLayout()
        self.sehmertmann_Part.addRow ("t(year)" , self.t_Sehmertmann)
        self.sehmertmann_Part.addRow ("E" , self.E)
        self.EValue = "Constant"
        self.sehmertmann_Box.setLayout(self.sehmertmann_Part)

        #----------------------------------------------------------------------

        #----------------------------------------------------------------------


        #----------------------------------------------------------------------


        #Consolidation :
        #S(3D/1D)
        # self.S3DPer1D =  QLineEdit()
        # self.S3DPer1D.setValidator(QDoubleValidator())
        # self.S3DPer1D.textChanged.connect(self.enButton)
        

        # self.consolidation_Box = QGroupBox("Consolidation")
        # self.consolidation_Part = QFormLayout()
        # self.consolidation_Part.addRow ("S(3D/1D):" , self.S3DPer1D)
        # self.consolidation_Box.setLayout(self.consolidation_Part)

        #----------------------------------------------------------------------


        #---------------------------------------------------------------------

        #SOIL CHARACTERISTICS
        tableColor = "#fafcff"
        itemTableColor = "#e6efff"
        tableHeaderColor = "#a6c6f7"
        tableTitleColor = "#146C94"

        self.soilChar = QLabel()
        self.soilChar.setText("SOIL CHARACTERISTICS :")  


        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(10)
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem('')
                self.tableWidget.setItem(i, j, item)
                if (j == 0 and i != 0 )or j == 2:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)


        for i in range(6):
            self.tableWidget.setColumnWidth(i , 75)
            
        self.tableWidget.setColumnWidth(5 , 130)
        self.tableWidget.setColumnWidth(6 , 95)
        for i in range(7 , 10):
            self.tableWidget.setColumnWidth(i , 48)

        
        self.tableWidget.setHorizontalHeaderLabels(["From\nElev.\n(m)", "To\nElev.\n(m)" , "Thickness\n(m)" , 
            u"\u03B3 wet\n(t/m\u00B3)" , u"\u03B3 sat\n(t/m\u00B3)" , "Analysis\nmethod" , "E\nformula" , u"E₀\n(t/m\u00B2)" , "r\n(t/m\u00B2/m)" , "v"])
        
        self.tableWidget.horizontalHeaderItem(0).setToolTip("تراز ابتدای لایه خاک")
        self.tableWidget.horizontalHeaderItem(1).setToolTip("تراز انتهای لایه خاک")
        self.tableWidget.horizontalHeaderItem(2).setToolTip("ضخامت لایه خاک")
        self.tableWidget.horizontalHeaderItem(3).setToolTip("وزن مخصوص خاک")
        self.tableWidget.horizontalHeaderItem(4).setToolTip("وزن مخصوص اشباع خاک")
        self.tableWidget.horizontalHeaderItem(5).setToolTip("روش تحلیل")
        self.tableWidget.horizontalHeaderItem(6).setToolTip("فرمول محاسبه مدول الاستیسیته لایه خاک")
        self.tableWidget.horizontalHeaderItem(7).setToolTip("مدول الاستیسیته لایه خاک")
        self.tableWidget.horizontalHeaderItem(8).setToolTip("")
        self.tableWidget.horizontalHeaderItem(9).setToolTip("ضریب پوآسون")

        
        self.tableWidget.itemChanged.connect(self.cellChangedHandeler)
        
        #######????????????????????????????????????
        # for j in range(0 , 9):
        #     self.tableWidget.openPersistentEditor(self.tableWidget.itemAt(25, 9))
        self.tableWidget.cellChanged.connect(self.enButton)
    

    


        self.analysisMethodInTable = [ QComboBox () , QComboBox () , QComboBox () , QComboBox () ]
        self.analysisMethodInTableValue = ["Schmertmann" , "Schmertmann" ,"Schmertmann" ,"Schmertmann" ]
        for i in range(4):
            self.analysisMethodInTable[i].addItems(["Schmertmann" ,"Elastic"])
            self.analysisMethodInTable[i].currentTextChanged.connect (self.analysisMethodInTableFunction)
            self.tableWidget.setCellWidget(i , 5 , self.analysisMethodInTable[i])


        self.EFormulaInTable = [ QComboBox () , QComboBox () , QComboBox () , QComboBox () ]
        self.EFormulaInTableValue = ["E0+r.z" , "E0+r.z" ,"E0+r.z" ,"E0+r.z" ]
        for i in range(4):
            self.EFormulaInTable[i].addItems(["E0+r.z" ,"E0(s/pa)^r" , "USER"])
            self.EFormulaInTable[i].currentTextChanged.connect (self.EFormulaInTableFunction)
            self.tableWidget.setCellWidget(i , 6 , self.EFormulaInTable[i])
        




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

        
        gridLayout.addWidget(self.foundationDimention_Box , 0 , 0 )
        gridLayout.addWidget(self.FoundationLoad_Box , 0 , 1 )
        gridLayout.addWidget(self.sehmertmann_Box , 0 , 2 )
        #gridLayout.addWidget(self.consolidation_Box , 1 , 2)


        ButtonLayout = QHBoxLayout()
        self.graphButtonFunction(ButtonLayout)
        self.resetButtonFunction(ButtonLayout)


        verticalLayout.addLayout(gridLayout)
        verticalLayout.addWidget(self.soilChar , alignment = Qt.AlignCenter) 
        verticalLayout.addWidget(self.tableWidget)

        
        verticalLayout.addLayout(ButtonLayout)
        self.whichRowsHasChanged = set()
        layout.addLayout(verticalLayout, 1, 0)
    

    def enButton(self):
        #TO DO : bayad check shavad ke row = 0 table filled bashad !
        if (self.B.text() == '' or self.L.text() == '' or self.Df.text() == '' or self.t.text() == '' or self.Efoundation.text() == '' or self.qPrimNet.text() == '' or self.eBPerB.text() == '' or self.eLPerL.text() == '' or self.t_Sehmertmann.text() == '' or self.Pa.text() == '' or self.G_W_L.text() == ''):
            self.Button.setEnabled(False)
        else :
            self.Button.setEnabled(True)
        
        
    def graphButtonFunction (self , layout):
        self.Button = QPushButton ("Calculation" , self)
        self.Button.clicked.connect (self.calcFromElev)
        self.Button.clicked.connect (self.calcThickness)
        
        self.Button.clicked.connect(self.result)
        self.Button.setEnabled(False)
        layout.addWidget(self.Button, alignment = Qt.AlignLeft)
        
    
    def resetButtonFunction(self , layout):
        self.resetButton = QPushButton ("Reset" , self)
        self.resetButton.clicked.connect(self.resetAll)
        #self.resetButton.setEnabled(True)
        layout.addWidget(self.resetButton ,alignment = Qt.AlignRight)

    def resetAll(self):
        theInputs = [self.B , self.L , self.Df ,self.t , self.Efoundation , self.qPrimNet , self.eBPerB , self.eLPerL ,self.gammaWat , self.Pa , self.t_Sehmertmann , self.G_W_L]
        

        for inp in theInputs:
            inp.clear()

        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(r , c , QTableWidgetItem(''))



        self.Button.setEnabled(False)

    def inputError(self , theInput):
        error_dialog = QErrorMessage()
        error_dialog.showMessage(" مقدار" + theInput + "نامعتبر است " )
        error_dialog.exec_()


    def IfFunction (self , s ):
        if (s == "Fox 1948"):
            self.IfValue = "Fox 1948"
        elif (s == u"Mayne & Polous"):
            self.IfValue = u"Mayne & Polous"


    def FoundationRigidityFunction (self , s ):
        if (s == "Flexible"):
            self.FoundationRigidityValue = "Flexible"
        elif (s == "Rigid"):
            self.FoundationRigidityValue = "Rigid"
        elif (s == "Intermediate"):
            self.FoundationRigidityValue = "Intermediate"

        

    def EFunction ( self , s):
        if (s == "Constant"):
            self.EValue = "Constant"
        else :
            self.EValue = "Func. of stress"

    def numberOfLayersFunction(self , s):
        if (s == "1"):
            self.numberOfLayersValue = "1"
        elif (s == "2"):
            self.numberOfLayersValue = "2"
        elif (s == "3"):
            self.numberOfLayersValue = "3"
        elif (s == "4"):
            self.numberOfLayersValue = "4"


    def analysisMethodInTableFunction (self , s):
        for i in range (0 , 4):
            self.analysisMethodInTableValue[i] = self.analysisMethodInTable[i].currentText()
    
    def EFormulaInTableFunction (self , s):
        for i in range (0 , 4):
            self.EFormulaInTableValue[i] = self.EFormulaInTable[i].currentText()
    
    def calcFromElev (self):
        for i in range(2 , 5):
            if i <= int(self.numberOfLayersValue) and self.tableWidget.item(i-2 ,1) :
                self.tableWidget.setItem(i-1 , 0 , QTableWidgetItem(self.tableWidget.item(i-2 ,1).text()))
            else :
                self.tableWidget.setItem(i-1 , 0 , QTableWidgetItem(str("-")))

    def calcThickness (self):
        for i in range(1 , 5):
            if i < int(self.numberOfLayersValue) and self.tableWidget.item(i-1 ,0) and self.tableWidget.item(i-1 ,1) :
                self.tableWidget.setItem(i-1 , 2 , QTableWidgetItem(str(float(self.tableWidget.item(i-1 ,0).text()) - float(self.tableWidget.item(i-1 ,1).text()))))
            elif i == int(self.numberOfLayersValue) and self.tableWidget.item(i-1 ,0) and self.tableWidget.item(i-1 ,1) :
                self.tableWidget.setItem(i-1 , 2 , QTableWidgetItem(str(float("inf"))))
            else :
                self.tableWidget.setItem(i-1 , 2 , QTableWidgetItem(str("-")))

    def baseElev (self):
        return(float(self.tableWidget.item(0 , 0).text()) - float(self.Df.text()))

    def Beq (self):
        try :
            return math.sqrt(float(self.B.text()) * float(self.L.text()) *4 /math.pi )
        except:
            if float(self.B.text()) < 0 :
                raise Exception("B")
            if float(self.L.text()) < 0 : 
                raise Exception("L")

        
    def InflElev (self):
        if float(self.L.text())/float(self.B.text()) > 5 :
            return (self.baseElev() - 4 * float(self.B.text()))
        else:
            try:
                if float(self.L.text())/float(self.B.text()) >= 1 :
                    return (self.baseElev() - ((float(self.L.text())/float(self.B.text())-1)*float(self.B.text())/2 + 2*float(self.B.text()) ))
            except:
                raise Exception("B")
            else:
                raise Exception("B > L")

    
    def qPrimTotal (self):
        if (float(self.G_W_L.text()) <= self.baseElev() ):
            return (float(self.qPrimNet.text()) + float(self.tableWidget.item(0 , 3).text())*float(self.Df.text()))
        else :
            if (float(self.G_W_L.text()) >  float(self.tableWidget.item(0 , 0).text())):
                return (float(self.qPrimNet.text()) + (float(self.tableWidget.item(0 , 4).text())-float(self.gammaWat.text())) * float(self.Df.text()))
            else :
                return float(self.qPrimNet.text()) + float(self.tableWidget.item(0 , 3).text())*(float(self.tableWidget.item(0 , 0).text()) - float(self.G_W_L.text())) + (float(self.tableWidget.item(0 , 4).text()) - float(self.gammaWat.text()))*(float(self.G_W_L.text())- self.baseElev())

    def calcqPrim (self):
        return self.qPrimTotal() - float(self.qPrimNet.text())
    
    def Qnet(self):
        return float(self.qPrimNet.text()) * float(self.B.text()) * float(self.L.text())

    def QTotal (self):
        return self.qPrimTotal() * float(self.B.text()) * float(self.L.text())
    
    def qTotalst (self):
        try:
            if float(self.L.text())/float(self.B.text()) >= 3 :
                return self.QTotal()/float(self.L.text()) 
            else :
                return 0
        except:
            raise Exception ("L")
    

    def calcIf (self):
        try:
            if self.IfValue == "Fox 1948" :
                top = (1.432 * math.pow(float(self.L.text())/float(self.B.text()) , -0.69) * math.pow(float(self.Df.text())/float(self.B.text()) , 2))
                down = 2*1.432*math.pow(float(self.L.text())/float(self.B.text()) , -0.69) * math.pow(float(self.Df.text())/float(self.B.text()) , 2) + 1.333 * float(self.Df.text())/float(self.B.text()) + 1
                return ( 1 -  (top / down) + (2 * float(self.tableWidget.item(0 , 9).text())-1)/8 )
            else :
                if float(self.Df.text()) == 0:
                    return 1 
                else :
                    return (1 -(1 / (3.5 * math.pow(math.e ,(1.22 * float(self.tableWidget.item(0 , 9).text())-0.4)) * (1.6 + self.Beq()/float(self.Df.text())))))
        except :
            if float(self.B.text()) < 0 :
                raise Exception("B")
            if float(self.L.text()) < 0 : 
                raise Exception("L")
    #calculation of immediate elastic settlement 
    #layer char table
    def layerNumber (self):
        arr = []
        for i in range(1, 5):
            if i <= int(self.numberOfLayersValue) :
                arr.append(i)
            else:
                arr.append(0)
        return arr

    def H (self):
        layerNumber = self.layerNumber()

        arr = []
        for i in range (1 , 5):
            if (layerNumber[i-1] != 0):

                if (i != int(self.numberOfLayersValue) and i == 1) :
                    arr.append(float(self.tableWidget.item( i-1 , 2 ).text()) - float(self.Df.text()))
                
                else:
                    arr.append(float(self.tableWidget.item( i-1 , 2 ).text()))
            else :
                arr.append(0)

        return arr
    
    def sigmaH (self):
        arr = []
        H = self.H()

        if H[0] == float("inf") :
            arr.append(float("inf"))
        else :
            arr.append(H[0])



        if H[1] == 0 :
            arr.append(0)
        else :
            if H[1] == float("inf"):
                arr.append(float("inf"))
            else:
                arr.append(H[0] + H[1])



        if H[2] == 0 :
            arr.append(0)
        else :
            if H[2] == float("inf"):
                arr.append(float("inf"))
            else:
                arr.append(H[0] + H[1] + H[2])



        if H[3] == 0 :
            arr.append(0)
        else :
            if H[3] == float("inf"):
                arr.append(float("inf"))
            else:
                arr.append(H[0] + H[1] + H[2] + H[3])

        return arr

        

    def checkWhichRowsChanged (self):
        theMax = max(self.whichRowsHasChanged)
        colCount = self.tableWidget.columnCount()
        for row in range(0 , theMax+1):
            for col in range(0 , colCount):
                if self.tableWidget.item(row , col).text() == '':
                    self.tableWidget.setItem(row , col , QTableWidgetItem('0'))


    #Rectangular Base and Center 
    def BPrim (self , coff_B ):
        return (float(self.B.text()) * coff_B)
    
    def LPrim (self , coff_L):
        return (float(self.L.text()) * coff_L)
    
    def M (self , BPrim , LPrim):
        arr = []
        try:
            for i in range(1 , 5):
                if (i <= int(self.numberOfLayersValue)):
                    arr.append(LPrim / BPrim)
                else :
                    arr.append(0)
            return arr
        except:
            raise Exception('B')
        

    def N (self , BPrim):
        arr = []
        try:
            sigmaH = self.sigmaH()
            for i in range(1 , 5):
                if (i < int(self.numberOfLayersValue)):
                    arr.append(sigmaH[i-1] / BPrim)
                else :
                    if (i == int(self.numberOfLayersValue)):
                        arr.append(float("inf"))
                    else:
                        arr.append(0)
            return arr
        except:
            raise Exception('B')
    


    def I1 (self , BPrim , LPrim):
        try:
            N = self.N(BPrim)
            M = self.M(BPrim , LPrim)

            arr = []
            for i in range(1 , 5):

                if i > int(self.numberOfLayersValue) :
                    arr.append(0)

                elif N[i-1] == float("inf") :



                    top1 = math.sqrt(1+M[i-1]**2+(1000*M[i-1])**2)+M[i-1] 
                    down1 = (math.sqrt(1+M[i-1]**2+(1000*M[i-1])**2)-M[i-1])
                    top2 = (math.sqrt(1+M[i-1]**2+(1000*M[i-1])**2)+1)
                    down2 = (math.sqrt(1+M[i-1]**2+(1000*M[i-1])**2)-1)
                    arr.append( (1/math.pi)*(math.log( top1/down1 , math.e) + M[i-1]*math.log( top2/down2 , math.e) ))

                else :
                    top1 = math.sqrt(1+M[i-1]**2+(N[i-1])**2)+M[i-1] 
                    down1 = (math.sqrt(1+M[i-1]**2+(N[i-1])**2)-M[i-1])

                    top2 = (math.sqrt(1+M[i-1]**2+(N[i-1])**2)+1)
                    down2 = (math.sqrt(1+M[i-1]**2+(N[i-1])**2)-1)
                    arr.append( (1/math.pi)*(math.log( top1/down1 , math.e) + M[i-1]*math.log( top2/down2 , math.e) ))


            return arr

        except:
            raise Exception('m or n')

    def I2 (self , BPrim , LPrim):
        try:
            N = self.N(BPrim)
            M = self.M(BPrim , LPrim)

            arr = []
            for i in range(1 , 5):
                if i > int(self.numberOfLayersValue) :
                    arr.append(0)
                elif N[i-1] == float("inf") :
                    arr.append(0)
                else :
                    arr.append( (N[i-1]/math.pi)*math.atan(M[i-1]/(N[i-1]*math.sqrt(1+M[i-1]**2+N[i-1]**2))) )
            return arr
        except:
            raise Exception('m or n')



    def Is(self , BPrim , LPrim):
        try:
            I1 = self.I1( BPrim , LPrim)
            I2 = self.I2( BPrim , LPrim)
            arr = []
            for i in range(1 , 5):
                if i <= int(self.numberOfLayersValue):
                    arr.append(I1[i-1]+ (I2[i-1] * (1-2*float(self.tableWidget.item(i-1 , 9).text())))/(1-float(self.tableWidget.item(i-1 , 9).text())))
                else:
                    arr.append(0)
            return arr
        except:
            raise Exception('v')
    
    def S1 (self , BPrim , LPrim , theType):
        try:    
            Is = self.Is( BPrim , LPrim)
            If = self.calcIf()
            arr = []
            for i in range(1 , 5):
                if i > int(self.numberOfLayersValue) :
                    arr.append(0)
                else :
                    if self.analysisMethodInTableValue[i-1] == "Schmertmann" :
                        arr.append(0)

                    else :
                        if theType == "center":
                            arr.append(float(self.qPrimNet.text()) * Is[i-1] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2 )) * 100 * 4 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "corner":
                            arr.append(float(self.qPrimNet.text()) * Is[i-1] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2 )) * 100 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "b/2":
                            arr.append(float(self.qPrimNet.text()) * Is[i-1] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2 )) * 100 * 2 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "l/2":
                            arr.append(float(self.qPrimNet.text()) * Is[i-1] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2 )) * 100 * 2 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        
            return arr
        except:
            raise Exception('E0(1)')

    
    def S2 (self , BPrim , LPrim , theType):
        try:
            arr =[0]
            Is = self.Is( BPrim , LPrim)
            If = self.calcIf()

            for i in range(2 , 5):
                if i > int(self.numberOfLayersValue) :
                    arr.append(0)
                else :
                    if self.analysisMethodInTableValue[i-1] == "Schmertmann" :
                        arr.append(0)
                    else :
                        if theType == "center":
                            arr.append(float(self.qPrimNet.text()) * Is[i-2] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2)) * 100 * 4 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "corner":
                            arr.append(float(self.qPrimNet.text()) * Is[i-2] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2)) * 100 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "b/2":
                            arr.append(float(self.qPrimNet.text()) * Is[i-2] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2)) * 100 * 2 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )
                        if theType == "l/2":
                            arr.append(float(self.qPrimNet.text()) * Is[i-2] * If * (1-math.pow(float(self.tableWidget.item(i-1 , 9).text()), 2)) * 100 * 2 * BPrim / float(self.tableWidget.item(i-1 , 7).text()) )

            return arr
        except:
            raise Exception('E0(2)')

        
    def deltaS (self , BPrim , LPrim , theType):
        arr = []
        S1 = self.S1 (BPrim , LPrim , theType)
        S2 = self.S2 (BPrim , LPrim , theType)

        for i in range(1 , 5):
            if i <= int(self.numberOfLayersValue) :
                arr.append(-S1[i-1] + S2[i-1])
            else :
                arr.append(0)
        return arr

    def sigmaDeltaS(self , BPrim , LPrim , theType):
        return sum(self.deltaS( BPrim , LPrim , theType))  

    def Sce (self):
        theType = 'center'
        b = self.BPrim (1/2)
        l = self.LPrim (1/2)
        m = self.M (b , l)
        n = self.N (b)
        i1 = self.I1 (b , l)
        i2 = self.I2 (b , l)
        i_s = self.Is (b , l)
        s1 = self.S1 (b , l , theType)
        s2 = self.S2 (b , l , theType)

        return self.sigmaDeltaS(b , l , theType)
    
    def Sco (self):
        theType = 'corner'
        b = self.BPrim (1)
        l = self.LPrim (1)
        m = self.M (b , l)
        n = self.N (b)
        i1 = self.I1 (b , l)
        i2 = self.I2 (b , l)
        i_s = self.Is (b , l)
        s1 = self.S1 (b , l , theType)
        s2 = self.S2 (b , l , theType)

        return self.sigmaDeltaS(b , l , theType)

    def SbdivBy2 (self):
        theType = 'b/2'
        b = self.BPrim (1/2)
        l = self.LPrim (1)
        m = self.M (b , l)
        n = self.N (b)
        i1 = self.I1 (b , l)
        i2 = self.I2 (b , l)
        i_s = self.Is (b , l)
        s1 = self.S1 (b , l , theType)
        s2 = self.S2 (b , l , theType)

    

        return self.sigmaDeltaS(b , l , theType)
    
    def SldivBy2 (self):
        theType = 'l/2'
        b = self.BPrim (1)
        l = self.LPrim (1/2)
        m = self.M (b , l)
        n = self.N (b)
        i1 = self.I1 (b , l)
        i2 = self.I2 (b , l)
        i_s = self.Is (b , l)
        s1 = self.S1 (b , l , theType)
        s2 = self.S2 (b , l , theType)




        return self.sigmaDeltaS(b , l , theType)

    def C1 (self):
        try:
            return (1 - 0.5 * self.calcqPrim()/float(self.qPrimNet.text()))
        except:
            raise Exception('q\'net')
    
    def C2 (self):
        try:
            return (1 + 0.2 * math.log(float(self.t_Sehmertmann.text())/0.1 , 10))
        except:
            raise Exception('t')   





    def deltaH (self):
        return (4 * float(self.B.text()) / 40)

    def existFactor (self):
        try:
            arr = []
            for i in range (1 , 5):
                if (i <= int(self.numberOfLayersValue)):
                    if self.analysisMethodInTableValue[i-1] == "Schmertmann":
                        arr.append(2 - 1)
                    else :
                        arr.append(2 - 2)
                else :
                    arr.append(0)

            return arr
        except:
            raise Exception('ExistFactor')


    #Last Table to calculate :
    def H_table(self):
        arr = []
        be = self.baseElev()
        dh = self.deltaH()
        for i in range(0 , 41):
            arr.append(be - i *dh)
        return arr




    def layerNumber_table(self):
        H = self.H_table ()
        arr = []
        for i in range(0 , 41):
            for j in range (0 , 4):
                if float(self.tableWidget.item(j , 0).text()) > H[i] and  H[i] > float(self.tableWidget.item(j , 1).text()) :
                    arr.append(j+1)
                    break

        return arr


    def top_table(self):
        lyrNo = self.layerNumber_table()
        arr = []
        for i in range(0 , 41):
            arr.append(float(self.tableWidget.item(lyrNo[i]-1 , 0).text()))
        return arr

    def existFactor_table(self):
        exFa = self.existFactor ()
        arr = []
        ln = self.layerNumber_table()
        for i in range(0 , 41):
            arr.append(exFa[ln[i]-1])
        return arr



    def gammaWet_table(self):
        lyrNo = self.layerNumber_table()
        arr = []
        for i in range(0 , 41):
            arr.append(float(self.tableWidget.item(lyrNo[i]-1 , 3).text()))
        return arr

    def gammaSat_table(self):
        lyrNo = self.layerNumber_table()
        arr = []
        for i in range(0 , 41):
            arr.append(float(self.tableWidget.item(lyrNo[i]-1 , 4).text()))
        return arr

    def gammaMean_table(self):
        arr = [0]
        H = self.H_table()
        dh = self.deltaH()
        gammaSat = self.gammaSat_table()
        gammaWet = self.gammaWet_table()
        for i in range(1 , 41):
            if float(self.G_W_L.text()) >= H[i-1] : 
                arr.append(gammaSat[i]-float(self.gammaWat.text()))
                continue
            if float(self.G_W_L.text()) < H[i] :
                arr.append(gammaWet[i])
                continue
            else :
               arr.append((gammaWet[i] * math.pow(H[i-1]-float(self.G_W_L.text())  , 2) + 2 * gammaWet[i] * (H[i-1] - float(self.G_W_L.text())) * (float(self.G_W_L.text()) - H[i]) + (gammaSat[i]-float(self.gammaWat.text())) * math.pow(float(self.G_W_L.text()) - H[i] , 2) )/ math.pow(dh , 2) )
        return arr

    def Pprim0_table (self):
        arr = [self.calcqPrim()]
        gammaMean = self.gammaMean_table()
        dH = self.deltaH()
        for i in range(1 , 41):
            arr.append(arr[i-1] + gammaMean[i] * dH)
        return arr
    
    def formula_table(self):
        arr = []
        lyrNo = self.layerNumber_table()
        for i in range( 0 , 41):
            if self.EFormulaInTableValue[lyrNo[i]-1] == "E0+r.z" :
                arr.append(1)
            elif self.EFormulaInTableValue[lyrNo[i]-1] == "E0(s/pa)^r" :
                arr.append(2)
            else :
                arr.append(3)
        return arr

    def E0_table(self):
        arr = []
        lyrNo = self.layerNumber_table()
        for i in range(0 , 41):
            arr.append(float(self.tableWidget.item(lyrNo[i]-1 , 7).text()))
        return arr
    
    def r_table(self):
        arr = []
        lyrNo = self.layerNumber_table()
        for i in range(0 , 41):
            arr.append(float(self.tableWidget.item(lyrNo[i]-1 , 8).text()))
        return arr

    def E_table(self):
        formula = self.formula_table()
        arr = []
        E0 = self.E0_table()
        r = self.r_table()
        top = self.top_table()
        H = self.H_table()
        pprim = self.Pprim0_table()
        try:
            for i in range(0 , 41):
                if formula[i] == 1:
                    arr.append(E0[i]+r[i]*(top[i]-H[i]))
                elif formula[i] == 2:
                    arr.append(E0[i] * math.pow(pprim[i]/float(self.Pa.text()) , r[i]))
                else :
                    arr.append(E0[i])
            return arr
        except:
            raise Exception ("Pa")


    def deltaqPrim_table(self):
        arr = [float(self.qPrimNet.text())]
        H = self.H_table()
        for i in range (1 , 41):
            arr.append( arr[0] * math.pow(float(self.B.text()) , 2) / math.pow(float(self.B.text())+H[0]-H[i] , 2))
        return arr

    def Ed_table(self):
        try:
            arr = []
            E = self.E0_table()
            p0prim = self.Pprim0_table()
            deltaq = self.deltaqPrim_table()

            for i in range (0 , 41):
                if self.EValue == "Constant":
                    arr.append(E[i])
                else :
                    arr.append(E[i] * math.sqrt((p0prim[i] + deltaq[i])/p0prim[i]))
            return arr
        except:
            raise Exception ("p0\'")

    def Izp(self):
        
        sigma = self.Pprim0_table()[5] + self.deltaqPrim_table()[5]
        try:
            return ( 0.5 + 0.1 * math.sqrt(float(self.qPrimNet.text())/sigma) ) 
        except:
            raise Exception ("q\'net")
    

    def I2_table (self):
        I2 = self.Izp()
        arr = []
        H = self.H_table()
        for i in range(0 , 41):
            if H[i] >= (self.baseElev() - (float(self.B.text())/2)):
                arr.append(0.1 + (I2-0.1)/(0.5*float(self.B.text())) * (self.baseElev() - H[i]))
            elif H[i] >= self.baseElev() - 2*float(self.B.text()):
                arr.append(I2 - (I2/(1.5*float(self.B.text())))*(self.baseElev()-H[i]-float(self.B.text())/2) )
            else :
                arr.append(0)
        return arr
    

    def deltaS_table (self):
        arr = [0]
        extFac = self.existFactor_table()
        Iz = self.I2_table ()
        Ed = self.Ed_table()

        for i in range (1 , 41):
            delta = 0.5 * (extFac[i]+extFac[i-1]) * self.C1() * self.C2() * float(self.qPrimNet.text()) * self.deltaH() * (Iz[i] + Iz[i-1])/(Ed[i] + Ed[i-1]) * 100
            arr.append(delta)
        return arr

    def deltaqPrimSTRP (self):
        arr = [float(self.qPrimNet.text())]
        deltaqPrim0 = self.deltaqPrim_table()[0]
        H = self.H_table()

        for i in range (1 , 41):
            arr.append(deltaqPrim0 * math.pow(float(self.B.text()) , 2) * 10 / ((float(self.B.text()) + H[0] - H[i])*(10*float(self.B.text()) + H[0] - H[i])))
        return arr

    def EdSTRP (self):
        return (self.Ed_table())
    
    def I2STRP (self):
        sigma = self.Pprim0_table()[10] + self.deltaqPrim_table()[10]
        I2p = ( 0.5 + 0.1 * math.sqrt(self.C1()/sigma)) 

        arr = []
        H = self.H_table()
        for i in range(0 , 41):
            if H[i] >= (self.baseElev() - float(self.B.text())):
                arr.append(0.2 + (I2p-0.2)/float(self.B.text()) * (self.baseElev() - H[i]))
            elif H[i] >= self.baseElev() - 4*float(self.B.text()):
                arr.append(I2p - (I2p/(3*float(self.B.text())))*(self.baseElev()-float(self.B.text())-H[i]) )
            else :
                arr.append(0)
        return arr
    
    def deltaSSTRP (self):
        arr = [0]
        extFac = self.existFactor_table()
        Iz = self.I2STRP ()
        Ed = self.EdSTRP()

        for i in range (1 , 41):
            #print(i , (extFac[i]+extFac[i-1]) ,  "\t" , self.C1() ,'\t', self.C2() ,'\t' ,float(self.qPrimNet.text()) , '\t' , self.deltaH() , '\t' , (Iz[i] + Iz[i-1]) , '\n')
            delta = 0.5 * (extFac[i]+extFac[i-1]) * self.C1() * self.C2() * float(self.qPrimNet.text()) * self.deltaH() * (Iz[i] + Iz[i-1])/(Ed[i] + Ed[i-1]) * 100
            arr.append(delta)
        return arr

    def Saxi (self):
        delta = self.deltaS_table()
        return (sum(delta))
    
    def Sstrp(self):
        delta = self.deltaSSTRP()
        return (sum(delta))

    def Srect(self):
        Sax = self.Saxi()
        Sstr = self.Sstrp()

        return (Sax + ((float(self.B.text())/float(self.L.text())) -1)*(Sstr - Sax)/9 )


    def cellChangedHandeler(self, item):
        self.whichRowsHasChanged.add(item.row())



    def result (self):  
        #self.checkWhichRowsChanged()
        try:
            resultWindow = QDialog(self)
            resultWindow.setWindowTitle("Results")
            
            
            
            title1 = QLabel()
            title1.setText("Elastic settlement: " )  
            table1 = QTableWidget()

            table1.setRowCount(7)
            table1.setColumnCount(3)
            #table1.setFixedSize(190 , 215)
            table1.setHorizontalHeaderLabels(["Flexible" ,"Rigid", "Intermediate"])
            table1.setVerticalHeaderLabels(["I(R)" , "I(ave)" , "Center" , "Corner" , "Mid. of B Edge" , "Mid. of L Edge" , "Average"])
            Flexible_values = [round(1,3) , round(0.848,3) , round(self.Sce(),3) , round(self.Sco(),3) , round(self.SbdivBy2(),3) , round(self.SldivBy2(),3) , round((self.Sce()* 0.848),3)]
            Rigid_values = [round(math.pi/4,3) , round(1,3) , round(math.pi/4*self.Sce(),3) , round(math.pi/4*self.Sce(),3) , round(math.pi/4*self.Sce(),3) , round(math.pi/4*self.Sce(),3) , round(math.pi/4*self.Sce(),3)]
            
            Inter_0 = math.pi/4 + 1/((1/(1-math.pi/4))+10*(float(self.Efoundation.text()))/float(self.tableWidget.item(0 , 7).text())* math.pow(2*float(self.t.text())/self.Beq() , 3))
            Inter_1 = Rigid_values[1] + (Inter_0 - Rigid_values[0])*(Flexible_values[1] - Rigid_values[1])/(Flexible_values[0] - Rigid_values[0])
            Inter_2 = Rigid_values[0]*self.Sce() + (self.Sce() - Rigid_values[0]*self.Sce())*(Inter_0 - Rigid_values[0] )/(Flexible_values[0] - Rigid_values[0])
            Inter_3 = Rigid_values[0]*self.Sce() + (self.Sco() - Rigid_values[0]*self.Sce())*(Inter_0 - Rigid_values[0] )/(Flexible_values[0] - Rigid_values[0])
            Inter_4 = Rigid_values[0]*self.Sce() + (self.SbdivBy2() - Rigid_values[0]*self.Sce())*(Inter_0 - Rigid_values[0] )/(Flexible_values[0] - Rigid_values[0])
            Inter_5 = Rigid_values[0]*self.Sce() + (self.SldivBy2() - Rigid_values[0]*self.Sce())*(Inter_0 - Rigid_values[0] )/(Flexible_values[0] - Rigid_values[0])
            Inter_6 = Inter_1 * Inter_2



            Intermediate_values = [round(Inter_0,3) , round(Inter_1,3) , round(Inter_2,3) , round(Inter_3,3)  , round(Inter_4,3) , round(Inter_5,3) , round(Inter_6,3)]

            
            for i in range(len(Flexible_values)):
                table1.setItem(i , 0 , QTableWidgetItem(str(Flexible_values[i])))
            for i in range(len(Rigid_values)):
                table1.setItem(i , 1 , QTableWidgetItem(str(Rigid_values[i])))
            
            for i in range(len(Intermediate_values)):
                table1.setItem(i , 2 , QTableWidgetItem(str(Intermediate_values[i])))
            

            self.selectedColInElasticSettTable(table1)



            title2 = QLabel()
            title2.setText("Elastic Rotational sett. for e(B) ")  
            table2= QTableWidget()

            table2.setRowCount(6)
            table2.setColumnCount(1)
            #table1.setFixedSize(190 , 215)
            table2.horizontalHeader().setVisible(False)
            table2.setVerticalHeaderLabels(["I\u03F4(Rig)" , "I\u03F4(Flx)" , "I\u03F4(int)" , "I\u03F4" , "tg \u03F4" , "S(rot)" ])
                
            tab2_0 = 16/(math.pi*(1+0.22*float(self.L.text())/float(self.B.text())))
            tab2_1 = 12.027/(math.pi*(1+0.26*float(self.L.text())/float(self.B.text())))
            tab2_2 = tab2_1 + (Inter_0 - 1)* (tab2_0 - tab2_1)/(math.pi/4 - 1)
            if self.FoundationRigidityValue == "Flexible":
                tab2_3 = tab2_1
            elif self.FoundationRigidityValue == "Rigid":
                tab2_3 = tab2_0
            elif self.FoundationRigidityValue == "Intermediate":
                tab2_3 = tab2_2
            tab2_4 = float(self.qPrimNet.text()) * float(self.eBPerB.text()) * tab2_3 * (1 - math.pow(float(self.tableWidget.item(0 , 9).text()) , 2))/float(self.tableWidget.item(0 , 7).text())
            tab2_5 = tab2_4 * 50 * float(self.B.text())



            table2_values = [round(tab2_0,3),round(tab2_1,3),round(tab2_2,3),round(tab2_3,3),round(tab2_4,3),round(tab2_5,3)]
            for i in range(len(table2_values)):
                table2.setItem(i , 0 , QTableWidgetItem(str(table2_values[i])))
            


            title3 = QLabel()
            title3.setText("Elastic Rotational sett. for e(L) ")  
            table3= QTableWidget()

            table3.setRowCount(6)
            table3.setColumnCount(1)
            #table1.setFixedSize(190 , 215)
            table3.horizontalHeader().setVisible(False)
            table3.setVerticalHeaderLabels(["I\u03F4(Rig)" , "I\u03F4(Flx)" , "I\u03F4(int)" , "I\u03F4" , "tg \u03F4" , "S(rot)" ])
            

            tab3_0 = 16/(math.pi*(1+0.22*float(self.L.text())/float(self.B.text())))
            tab3_1 = 12.027/(math.pi*(1+0.26*float(self.L.text())/float(self.B.text())))
            tab3_2 = tab3_1 + (Inter_0 - 1)* (tab3_0 - tab3_1)/(math.pi/4 - 1)
            if self.FoundationRigidityValue == "Flexible":
                tab3_3 = tab3_1
            elif self.FoundationRigidityValue == "Rigid":
                tab3_3 = tab3_0
            elif self.FoundationRigidityValue == "Intermediate":
                tab3_3 = tab3_2
            tab3_4 = float(self.qPrimNet.text()) * float(self.eLPerL.text()) * tab3_3 * (1 - math.pow(float(self.tableWidget.item(0 , 9).text()) , 2))/float(self.tableWidget.item(0 , 7).text())
            tab3_5 = tab3_4 * 50 * float(self.L.text())

            table3_values = [round(tab3_0,3),round(tab3_1,3),round(tab3_2,3),round(tab3_3,3),round(tab3_4,3),round(tab3_5,3)]
            
            for i in range(len(table3_values)):
                table3.setItem(i , 0 , QTableWidgetItem(str(table3_values[i])))
            

                    
            title4 = QLabel()
            title4.setText("Elastic settl. + Rot. (cm) ")  
            table4= QTableWidget()

            table4.setRowCount(5)
            table4.setColumnCount(1)
            #table1.setFixedSize(190 , 215)
            table4.horizontalHeader().setVisible(False)
            table4.setVerticalHeaderLabels(["Center" , "Corner" , "Mid. of B Edge" , "Mid. of L Edge" , "Average" ])
            
            if self.FoundationRigidityValue == "Flexible":
                tab4_0 = Flexible_values[2]
            elif self.FoundationRigidityValue == "Rigid":
                tab4_0 = Rigid_values[2]
            elif self.FoundationRigidityValue == "Intermediate":
                tab4_0 = Intermediate_values[2]
        #############
            if self.FoundationRigidityValue == "Flexible":
                tab4_1 = Flexible_values[3] + table3_values[5] + table2_values[5]
            elif self.FoundationRigidityValue == "Rigid":
                tab4_1 = Rigid_values[3] + table3_values[5] + table2_values[5]
            elif self.FoundationRigidityValue == "Intermediate":
                tab4_1 = Intermediate_values[3] + table3_values[5] + table2_values[5]
        ##############
            if self.FoundationRigidityValue == "Flexible":
                tab4_2 = Intermediate_values[4] + table3_values[5] 
            elif self.FoundationRigidityValue == "Rigid":
                tab4_2 = Rigid_values[4] + table3_values[5] 
            elif self.FoundationRigidityValue == "Intermediate":
                tab4_2 = Intermediate_values[4] + table3_values[5] 
        ###############
            if self.FoundationRigidityValue == "Flexible":
                tab4_3 = Intermediate_values[5] + table2_values[5] 
            elif self.FoundationRigidityValue == "Rigid":
                tab4_3 = Rigid_values[5] + table2_values[5] 
            elif self.FoundationRigidityValue == "Intermediate":
                tab4_3 = Intermediate_values[5] + table2_values[5] 
        #############
            if self.FoundationRigidityValue == "Flexible":
                tab4_4 = Intermediate_values[6] 
            elif self.FoundationRigidityValue == "Rigid":
                tab4_4 = Rigid_values[6] 
            elif self.FoundationRigidityValue == "Intermediate":
                tab4_4 = Intermediate_values[6] 

            
            

        
            
            
            
            
            
            table4_values = [round(tab4_0,3) , round(tab4_1,3), round(tab4_2,3) ,round(tab4_3,3) ,round(tab4_4,3) ]
            for i in range(len(table4_values)):
                table4.setItem(i , 0 , QTableWidgetItem(str(table4_values[i])))

        
            title5 = QLabel()
            title5.setText("Imm Setll.(Schm) (cm)")  
            table5= QTableWidget()
            table5.setRowCount(3)
            table5.setColumnCount(1)
            #table1.setFixedSize(190 , 215)
            table5.horizontalHeader().setVisible(False)
            table5.setVerticalHeaderLabels(["S(axi)" , "S(strp)" ,"S(rect)"])






            table5_values = [round(self.Saxi(),3) , round(self.Sstrp(),3) , round(self.Srect(),3) ]
            for i in range(len(table5_values)):
                table5.setItem(i , 0 , QTableWidgetItem(str(table5_values[i])))

            RowsTables = QVBoxLayout()
            resultWindowLayout1 = QGridLayout()
            resultWindowLayout2 = QGridLayout()
            resultWindow.setLayout(RowsTables)


            


            resultWindowLayout1.addWidget(title1, 0 , 0 , alignment = Qt.AlignCenter)
            resultWindowLayout1.addWidget(table1 , 1 , 0)

            resultWindowLayout1.addWidget(title5, 0 , 1 , alignment = Qt.AlignCenter)
            resultWindowLayout1.addWidget(table5 , 1 , 1 )



            resultWindowLayout2.addWidget(title2, 0 , 0 , alignment = Qt.AlignCenter)
            resultWindowLayout2.addWidget(table2 , 1 , 0)
        
            resultWindowLayout2.addWidget(title3, 0 , 1 , alignment = Qt.AlignCenter)
            resultWindowLayout2.addWidget(table3 , 1 , 1)

            resultWindowLayout2.addWidget(title4, 0 , 2 , alignment = Qt.AlignCenter)
            resultWindowLayout2.addWidget(table4 , 1 , 2)
            
            RowsTables.addLayout(resultWindowLayout1)
            RowsTables.addLayout(resultWindowLayout2)



            resultWindow.exec()
        except Exception as e:
       
            self.inputError(str(e))






    def selectedColInElasticSettTable (self , table1 ):
        if self.FoundationRigidityValue == "Flexible":
            for i in range(0 , table1.rowCount()):
                table1.item(i,0).setBackground(QColor(58 , 175 ,9 ))
        elif self.FoundationRigidityValue == "Rigid":
            for i in range(0 , table1.rowCount()):
                table1.item(i,1).setBackground(QColor(58 , 175 ,9 ))
        elif self.FoundationRigidityValue == "Intermediate":
            for i in range(0 , table1.rowCount()):
                table1.item(i,2).setBackground(QColor(58 , 175 ,9 ))                  


    def module4HelpFunction(self):
        
        image_label = QLabel()
        message_box = QMessageBox()

        about = "شما در حال استفاده از ماژول محاسبات نشست آنی از نرم افزار GeOnion هستید."
        about2 = "زمانی که خاک زیر فونداسیون تحت بارگذاری قرار می‌گیرد، لایه خاک دچار تغییر شکل می‌شود. این تغییر شکل (فشرده شدن خاک) نشست نام دارد که منجر به نشست فونداسیون می‌شود. "
        about3 = "در واقعیت اکثر پی‌ها تا حدی انعطاف‌پذیر هستند که این امر موجب نشست نامتقارن می‌شود:"
        about4 = "1."
        about5 = " در خاک‌های دانه‌ای: نشست در گوشه پی بیشتر از مرکز آن است، زیرا در این خاک دانه‌هایی که در گوشه پی هستند وقتی تحت فشار قرار می‌گیرند، به سادگی از زیر آن فرار می‌کنند که این امر باعث نشست بیشتر می‌شود."
        about6 = "2."
        about7 = "در خاک‌های چسبنده: دانه‌ها به دلیل چسبندگی از زیر پی نمی توانند فرار کنند و به همین دلیل تحت بارگذاری نشستهای مرکز پی بیشتر از گوشه‌های آن است."
        about8 = "نشستهای آنی در تمامی خاک‌ها چه ریزدانه، چه درشت دانه، اشباع و غیر اشباع رخ می‌دهد. بخش کمی از نشستها ناشی از تغییر شکل الاستیک دانه‌های خاک است."
        about9 = 'این ماژول علاوه بر روش تحلیل الاستیک قادر به محاسبه به روش اشمارتمن نیز می باشد.'
        message_box.setText(about + "\n\n    " + about2 + "\n\n    " + about3 + "\n\n" + about4 + about5 + "\n\n" + about6 + about7 + "\n\n" + about8 + "\n\n" + about9)


        message_box.setWindowTitle('Module 4 Help')

        message_box.exec_()


