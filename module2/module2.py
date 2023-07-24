from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QToolButton ,QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog ,QToolTip , QErrorMessage
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor , QCursor
from PyQt5.QtCore import Qt ,QSize
import sys , math



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure






class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Module 2'
        self.setWindowTitle(self.title)
        
        self.table_widget = Module2(self)
        self.setCentralWidget(self.table_widget)

        
        self.show()
        self.setFixedSize(self.size())
class Module2(QWidget):



    def input_datas (self,layout ):
        gridLayout = QGridLayout()


        #PILE CHAR.
        #pile type
        self.pileType = QComboBox()
        
        # One of the pile Type item was STEEL , it has been deleted . 
        self.pileType.addItems([ "PRECAST CONCRETE" , "INSITU CONCRETE" ])
        self.pileType.currentTextChanged.connect(self.PileTypeSettings)
        self.pileType_string = "INSITU"

        #pile Sec.
        self.pileSection = QComboBox()
        self.pileSection.addItems(["CYLINDRICAL", "SQUARE"])
        self.pileSection.currentTextChanged.connect(self.choosingPileSection)
        self.pileSection_string = "CYLINDRICAL"

        #End Con.
        self.endCondition = QComboBox()
        self.endCondition.addItems(["TUBULAR", "NONTUBULAR"])
        self.endCondition.currentTextChanged.connect (self.choosingEndCondition)
        self.endCondition_string = "TUBULAR"
        self.endCondition.setEnabled(True)

        #Dp
        self.pileChar_Dp = QLineEdit()
        self.pileChar_Dp.setValidator(QDoubleValidator())
        self.pileChar_Dp.setPlaceholderText("meters")
        self.pileChar_Dp.textChanged.connect(self.enButton)
        #Thick
        self.pileChar_thick = QLineEdit()
        self.pileChar_thick.setValidator(QDoubleValidator())
        self.pileChar_thick.setPlaceholderText("mm")
        self.pileChar_thick.textChanged.connect(self.enButton)

        #pile Len.
        self.pileChar_pileLen = QLineEdit()
        self.pileChar_pileLen.setValidator(QDoubleValidator())
        self.pileChar_pileLen.setPlaceholderText("meters")
        self.pileChar_pileLen.textChanged.connect(self.enButton)

        #max expected depth of pile
        self.pileChar_maxExpectedDepthOfPile = QLineEdit()
        self.pileChar_maxExpectedDepthOfPile.setValidator(QDoubleValidator())
        self.pileChar_maxExpectedDepthOfPile.setPlaceholderText("meters")

        #Depth increment
        self.pileChar_depthIncrement = QComboBox ()
        self.pileChar_depthIncrement.addItems(["0.25 m" , "0.5 m" , "1.0 m"])
        self.pileChar_depthIncrement.currentTextChanged.connect (self.pileChar_depthIncrement_calculator)
        self.pileLen_ = 0.25

        #Loading
        self.loading_Q = QLineEdit()
        self.loading_Q.setValidator(QDoubleValidator())
        self.loading_Q.setPlaceholderText("ton")
        self.loading_Q.textChanged.connect(self.enButton)

        

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



        
        
        self.pileChar_Box = QGroupBox("PILE CHARACTERISTIC")
        self.pileChar_Part = QFormLayout()
        
        pileTypeLabel = QLabel("Pile Type ") 
        pileTypeLabel.setToolTip("نوع شمع")
        self.pileChar_Part.addRow (pileTypeLabel , self.pileType)
                
        pileSecLabel = QLabel("Pile Section ") 
        pileSecLabel.setToolTip("مقطع شمع")
        self.pileChar_Part.addRow (pileSecLabel, self.pileSection)

        endConLabel = QLabel("End Condition ") 
        endConLabel.setToolTip("وضعیت نوک شمع")
        self.pileChar_Part.addRow (endConLabel , self.endCondition)

        DpLabel = QLabel ("Dp (m)")
        DpLabel.setToolTip("قطر شمع با مقطع دایره یا ضلع شمع با مقطع مربع")
        self.pileChar_Part.addRow(DpLabel , self.pileChar_Dp)

        thicknessLabel = QLabel ("Thickness (mm)" )
        thicknessLabel.setToolTip("ضخامت شمع")
        self.pileChar_Part.addRow(thicknessLabel, self.pileChar_thick )

        pileLenLabel = QLabel ("Pile Length (m)" )
        pileLenLabel.setToolTip("طول شمع")
        self.pileChar_Part.addRow(pileLenLabel , self.pileChar_pileLen )
        #self.pileChar_Part.addRow("Max Expected Depth (m)" , self.pileChar_maxExpectedDepthOfPile )

        self.pileChar_Box.setLayout(self.pileChar_Part)
        self.pileChar_Box.setStyleSheet(boxesStyle)
        self.pileChar_Box.setAlignment(Qt.AlignCenter)




        #Other Char.
        self.numberOfLayer = QComboBox ()
        self.numberOfLayer.addItems(["One layer", "Two layers", "Three layers", "Four layers"])
        self.numberOfLayer.currentTextChanged.connect(self.activeLayer)

        
        #Dw
        self.otherChar_Dw = QLineEdit()
        self.otherChar_Dw.setValidator(QDoubleValidator())
        self.otherChar_Dw.setPlaceholderText("meters")
        self.otherChar_Dw.textChanged.connect(self.enButton)

        #gamma w
        self.otherChar_gammaw = QLineEdit()
        self.otherChar_gammaw.setValidator(QDoubleValidator())
        self.otherChar_gammaw.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.otherChar_gammaw.textChanged.connect(self.enButton)

        #FOS P
        self.otherChar_FOS_p = QLineEdit()
        self.otherChar_FOS_p.setValidator(QDoubleValidator())
        self.otherChar_FOS_p.textChanged.connect(self.enButton)

        #FOS f
        self.otherChar_FOS_f = QLineEdit()
        self.otherChar_FOS_f.setValidator(QDoubleValidator())
        self.otherChar_FOS_f.textChanged.connect(self.enButton)

        
        self.otherChar_Box = QGroupBox("GENERAL")
        self.otherChar_Part = QFormLayout()
        self.otherChar_Part.addRow("Layers " , self.numberOfLayer)

        # loadingLabel = QLabel ("Loading (ton)")
        # loadingLabel.setToolTip("بار قائم شمع")
        # self.otherChar_Part.addRow (loadingLabel , self.loading_Q)

        DwLabel = QLabel ("Dw (m)")
        DwLabel.setToolTip("عمق‌آب")
        self.otherChar_Part.addRow(DwLabel , self.otherChar_Dw)

        gammawLabel = QLabel (u"\u03B3 w (ton/m\N{SUPERSCRIPT THREE})" )
        gammawLabel.setToolTip("وزن مخصوص آب")
        self.otherChar_Part.addRow(gammawLabel, self.otherChar_gammaw)

        fospLabel = QLabel ("(FOS) p " )
        fospLabel.setToolTip("ضریب اطمینان ظرفیت انتهای شمع")
        self.otherChar_Part.addRow(fospLabel, self.otherChar_FOS_p)
        
        fospLabel = QLabel ("(FOS) f " )
        fospLabel.setToolTip("ضریب اطمینان ظرفیت جدار شمع")
        self.otherChar_Part.addRow(fospLabel, self.otherChar_FOS_f)


        self.otherChar_Part.addRow("Depth increment" , self.pileChar_depthIncrement )
        self.otherChar_Box.setLayout(self.otherChar_Part)
        self.otherChar_Box.setStyleSheet(boxesStyle)
        self.otherChar_Box.setAlignment(Qt.AlignCenter)


        

        
        
        
        # first layer PART
        # gamma 1 wet
        self.l1_gammawet = QLineEdit()
        self.l1_gammawet.setValidator(QDoubleValidator())
        self.l1_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l1_gammawet.textChanged.connect(self.enButton)

        # gamma 1 sat
        self.l1_gammasat = QLineEdit()
        self.l1_gammasat.setValidator(QDoubleValidator())
        self.l1_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l1_gammasat.textChanged.connect(self.enButton)

        # fi 1
        self.l1_fi = QLineEdit()
        self.l1_fi.setValidator(QDoubleValidator())
        self.l1_fi.setPlaceholderText("degree")
        self.l1_fi.textChanged.connect(self.enButton)


        # C 1
        self.l1_c = QLineEdit()
        self.l1_c.setValidator(QDoubleValidator())
        self.l1_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l1_c.textChanged.connect(self.enButton)


        # D 1
        self.l1_d = QLineEdit()
        self.l1_d.setValidator(QDoubleValidator())
        self.l1_d.setPlaceholderText("meters")
        self.l1_d.textChanged.connect(self.enButton)


        self.l1Box = QGroupBox("1ST LAYER CHARACTERISTIC")
        self.l1Part = QFormLayout()

        l1_gammaWetLabel = QLabel (u"\u03B3\u2081 wet (ton/m\N{SUPERSCRIPT THREE})")
        l1_gammaWetLabel.setToolTip("وزن مخصوص مرطوب خاک")
        self.l1Part.addRow(l1_gammaWetLabel, self.l1_gammawet)

        l1_gammaSatLabel = QLabel (u"\u03B3\u2081 sat (ton/m\N{SUPERSCRIPT THREE})")
        l1_gammaSatLabel.setToolTip("وزن مخصوص اشباع خاک")
        self.l1Part.addRow(l1_gammaSatLabel, self.l1_gammasat)

        l1_fiLabel = QLabel (u"\u03C6\u2081 (degree)")
        l1_fiLabel.setToolTip("زاویه اصطکاک خاک")
        self.l1Part.addRow(l1_fiLabel, self.l1_fi)
        
        l1_cLabel = QLabel (u"C\u2081 (ton/m\N{SUPERSCRIPT TWO})")
        l1_cLabel.setToolTip("چسبندگی خاک")
        self.l1Part.addRow(l1_cLabel, self.l1_c)

        l1_dLabel = QLabel (u"D\u2081 (m)")
        l1_dLabel.setToolTip("عمق لایه خاک")
        self.l1Part.addRow(l1_dLabel, self.l1_d)
        self.l1Box.setLayout(self.l1Part)
        self.l1Box.setStyleSheet(boxesStyle)
        self.l1Box.setAlignment(Qt.AlignCenter)



        # second Layer PART
        # gamma 2 wet
        self.l2_gammawet = QLineEdit()
        self.l2_gammawet.setValidator(QDoubleValidator())
        self.l2_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l2_gammawet.textChanged.connect(self.enButton)

        # gamma 2 sat
        self.l2_gammasat = QLineEdit()
        self.l2_gammasat.setValidator(QDoubleValidator())
        self.l2_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l2_gammasat.textChanged.connect(self.enButton)

        # fi 2
        self.l2_fi = QLineEdit()
        self.l2_fi.setValidator(QDoubleValidator())
        self.l2_fi.setPlaceholderText("degree")
        self.l2_fi.textChanged.connect(self.enButton)


        # C 2
        self.l2_c = QLineEdit()
        self.l2_c.setValidator(QDoubleValidator())
        self.l2_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l2_c.textChanged.connect(self.enButton)


        # D 2
        self.l2_d = QLineEdit()
        self.l2_d.setValidator(QDoubleValidator())
        self.l2_d.setPlaceholderText("meters")
        self.l2_d.textChanged.connect(self.enButton)


        self.l2Box = QGroupBox("2ND LAYER CHARACTERISTIC")
        self.l2Part = QFormLayout()
        self.l2Part.addRow(u"\u03B3\u2082 wet (ton/m\N{SUPERSCRIPT THREE})", self.l2_gammawet)
        self.l2Part.addRow(u"\u03B3\u2082 sat (ton/m\N{SUPERSCRIPT THREE})", self.l2_gammasat)
        self.l2Part.addRow(u"\u03C6\u2082 (degree)", self.l2_fi)
        self.l2Part.addRow(u"C\u2082 (ton/m\N{SUPERSCRIPT TWO})", self.l2_c)
        self.l2Part.addRow(u"D\u2082 (m)", self.l2_d)
        self.l2Box.setLayout(self.l2Part)
        self.l2Box.setEnabled(False)
        self.l2Box.setStyleSheet(boxesStyle)
        self.l2Box.setAlignment(Qt.AlignCenter)



        # third Layer PART
        # gamma 3 wet
        self.l3_gammawet = QLineEdit()
        self.l3_gammawet.setValidator(QDoubleValidator())
        self.l3_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l3_gammawet.textChanged.connect(self.enButton)

        # gamma 3 sat
        self.l3_gammasat = QLineEdit()
        self.l3_gammasat.setValidator(QDoubleValidator())
        self.l3_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l3_gammasat.textChanged.connect(self.enButton)

        # fi 3
        self.l3_fi = QLineEdit()
        self.l3_fi.setValidator(QDoubleValidator())
        self.l3_fi.setPlaceholderText("degree")
        self.l3_fi.textChanged.connect(self.enButton)


        # C 3
        self.l3_c = QLineEdit()
        self.l3_c.setValidator(QDoubleValidator())
        self.l3_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l3_c.textChanged.connect(self.enButton)


        # D 3
        self.l3_d = QLineEdit()
        self.l3_d.setValidator(QDoubleValidator())
        self.l3_d.setPlaceholderText("meters")
        self.l3_d.textChanged.connect(self.enButton)


        self.l3Box = QGroupBox("3RD LAYER CHARACTERISTIC")
        self.l3Part = QFormLayout()
        self.l3Part.addRow(u"\u03B3\u2083 wet (ton/m\N{SUPERSCRIPT THREE})", self.l3_gammawet)
        self.l3Part.addRow(u"\u03B3\u2083 sat (ton/m\N{SUPERSCRIPT THREE})", self.l3_gammasat)
        self.l3Part.addRow(u"\u03C6\u2083 (degree)", self.l3_fi)
        self.l3Part.addRow(u"C\u2083 (ton/m\N{SUPERSCRIPT TWO})", self.l3_c)
        self.l3Part.addRow(u"D\u2083 (m)", self.l3_d)
        self.l3Box.setLayout(self.l3Part)
        self.l3Box.setEnabled(False)
        self.l3Box.setStyleSheet(boxesStyle)
        self.l3Box.setAlignment(Qt.AlignCenter)


        
        

        # fourth Layer PART
        # gamma 4 wet
        self.l4_gammawet = QLineEdit()
        self.l4_gammawet.setValidator(QDoubleValidator())
        self.l4_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l4_gammawet.textChanged.connect(self.enButton)

        # gamma 4 sat
        self.l4_gammasat = QLineEdit()
        self.l4_gammasat.setValidator(QDoubleValidator())
        self.l4_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l4_gammasat.textChanged.connect(self.enButton)

        # fi 4
        self.l4_fi = QLineEdit()
        self.l4_fi.setValidator(QDoubleValidator())
        self.l4_fi.setPlaceholderText("degree")
        self.l4_fi.textChanged.connect(self.enButton)


        # C 4
        self.l4_c = QLineEdit()
        self.l4_c.setValidator(QDoubleValidator())
        self.l4_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l4_c.textChanged.connect(self.enButton)


        # D 4
        self.l4_d = QLineEdit()
        self.l4_d.setValidator(QDoubleValidator())
        self.l4_d.setPlaceholderText("meters")
        self.l4_d.textChanged.connect(self.enButton)


        self.l4Box = QGroupBox("4TH LAYER CHARACTERISTIC")
        self.l4Part = QFormLayout()
        self.l4Part.addRow(u"\u03B3\u2084 wet (ton/m\N{SUPERSCRIPT THREE})", self.l4_gammawet)
        self.l4Part.addRow(u"\u03B3\u2084 sat (ton/m\N{SUPERSCRIPT THREE})", self.l4_gammasat)
        self.l4Part.addRow(u"\u03C6\u2084 (degree)", self.l4_fi)
        self.l4Part.addRow(u"C\u2084 (ton/m\N{SUPERSCRIPT TWO})", self.l4_c)
        self.l4Part.addRow(u"D\u2084 (m)", self.l4_d)
        self.l4Box.setLayout(self.l4Part)
        self.l4Box.setEnabled(False)
        self.l4Box.setStyleSheet(boxesStyle)
        self.l4Box.setAlignment(Qt.AlignCenter)




        gridLayout.addWidget(self.pileChar_Box , 0 , 0 )
        gridLayout.addWidget(self.otherChar_Box , 1 , 0)
        gridLayout.addWidget(self.l1Box, 0, 2)
        gridLayout.addWidget(self.l2Box, 1, 2)
        gridLayout.addWidget(self.l3Box, 0, 3)
        gridLayout.addWidget(self.l4Box, 1, 3)

        layout.addLayout(gridLayout)
    
    

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


    def resetAll(self):
        theInputs = [self.pileChar_Dp , self.pileChar_thick , self.pileChar_pileLen ,self.loading_Q , self.otherChar_Dw , self.otherChar_gammaw , self.otherChar_FOS_p , self.otherChar_FOS_f , self.l1_gammawet , self.l1_gammasat , self.l1_fi , self.l1_c , self.l1_d ,self.l2_gammawet , self.l2_gammasat , self.l2_fi , self.l2_c , self.l2_d ,self.l3_gammawet , self.l3_gammasat , self.l3_fi , self.l3_c , self.l3_d , self.l4_gammawet , self.l4_gammasat , self.l4_fi , self.l4_c , self.l4_d]
        
        
        for inp in theInputs:
            inp.clear()

        self.graphButton.setEnabled(False)


    def enButton(self):
        #TO DO : bayad check shavad ke row = 0 table filled bashad !
        flag = 0 
        if self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False :

            if (self.pileChar_Dp.text() == '' or self.pileChar_pileLen.text() == '' or self.otherChar_Dw.text() == '' or self.otherChar_gammaw.text() == '' or self.otherChar_FOS_p.text() == '' or self.otherChar_FOS_f.text() == '' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == ''):
                self.graphButton.setEnabled(False)
                flag = 1


        if self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False :

            if (self.pileChar_Dp.text() == '' or self.pileChar_pileLen.text() == '' or self.otherChar_Dw.text() == '' or self.otherChar_gammaw.text() == '' or self.otherChar_FOS_p.text() == '' or self.otherChar_FOS_f.text() == '' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == '' or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == ''):
                self.graphButton.setEnabled(False)
                flag = 1

        if self.l3Box.isEnabled() == True and self.l4Box.isEnabled() == False :

            if (self.pileChar_Dp.text() == '' or self.pileChar_pileLen.text() == '' or self.otherChar_Dw.text() == '' or self.otherChar_gammaw.text() == '' or self.otherChar_FOS_p.text() == '' or self.otherChar_FOS_f.text() == '' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == '' or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == '' or self.l3_gammawet.text() == '' or self.l3_gammasat.text() == '' or self.l3_fi.text() == '' or self.l3_c.text() == '' or self.l3_d.text() == ''):
                self.graphButton.setEnabled(False)
                flag = 1

        if self.l4Box.isEnabled() == True  :

            if (self.pileChar_Dp.text() == ''  or self.pileChar_pileLen.text() == '' or self.otherChar_Dw.text() == '' or self.otherChar_gammaw.text() == '' or self.otherChar_FOS_p.text() == '' or self.otherChar_FOS_f.text() == '' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == '' or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == '' or self.l3_gammawet.text() == '' or self.l3_gammasat.text() == '' or self.l3_fi.text() == '' or self.l3_c.text() == '' or self.l3_d.text() == '' or self.l4_gammawet.text() == '' or self.l4_gammasat.text() == '' or self.l4_fi.text() == '' or self.l4_c.text() == '' or self.l4_d.text() == ''):
                self.graphButton.setEnabled(False)
                flag = 1
         
        if self.endCondition_string == "TUBULAR" and self.pileChar_thick.text() == '':
            self.graphButton.setEnabled(False)
            flag = 1
        



        if flag == 0 :
            self.graphButton.setEnabled(True)
        
    def activeLayer(self, s):
        if (s == "One layer"):
            self.l1Box.setEnabled(True)
            self.l2Box.setEnabled(False)
            self.l3Box.setEnabled(False)
            self.l4Box.setEnabled(False)
        if (s == "Two layers"):
            self.l1Box.setEnabled(True)
            self.l2Box.setEnabled(True)
            self.l3Box.setEnabled(False)
            self.l4Box.setEnabled(False)
        if (s == "Three layers"):
            self.l1Box.setEnabled(True)
            self.l2Box.setEnabled(True)
            self.l3Box.setEnabled(True)
            self.l4Box.setEnabled(False)
        if (s == "Four layers"):
            self.l1Box.setEnabled(True)
            self.l2Box.setEnabled(True)
            self.l3Box.setEnabled(True)
            self.l4Box.setEnabled(True)
            
    def pileChar_depthIncrement_calculator(self , s):
        self.pileLen_ = 0.25
        if (s == "0.25 m"):
            self.pileLen_ = 0.25
        if (s == "0.5 m"):
            self.pileLen_ = 0.5
        if (s == "1.0 m"):
            self.pileLen_ = 1



        

        
    '''
    def module2_comboBoxes(self , layout):
        self.comboBoxesBox = QGroupBox()
        self.comboBoxesForm = QFormLayout()
        
        #pile type :
        self.pileType = QComboBox()
        self.pileType.addItems([ "PRECAST CONCRETE" , "INSITU CONCRETE", "STEEL"])
        self.comboBoxesForm.addRow ("Pile Type:" , self.pileType)
        self.pileType.currentTextChanged.connect(self.PileTypeSettings)
        self.pileType_string = "INSITU"
        
        
        #pile section :
        self.pileSection = QComboBox()
        self.pileSection.addItems(["CYLINDRICAL", "SQUARE"])
        self.comboBoxesForm.addRow ("Pile Section:" , self.pileSection)
        self.pileSection.currentTextChanged.connect(self.choosingPileSection)
        self.pileSection_string = "CYLINDRICAL"
        
        #end condition :
        self.endCondition = QComboBox()
        self.endCondition.addItems(["TUBULAR", "NONTUBULAR"])
        self.comboBoxesForm.addRow ("End Condition:" , self.endCondition)
        self.endCondition.currentTextChanged.connect (self.choosingEndCondition)
        self.endCondition_string = "TUBULAR"
        self.endCondition.setEnabled(True)
        
        self.comboBoxesBox.setLayout(self.comboBoxesForm)
        
        layout.addWidget(self.comboBoxesBox, 0 , 0)
    '''
    
    def choosingPileSection (self , s ):
        if (s == "CYLINDRICAL"):
            self.pileSection_string = "CYLINDRICAL"
        elif (s == "SQUARE"):
            self.pileSection_string = "SQUARE"
    
    def choosingEndCondition (self , s):
        if (s == "TUBULAR"):
            self.endCondition_string = "TUBULAR"
            self.pileChar_thick.setEnabled(True)

        elif (s == "NONTUBULAR"):
            self.pileChar_thick.setEnabled(False)
            self.endCondition_string = "NONTUBULAR"
        elif (s == "OPEN END"):
            self.endCondition_string = "OPEN END"
        elif (s == "CLOSED END"):
            self.endCondition_string = "CLOSED END"
    
            
            
            
    def PileTypeSettings (self , s ):
        CYLINDRICAL_index = self.pileSection.findText ("CYLINDRICAL")
        SQUARE_index = self.pileSection.findText ("SQUARE")
        TUBULAR_index = self.endCondition.findText("TUBULAR")
        NONTUBULAR_index = self.endCondition.findText("NONTUBULAR")
        OPEN_END_index = self.endCondition.findText("OPEN END")
        CLOSED_END_index = self.endCondition.findText("CLOSED END")
                    
            
        if (s == "INSITU CONCRETE"):
            self.pileSection.removeItem(SQUARE_index)
            self.endCondition.removeItem(OPEN_END_index)
            self.endCondition.removeItem(CLOSED_END_index)
            self.endCondition.removeItem(TUBULAR_index)
            self.endCondition.removeItem(NONTUBULAR_index)
            self.endCondition.setEnabled(False)
            self.pileSection.setEnabled(False)
            self.pileType_string = "INSITU"
            
            
        if (s == "PRECAST CONCRETE"):
            self.pileSection.addItem("SQUARE")
            self.endCondition.setEnabled(True)
            self.pileSection.setEnabled(True)
            self.endCondition.removeItem(OPEN_END_index)
            self.endCondition.removeItem(CLOSED_END_index)
            self.endCondition.removeItem(TUBULAR_index)
            self.endCondition.removeItem(NONTUBULAR_index)
            self.endCondition.addItem("TUBULAR")
            self.endCondition.addItem("NONTUBULAR")
            self.pileType_string = "PRECAST"
            
            
        # if (s == "STEEL"):
        #     self.pileSection.removeItem(SQUARE_index)
        #     self.endCondition.setEnabled(True)
        #     self.pileSection.setEnabled(False)
        #     self.endCondition.removeItem(TUBULAR_index)
        #     self.endCondition.removeItem(NONTUBULAR_index)
        #     self.endCondition.removeItem(OPEN_END_index)
        #     self.endCondition.removeItem(CLOSED_END_index)
        #     self.endCondition.addItem("OPEN END")
        #     self.endCondition.addItem("CLOSED END")
        #     self.pileSection.removeItem(SQUARE_index)
        #     self.pileType_string = "STEEL"
        
            
            
        
    
    def choosingLayer (self , DBase):
        if (self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False):
            self.n = 1

        elif (self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False):

            if (DBase <= float(self.l1_d.text()) ):
                self.n = 1
            elif (float(self.l1_d.text()) < DBase <= float(self.l1_d.text()) + float(self.l2_d.text() )):
                self.n = 2
            else :
                self.n = 0


        elif (self.l3Box.isEnabled() == True and self.l4Box.isEnabled == False):
            if (DBase <= float(self.l1_d.text()) ):
                self.n = 1
            elif (float(self.l1_d.text()) < DBase <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.n = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < DBase <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.n = 3
            else :
                self.n = 0
            
        elif (self.l4Box.isEnabled() == True):
            if (DBase <= float(self.l1_d.text() )):
                self.n = 1
            elif (float(self.l1_d.text()) < DBase <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.n = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < DBase <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.n = 3
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) + float(self.l3_d.text()) <= DBase <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) + float(self.l4_d.text())):
                self.n = 4
            else :
                self.n = 0
                 
    def choosingLayerForWater (self):
        if (self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False):
            self.nWater = 1
        elif (self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False):
            if (float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) ):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text() )):
                self.nWater = 2
            else :
                self.nWater = 0


        elif (self.l3Box.isEnabled() == True and self.l4Box.isEnabled == False):
            if (float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) ):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.nWater = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.nWater = 3
            else :
                self.nWater = 0
            
        elif (self.l4Box.isEnabled() == True ):
            if (float(self.otherChar_Dw.text()) <= float(self.l1_d.text() )):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.nWater = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.nWater = 3
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) + float(self.l3_d.text()) <= float(self.otherChar_Dw.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) + float(self.l4_d.text())):
                self.nWater = 4
            else :
                self.nWater = 0
    
    def calculate_Ap(self):
        Ap = 0
        
        if (self.pileType_string == "INSITU"):
            Ap = 1/4 * math.pi * math.pow (float(self.pileChar_Dp.text()) , 2)
            
            
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "TUBULAR"):
            Ap = math.pi * float(self.pileChar_Dp.text()) * float(self.pileChar_thick.text())/1000
            
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "NONTUBULAR"):
            Ap = 1/4 * math.pi * math.pow (float(self.pileChar_Dp.text()) , 2)
            
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "SQUARE" and self.endCondition_string == "TUBULAR"):
            Ap = 4 * float(self.pileChar_Dp.text()) * float(self.pileChar_thick.text())/1000
            
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "SQUARE" and self.endCondition_string == "NONTUBULAR"):
            Ap = math.pow (float(self.pileChar_Dp.text()) , 2)
        
        if (self.pileType_string == "STEEL" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "OPEN END"):
            Ap = math.pi * float(self.pileChar_Dp.text()) * float(self.pileChar_thick.text())/1000
            
        if (self.pileType_string == "STEEL" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "CLOSED END"):
            Ap = 1/4 * math.pi * math.pow (float(self.pileChar_Dp.text()) , 2)

        return (Ap)
    
    def calculate_Pp (self):
        Pp = 0
        if (self.pileType_string == "INSITU"):
            Pp = math.pi * float(self.pileChar_Dp.text())
            
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "TUBULAR"):
            Pp = math.pi * float(self.pileChar_Dp.text())
        
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "NONTUBULAR"):
            Pp = math.pi * float(self.pileChar_Dp.text())
        
        if (self.pileType_string == "PRECAST" and self.pileSection_string == "SQUARE" and self.endCondition_string == "TUBULAR"):
            Pp = 4 * float(self.pileChar_Dp.text())

        if (self.pileType_string == "PRECAST" and self.pileSection_string == "SQUARE" and self.endCondition_string == "NONTUBULAR"):
            Pp = 4 * float(self.pileChar_Dp.text())
        
        if (self.pileType_string == "STEEL" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "OPEN END"):
            Pp = math.pi * float(self.pileChar_Dp.text())

        if (self.pileType_string == "STEEL" and self.pileSection_string == "CYLINDRICAL" and self.endCondition_string == "CLOSED END"):
            Pp = math.pi * float(self.pileChar_Dp.text())
        
        return (Pp)
    
    def calculate_N (self):
        N = 2.5
        return (N)
    
    def calculate_Nq (self , N):
        try:
            Nq = 0
            if (self.n == 1):
                fi = float(self.l1_fi.text())
            if (self.n == 2):
                fi = float(self.l2_fi.text())
            if (self.n == 3):
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            fi = math.radians(fi)
            
            Nq = math.pow (10 , N * math.tan(fi))
            return Nq
        except :
            raise Exception("\u03C6"+str(self.n))
    
    def calculate_Nc (self , Nq):
        try:
            Nc = 0
            if (self.n == 1):
                fi = float(self.l1_fi.text())
            if (self.n == 2):
                fi = float(self.l2_fi.text())
            if (self.n == 3):
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            
            fi = math.radians(fi)
            Nc = (Nq - 1)/math.tan(fi)
            return Nc
        except :
            raise Exception(u"\u03C6"+str(self.n))
    
    
    def calculate_Qp (self , Nc , qp , Nq , Ap):
        Qp= 0
        if (self.n == 1):
            cn = float(self.l1_c.text())
            fi = float(self.l1_fi.text())
        if (self.n == 2):
            cn = float(self.l2_c.text())
            fi = float(self.l2_fi.text())
        if (self.n == 3):
            cn = float(self.l3_c.text())
            fi = float(self.l3_fi.text())
        if (self.n == 4):
            cn = float(self.l4_c.text())
            fi = float(self.l4_fi.text())
        
        if (fi > 0):
            Qp = (cn*Nc + qp*Nq)*Ap
        if (fi == 0):
            Qp = 9*cn*Ap
        return Qp
    
    def calculate_p (self , Pp , pileChar_pileLen):
        if (self.n == 1):
            p1 = 0
            p1 = Pp * pileChar_pileLen
            return p1
        if (self.n == 2):
            p1 = 0
            p2 = 0
            p1 = Pp*float(self.l1_d.text())
            p2 = Pp*(pileChar_pileLen-float(self.l1_d.text()))
            return p1 , p2
        if (self.n == 3):
            p1 = 0
            p2 = 0
            p3 = 0
            p1 = Pp*float(self.l1_d.text())
            p2 = Pp*float(self.l2_d.text())
            p3 = Pp*(pileChar_pileLen-float(self.l1_d.text())-float(self.l2_d.text()))
            return p1 , p2 , p3
        if (self.n == 4):
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p1 = Pp*float(self.l1_d.text())
            p2 = Pp*float(self.l2_d.text())
            p3 = Pp*float(self.l3_d.text())
            p4 = Pp*(pileChar_pileLen-float(self.l1_d.text())-float(self.l2_d.text())-float(self.l3_d.text()))
            return p1 , p2 , p3 , p4
        
    def calculate_gama (self):
        if (self.pileType_string == "INSITU"):
            if (self.n == 1):
                gamma1 = 3/4*float(self.l1_fi.text())
                return (gamma1)
            elif (self.n == 2):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                return (gamma1 , gamma2)
            elif (self.n == 3):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                gamma3 = 3/4*float(self.l3_fi.text())
                return(gamma1 , gamma2 , gamma3)
            elif (self.n == 4):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                gamma3 = 3/4*float(self.l3_fi.text())
                gamma4 = 3/4*float(self.l4_fi.text())
                return (gamma1 , gamma2 , gamma3 , gamma4)
        elif (self.pileType_string == "PRECAST"):
            
            if (self.n == 1):
                gamma1 = 3/4*float(self.l1_fi.text())
                return (gamma1)
            elif (self.n == 2):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                return (gamma1 , gamma2)
            elif (self.n == 3):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                gamma3 = 3/4*float(self.l3_fi.text())
                return(gamma1 , gamma2 , gamma3)
            elif (self.n == 4):
                gamma1 = 3/4*float(self.l1_fi.text())
                gamma2 = 3/4*float(self.l2_fi.text())
                gamma3 = 3/4*float(self.l3_fi.text())
                gamma4 = 3/4*float(self.l4_fi.text())
                return (gamma1 , gamma2 , gamma3 , gamma4)
                
        elif (self.pileType_string == "STEEL"):
            if (self.n == 1):
                gamma1 = 20
                return(gamma1)
            elif (self.n == 2):
                gamma1 = 20
                gamma2 = 20
                return(gamma1 , gamma2)
            elif (self.n == 3):
                gamma1 = 20
                gamma2 = 20
                gamma3 = 20
                return (gamma1 , gamma2 , gamma3)
            elif (self.n == 4):
                gamma1 = 20
                gamma2 = 20
                gamma3 = 20
                gamma4 = 20
                return (gamma1 , gamma2 , gamma3 , gamma4)
            
    def calculate_k (self):
        if (self.pileType_string == "INSITU"):
            if (self.n == 1):
                k1 = 0.5
                return (k1)
            elif (self.n == 2):
                k1 = 0.5
                k2 = 0.5
                return (k1 , k2)
            elif (self.n == 3):
                k1 = 0.5
                k2 = 0.5
                k3 = 0.5
                return(k1 , k2 , k3)
            elif (self.n == 4):
                k1 = 0.5
                k2 = 0.5
                k3 = 0.5
                k4 = 0.5
                return (k1 , k2 , k3 , k4)
        elif (self.pileType_string == "PRECAST"):
            
            if (self.n == 1):
                k1 = 1
                return (k1)
            elif (self.n == 2):
                k1 = 1
                k2 = 1
                return (k1 , k2)
            elif (self.n == 3):
                k1 = 1
                k2 = 1
                k3 = 1
                return(k1 , k2 , k3)
            elif (self.n == 4):
                k1 = 1
                k2 = 1
                k3 = 1
                k4 = 1
                return (k1 , k2 , k3 , k4)
                
                
        elif (self.pileType_string == "STEEL"):
            if (self.n == 1):
                k1 = 0.5
                return (k1)
            elif (self.n == 2):
                k1 = 0.5
                k2 = 0.5
                return (k1 , k2)
            elif (self.n == 3):
                k1 = 0.5
                k2 = 0.5
                k3 = 0.5
                return(k1 , k2 , k3)
            elif (self.n == 4):
                k1 = 0.5
                k2 = 0.5
                k3 = 0.5
                k4 = 0.5
                return (k1 , k2 , k3 , k4)
        
    def calculate_q (self , DBase):
        q = 0

        if (float(self.otherChar_Dw.text()) > DBase):
        
            if (self.n == 1):
                q = float(self.l1_gammawet.text()) * (DBase)
            if (self.n == 2):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * (DBase - float(self.l1_d.text()))
            
            if (self.n == 3):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * float(self.l2_d.text()) +  (DBase - float(self.l1_d.text())- float(self.l2_d.text()))*float(self.l3_gammawet.text())
            
            if (self.n == 4):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * float(self.l2_d.text())+ float(self.l3_gammawet.text()) * float(self.l3_d.text()) +  (DBase - float(self.l1_d.text())- float(self.l2_d.text())- float(self.l3_d.text()))*float(self.l4_gammawet.text())
            
            
        elif (float(self.otherChar_Dw.text()) <= DBase) :

            if (self.n == 1 and self.nWater == 1):
                q = float(self.otherChar_Dw.text()) * float(self.l1_gammawet.text()) + (DBase - float(self.otherChar_Dw.text()))*(float(self.l1_gammasat.text()) - float(self.otherChar_gammaw.text()))
            if (self.n == 2 and self.nWater == 1):
                q = float(self.otherChar_Dw.text())*float(self.l1_gammawet.text())+(float(self.l1_d.text()) - float(self.otherChar_Dw.text()))*(float(self.l1_gammasat.text()) - float(self.otherChar_gammaw.text())) + (DBase - float(self.l1_d.text()))*(float(self.l2_gammasat.text()) - float(self.otherChar_gammaw.text()))
            
            if (self.n == 2 and self.nWater == 1):
                q = float(self.l1_d.text())*float(self.l1_gammawet.text()) + (float(self.otherChar_Dw.text())- float(self.l1_d.text()))*(float(self.l2_gammawet.text())) + (DBase - float(self.otherChar_Dw.text()))*(float(self.l2_gammasat.text()) -float(self.otherChar_gammaw.text()) )
            
            if (self.n == 3 and self.nWater == 1):
                q = float(self.otherChar_Dw.text())*float(self.l1_gammawet.text()) + (float(self.l1_d.text()) - float(self.otherChar_Dw.text()))*(float(self.l1_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.l2_d.text()))*(float(self.l2_gammasat.text()) - float(self.otherChar_gammaw.text())) + (DBase - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammasat.text()) - float(self.otherChar_gammaw.text()))
            
                    
            if (self.n == 3 and self.nWater == 2):
                q = (float(self.l1_d.text()) * float(self.l1_gammawet.text())) + (float(self.otherChar_Dw.text()) - float(self.l1_d.text())) * (float(self.l2_gammawet.text()))+ (float(self.l1_d.text()) + float(self.l2_d.text()) - float(self.otherChar_Dw.text())) * ( float(self.l2_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammasat.text())-float(self.otherChar_gammaw.text()))
            
            if (self.n == 3 and self.nWater == 3):
                q = (float(self.l1_d.text()) * float(self.l1_gammawet.text())) + (float(self.l2_d.text()) * float(self.l2_gammawet.text())) + (float(self.otherChar_Dw.text()) - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammawet.text()))+ (DBase - float(self.otherChar_Dw.text()))*(float(self.l3_gammasat.text())-float(self.otherChar_gammaw.text()))


            if (self.n == 4 and self.nWater == 1):
                q = float(self.otherChar_Dw.text()) * float(self.l1_gammawet.text()) + (float(self.l1_d.text()) - float(self.otherChar_Dw.text()))* (float(self.l1_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.l2_d.text()))*(float(self.l2_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.l3_d.text()))*(float(self.l3_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.otherChar_gammaw.text()))

            
            if (self.n == 4 and self.nWater == 2):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) + (float(self.otherChar_Dw.text())-float(self.l1_d.text()))*float(self.l2_gammawet.text()) + (float(self.l1_d.text()) + float(self.l2_d.text()) - float(self.otherChar_Dw.text())) *(float(self.l2_gammasat.text()) - float(self.otherChar_gammaw.text()) ) + (float(self.l3_d.text()))*(float(self.l3_gammasat.text()) - float(self.otherChar_gammaw.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.otherChar_gammaw.text()))
                            
            if (self.n == 4 and self.nWater == 3):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) +float(self.l2_d.text()) * float(self.l2_gammawet.text())+ (float(self.otherChar_Dw.text())-float(self.l1_d.text())-float(self.l2_d.text()))*float(self.l3_gammawet.text()) + (float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) - float(self.otherChar_Dw.text())) *(float(self.l3_gammasat.text()) - float(self.otherChar_gammaw.text()) ) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.otherChar_gammaw.text()))
            if (self.n == 4 and self.nWater == 4):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) +float(self.l2_d.text()) * float(self.l2_gammawet.text())+ float(self.l3_d.text()) * float(self.l3_gammawet.text()) + (float(self.otherChar_Dw.text())-float(self.l1_d.text())-float(self.l2_d.text())-float(self.l3_d.text()))*float(self.l4_gammawet.text()) + (DBase - float(self.otherChar_Dw.text()))*(float(self.l4_gammasat.text())-float(self.otherChar_gammaw.text()))




        return (q)
    
    def calculate_qp(self , DBase):
        return self.calculate_q(DBase)
    
    def calculate_qcr(self , DBase):
        return self.calculate_q(15 * DBase)
    
    def calculate_q1(self):
        return self.calculate_q(float(self.l1_d.text()))
    
    def calculate_q2(self):
        return self.calculate_q(float(self.l1_d.text())+float(self.l2_d.text()))
    
    def calculate_q3(self):
        return self.calculate_q(float(self.l1_d.text())+float(self.l2_d.text())+float(self.l3_d.text()))
    
    def calculate_Qf1 (self , DBase):
        try:
            Qf1 = 0
            qp = self.calculate_qp (DBase)
            qcr = self.calculate_qcr(DBase)
            if (qp >= qcr):
                qp = qcr


            if (self.n == 1):
                k1 = self.calculate_k()
                p1 = self.calculate_p(self.calculate_Pp() , DBase)
                gamma1 = self.calculate_gama()
                Qf1 = k1 * qp/2 * math.tan(math.radians(gamma1)) * p1
                return Qf1
                

        
            if (self.n == 2):
                k1 , k2 = self.calculate_k()
                p1 , p2 = self.calculate_p(self.calculate_Pp() , DBase)
                gamma1 , gamma2 = self.calculate_gama()
                q1 = self.calculate_q1()
                if (q1 >= qcr):
                    q1 = qcr
                Qf1 = k1 * q1/2 * math.tan(math.radians(gamma1)) * p1 + k2 * (qp+q1)/2 * math.tan(math.radians(gamma2)) * p2
                return Qf1



            if (self.n == 3):
                k1 , k2 , k3 = self.calculate_k()
                p1 , p2 , p3 = self.calculate_p(self.calculate_Pp() , DBase)
                gamma1 , gamma2 , gamma3 = self.calculate_gama()
                q1 = self.calculate_q1()
                q2 = self.calculate_q2()
                if (q1 >= qcr):
                    q1 = qcr
                if (q2 >= qcr):
                    q2 = qcr
                Qf1 = k1 * q1/2 * math.tan(math.radians(gamma1)) * p1 + k2 * (q2+q1)/2 * math.tan(math.radians(gamma2)) * p2 + k3 * (qp+q2)/2 * math.tan(math.radians(gamma3)) * p3
                return Qf1
            if (self.n == 4):
                k1 , k2 , k3 , k4 = self.calculate_k()
                p1 , p2 , p3 , p4 = self.calculate_p(self.calculate_Pp() , DBase)
                gamma1 , gamma2 , gamma3 , gamma4 = self.calculate_gama()
                q1 = self.calculate_q1()
                q2 = self.calculate_q2()
                q3 = self.calculate_q3()
                if (q1 >= qcr):
                    q1 = qcr
                if (q2 >= qcr):
                    q2 = qcr
                if (q3 >= qcr):
                    q3 = qcr
                Qf1 = k1 * q1/2 * math.tan(math.radians(gamma1)) * p1 + k2 * (q2+q1)/2 * math.tan(math.radians(gamma2)) * p2 + k3 * (q3+q2)/2 * math.tan(math.radians(gamma3)) * p3 + k4 * (q3+qp)/2 * math.tan(math.radians(gamma4)) * p4
                return Qf1
        except :
            raise Exception("\u03C6"+str(self.n))
    
        
    def calculate_beta (self):
        if (self.n == 1):
            if (float(self.l1_c.text()) < 2.5):
                beta1 = 1
            else :
                beta1 = (1 + math.pow(float(self.l1_c.text()) , 2))/(1 + 7*math.pow(float(self.l1_c.text()) , 2))
            return beta1
        
        if (self.n == 2):
            if (float(self.l1_c.text()) < 2.5):
                beta1 = 1
            else :
                beta1 = (1 + math.pow(float(self.l1_c.text()) , 2))/(1 + 7*math.pow(float(self.l1_c.text()) , 2))
                
            if (float(self.l2_c.text()) < 2.5):
                beta2 = 1
            else :
                beta2 = (1 + math.pow(float(self.l2_c.text()) , 2))/(1 + 7*math.pow(float(self.l2_c.text()) , 2))
            return (beta1 , beta2)
        
        if (self.n == 3):
            if (float(self.l1_c.text()) < 2.5):
                beta1 = 1
            else :
                beta1 = (1 + math.pow(float(self.l1_c.text()) , 2))/(1 + 7*math.pow(float(self.l1_c.text()) , 2))
                
            if (float(self.l2_c.text()) < 2.5):
                beta2 = 1
            else :
                beta2 = (1 + math.pow(float(self.l2_c.text()) , 2))/(1 + 7*math.pow(float(self.l2_c.text()) , 2))

            if (float(self.l3_c.text()) < 2.5):
                beta3 = 1
            else :
                beta3 = (1 + math.pow(float(self.l3_c.text()) , 2))/(1 + 7*math.pow(float(self.l3_c.text()) , 2))
            return (beta1 , beta2 , beta3)
            
        if (self.n == 4):
            if (float(self.l1_c.text()) < 2.5):
                beta1 = 1
            else :
                beta1 = (1 + math.pow(float(self.l1_c.text()) , 2))/(1 + 7*math.pow(float(self.l1_c.text()) , 2))
                
            if (float(self.l2_c.text()) < 2.5):
                beta2 = 1
            else :
                beta2 = (1 + math.pow(float(self.l2_c.text()) , 2))/(1 + 7*math.pow(float(self.l2_c.text()) , 2))

            if (float(self.l3_c.text()) < 2.5):
                beta3 = 1
            else :
                beta3 = (1 + math.pow(float(self.l3_c.text()) , 2))/(1 + 7*math.pow(float(self.l3_c.text()) , 2))
                
            if (float(self.l4_c.text()) < 2.5):
                beta4 = 1
            else :
                beta4 = (1 + math.pow(float(self.l4_c.text()) , 2))/(1 + 7*math.pow(float(self.l4_c.text()) , 2))
            return (beta1 , beta2 , beta3 , beta4)
            
    def calculate_Qf2 (self , DBase):
        if (self.n == 1):
            beta1 = self.calculate_beta()
            p1 = self.calculate_p(self.calculate_Pp() , DBase)
            Qf2 = beta1 * float(self.l1_c.text()) * p1
            return Qf2
        if (self.n == 2):
            beta1 , beta2 = self.calculate_beta()
            p1 , p2 = self.calculate_p(self.calculate_Pp() , DBase)
            Qf2 = beta1 * float(self.l1_c.text()) * p1 + beta2 * float(self.l2_c.text()) * p2
            return Qf2
        if (self.n == 3):
            beta1 , beta2 , beta3 = self.calculate_beta()
            p1 , p2 , p3 = self.calculate_p(self.calculate_Pp() , DBase)
            Qf2 = beta1 * float(self.l1_c.text()) * p1 + beta2 * float(self.l2_c.text()) * p2 + beta3 * float(self.l3_c.text()) * p3
            return Qf2
        if (self.n == 4):
            beta1 , beta2 , beta3 , beta4 = self.calculate_beta()
            p1 , p2 , p3 , p4= self.calculate_p(self.calculate_Pp() , DBase )
            Qf2=beta1*float(self.l1_c.text()) * p1 + beta2 * float(self.l2_c.text()) * p2 + beta3 * float(self.l3_c.text()) * p3 + beta4 * float(self.l4_c.text()) * p4
            return Qf2
        else :
            return 0
    
    def calculate_Qf (self , Qf1 , Qf2):
        return (Qf1 + Qf2)
        
    def calculate_Qu (self , Qp , Qf):
        return (Qp + Qf)
    
    def calculate_Qall (self , Qp , Qf):
        return ( (Qp/float(self.otherChar_FOS_p.text())) + (Qf/float(self.otherChar_FOS_f.text())) )
    # this function put the result in the consule , under the inputs 
    # def process (self):
    #     self.choosingLayer()
    #     Ap = self.calculate_Ap()
    #     Pp = self.calculate_Pp()
    #     N = self.calculate_N()
    #     Nq = self.calculate_Nq(N)
    #     Nc = self.calculate_Nc(Nq)
    #     qp = self.calculate_qp()
    #     Qp = self.calculate_Qp (Nc , qp , Nq , Ap)
    #     Qf = self.calculate_Qf(self.calculate_Qf1() , self.calculate_Qf2())
    #     Qu = self.calculate_Qu(Qp , Qf)
    #     Qall = self.calculate_Qall(Qp , Qf)
    #     self.NqLabel = QLabel()
    #     self.NcLabel = QLabel()
    #     self.QpLabel = QLabel()
    #     self.QfLabel = QLabel()
    #     self.QuLabel = QLabel()
    #     self.QallLabel = QLabel()
    #     self.resultBox = QGroupBox("Results : ")
    #     self.resultPart = QFormLayout()

        
    #     self.NqLabel.setText("Nq = "  + "%.3f" %Nq)
    #     self.NcLabel.setText("Nc = "  + "%.3f" %Nc)
    #     self.QpLabel.setText("Qp = " + "%.3f" %Qp)
    #     self.QfLabel.setText("Qf = " + "%.3f" %Qf)
    #     self.QuLabel.setText("Qu = " + "%.3f" %Qu)
    #     self.QallLabel.setText("Qall = " + "%.3f" %Qall)
        

        
    #     self.resultPart.addRow (self.NqLabel)
    #     self.resultPart.addRow (self.NcLabel)
    #     self.resultPart.addRow (self.QpLabel)
    #     self.resultPart.addRow (self.QfLabel)
    #     self.resultPart.addRow (self.QuLabel)
    #     self.resultPart.addRow (self.QallLabel)

        
        
    #     self.resultBox.setLayout(self.resultPart)
        
        
    #     self.module2.layout.addWidget(self.resultBox , 2 , 0 )
        
    def drawGraph(self):

        if self.handelInvalidFOS() :
            return
        if self.handelInvalidfi():
            return
        try:

            self.graphWindow = QDialog(self)
            self.graphWindow.setWindowTitle("Graphs")
            self.graphWindowLayout = QGridLayout()
            self.graphWindow.setLayout(self.graphWindowLayout)
            self.graphWindow.setFixedSize(400 , 650)
            

            # Qp chart y and x
            QpChartX = []
            QpChartY = []
            # Qf chart y and x
            QfChartX = []
            QfChartY = []
            # Qu chart y and x
            QuChartX =[]
            QuChartY = []
            # Qall chart y and x
            QallChartX = []
            QallChartY = []
            


            x = 0
            maxExpectedDepthOfPile =  float(self.pileChar_pileLen.text()) + 5
            # q(u) graph :
            while (maxExpectedDepthOfPile >= x):
                QpChartX.append(x)
                QfChartX.append(x)
                QuChartX.append (x)
                QallChartX.append (x)
                x += float(self.pileLen_)
            
            
            QpChartX.sort()
            QfChartX.sort()
            QuChartX.sort()
            QallChartX.sort()



            
            for i_ in QuChartX:      

                self.choosingLayer(i_)
                self.choosingLayerForWater()
                Ap = self.calculate_Ap()
                Pp = self.calculate_Pp()
                N = self.calculate_N()
                Nq = self.calculate_Nq(N)
                Nc = self.calculate_Nc(Nq)
                qp = self.calculate_q(i_)
                Qp = self.calculate_Qp (Nc , qp , Nq , Ap)
                Qf = self.calculate_Qf(self.calculate_Qf1(i_) , self.calculate_Qf2(i_))
                Qu = self.calculate_Qu(Qp , Qf)
                Qall = self.calculate_Qall(Qp , Qf)

                QpChartY.append (Qp)
                QfChartY.append (Qf)
                QuChartY.append (Qu)
                QallChartY.append (Qall)


            shape , tool = self.passShapeToWindow(QpChartY , QpChartX , '#F21515' , QfChartY , QfChartX , '#BB15F2'  , QuChartY , QuChartX , '#216CEF' , QallChartY , QallChartX , '#33F12A')

            self.graphWindowLayout.addWidget(tool, 0 , 1)
            self.graphWindowLayout.addWidget(shape , 1 , 1)
            
            
            
            self.graphWindow.exec()
        except Exception as e:
       
            self.inputError(str(e))






    
    def passShapeToWindow (self , XQp , YQp , colorQp , XQf , YQf , colorQf , XQu , YQu , colorQu , XQall , YQall , colorQall):
        QperPile = Figure (figsize=(3 , 12) , dpi=100)
        theAxes = QperPile.add_subplot(111)
        
        theAxes.plot (XQp , YQp , marker = '.' , color=colorQp , label="Qp(ton)")
        theAxes.plot (XQf , YQf , marker = '.' , color=colorQf , label="Qf(ton)")
        theAxes.plot (XQu , YQu , marker = '.' , color=colorQu , label="Qu(ton)")
        theAxes.plot (XQall , YQall , marker = '.' , color=colorQall , label="Qall(ton)")
        theAxes.legend()


        theAxes.invert_yaxis()
        theAxes.xaxis.tick_top()
        theShape = FigureCanvas(QperPile)
        tool = NavigationToolbar(theShape, self)

        theAxes.grid(linewidth=0.5, alpha=0.5)
        theAxes.set_ylabel('Depth (m)')




        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        theShape.mpl_connect('motion_notify_event', on_mouse_move)

        return theShape , tool



    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.module2 = QWidget()
        self.tabs.resize(300,200)


        #help button 
        self.module2Help = QToolButton()
        self.module2Help.setText("Help")  
        self.module2Help.setIconSize(QSize(20 , 20))
        self.module2Help.clicked.connect(self.module2HelpFunction)




        # Add tabs
        self.tabs.addTab(self.module2,"Module 2")
        




        # Create first tab
        self.module2.layout = QVBoxLayout(self)
        self.module2.layout.addWidget(self.module2Help, alignment = Qt.AlignRight)

        self.input_datas (self.module2.layout)
        ButtonLayout = QHBoxLayout()
        self.graphButtonFunction(ButtonLayout)
        self.resetButtonFunction(ButtonLayout)
        self.module2.layout.addLayout(ButtonLayout)


        self.module2.setLayout(self.module2.layout)
        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.module2.setLayout(self.module2.layout)
        

        
        
    def module2HelpFunction(self):
        #pixmap = QPixmap('module3Help1.png')
        image_label = QLabel()
        #image_label.setPixmap(pixmap)


        message_box = QMessageBox()
        #message_box.layout().addWidget(image_label)
        message_box.setWindowTitle('Module 3 Help')
        about = "شما در حال استفاده از ماژول محاسبه ظرفیت باربری پی عمیق از نرم افزار GeOnion هستید."
        about2 = "به طور کلی امروزه از شمع های فولادی لوله‌ای، بتنی پیش ساخته معمولی، بتنی پیش ساخته پیش تنیده (شمع های سانتریفیوژ) و شمعهای بتنی درجا ساخت استفاده می‌شود. اگرچه در عمل اجرای یک پی عمیق یا شمع غالبا دارای هزینه بیشتری در مقایسه با پیهای سطحی متعارف است، با این حال هنگامی که (1) خاک زیر پی از باربری مناسب برخوردار نیست (2) نشست پی مشکل ساز است و یا (3) امکان اجرای پی سطحی وجود ندارد، استفاده از شمع به عنوان یک راه حل مناسب قابل طرح است. نسبت طول (عمق) به عرض (قطر) در این نوع پیها در مقایسه با پیهای سطحی بسیار قابل توجه است. اگر طول و قطر یک شمع به ترتیب L و B نامیده شوند ، برای پیهای عمیق نسبت L/B معمولا بیشتر از 10 تعریف می گردد."
        about3 = "باربری محوری یک شمع تحت بارهای وارد بر آن، از طریق مقاومت جداره Qf و مقاومت انتهایی Qp تامین میگردد. عملکرد باربری جداره و باربری انتهایی شمع ها بستگی به شرایط بارگذاری و شرایط بستر مورد نظر دارد. با توجه به شرایط بارگذاری، یک شمع ممکن است تحت فشار یا کشش قرار گیرد."



        message_box.setText(about + "\n\n    " + about2 + "\n\n    " + about3 + "\n\n    " )
        message_box.exec_()
        
        
    def handelInvalidFOS(self):
        if float(self.otherChar_FOS_p.text()) < 1 :
            error_dialog = QErrorMessage()
            error_dialog.showMessage('مقدار FOS-p وارد شده نامعتبر است')
            error_dialog.exec_()
            return (1)

        if float(self.otherChar_FOS_f.text()) < 1 :
            error_dialog = QErrorMessage()
            error_dialog.showMessage('مقدار FOS-f وارد شده نامعتبر است')
            error_dialog.exec_()
            return (1)
        return 0
    def handelInvalidfi (self):
        if (self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False and float(self.l1_fi.text()) < 0):
            error_dialog = QErrorMessage()
            error_dialog.showMessage(u'مقدار \u03C6 وارد شده نامعتبر است')
            error_dialog.exec_()
            return 1
       
        if (self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False and (float(self.l1_fi.text()) < 0 or float(self.l2_fi.text()) < 0) ):
            error_dialog = QErrorMessage()
            error_dialog.showMessage(u'مقدار \u03C6 وارد شده نامعتبر است')
            error_dialog.exec_()
            return 1

        if (self.l3Box.isEnabled() == True and self.l4Box.isEnabled() == False and (float(self.l1_fi.text()) < 0 or float(self.l2_fi.text()) < 0 or float(self.l3_fi.text()) < 0) ):
            error_dialog = QErrorMessage()
            error_dialog.showMessage(u'مقدار \u03C6 وارد شده نامعتبر است')
            error_dialog.exec_()
            return 1


        if (self.l4Box.isEnabled() == True and (float(self.l1_fi.text()) < 0 or float(self.l2_fi.text()) < 0 or float(self.l3_fi.text()) < 0 or float(self.l4_fi.text()) < 0) ):
            error_dialog = QErrorMessage()
            error_dialog.showMessage(u'مقدار \u03C6 وارد شده نامعتبر است')
            error_dialog.exec_()
            return 1

        return 0
    
    
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
