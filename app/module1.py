from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QLabel, QMainWindow, QComboBox, \
    QWidget, QHBoxLayout, QVBoxLayout, QGridLayout , QTabWidget , QToolButton , QMessageBox , QDesktopWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGroupBox, QStackedLayout , QDialog , QErrorMessage , QToolTip
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont, QPalette, QColor , QPixmap , QCursor
from PyQt5.QtCore import Qt,QSize 
import sys , math


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.pyplot import figure


class Module1(QWidget):
    
    def __init__(self , parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        self.module1 = QWidget()
        

        
        self.module1Help = QToolButton()
        self.module1Help.setText("Help")  
        self.module1Help.setIconSize(QSize(20 , 20))
        self.module1Help.clicked.connect(self.module1HelpFunction)
        #self.module1Help.clicked.connect(self.module1HelpFunction2)
        

        # Create first tab

        # process Button
        
        ButtonLayout = QHBoxLayout()
        self.graphButtonFunction(ButtonLayout)
        self.resetButtonFunction(ButtonLayout)


   
        

        self.module1.layout = QGridLayout(self)
        self.module1.layout.addWidget(self.module1Help,0,0 , alignment = Qt.AlignRight)
        self.layout.addWidget(self.module1)
        self.module1.setLayout(self.module1.layout)


        self.inputData(self.module1.layout)

     
        self.module1.layout.addLayout(ButtonLayout , 3 , 0)

        self.setLayout(self.layout)
        self.logo = QLabel(self)
        self.pixmap = QPixmap('./logo.PNG')
        self.pixmap = self.pixmap.scaled(600,600) 
        self.logo.setPixmap(self.pixmap)

        #self.logo.resize(self.pixmap.width(),self.pixmap.height())
        self.layout.addWidget(self.logo)


        self.setLayout(self.layout)
    

    def drawGraph_terzaghi (self):
        self.choosingLayer()
        self.choosingLayerForWater()
        #print(self.calculate_q_terzaghi(float(self.DBase.text())))

        self.graphWindow = QDialog(self)
        self.graphWindow.setWindowTitle("Graphs")
        self.graphWindowLayout = QGridLayout()
        self.graphWindow.setLayout(self.graphWindowLayout)
        
        
        # q(u) per B chart :
        bChartX = []
        bChartY = []
        
        bChartX.append(float(self.B.text()))
        for i in range (1 , self.steps + 1):
            bChartX.append (float(self.B.text()) + (i * float(self.BStep.text())))
            bChartX.append (float(self.B.text()) - (i * float(self.BStep.text())))
        
        bChartX.sort()
            
        for B in bChartX :
            qu = self.calculate_qu_terzaghi(B , self.calculate_Nc_terzaghi(self.calculate_Nq_terzaghi()) , self.calculate_Sc_terzaghi(B , float(self.L.text())) , self.calculate_q_terzaghi (float(self.DBase.text())), self.calculate_Nq_terzaghi() , self.calculate_Sq_terzaghi() , self.calculate_Ngamma_terzaghi(self.calculate_KPgamma_terzaghi()) , self.calculate_Sgamma_terzaghi(B, float(self.L.text())))
            qall = self.calculate_qall_terzaghi(qu)
            bChartY.append(qall)
        
                #[13.628,15.755,17.842,19.890,21.898]
        
        qPerB = Figure(figsize=(5, 3), dpi=100 )
        qPerB.text(0.4 , 0.9 ,"qall per B steps", fontsize=10, color='silver')
        qPerB_axes = qPerB.add_subplot(111)


        # static line in graph
        qPerB_axes.axhline(y = bChartY[4], color='#3DF1E8', linestyle='--')
        qPerB_axes.axvline(x = bChartX[4], color='#3DF1E8', linestyle='--')
        ###


        qPerB_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerB_axes.set_xlabel ("B steps")
        qPerB_axes.plot(bChartX, bChartY, marker = "o" )
        qPerB_axes.grid(linewidth=0.5, alpha=0.5)
        qPerB_shape = FigureCanvas(qPerB)
        tool = NavigationToolbar(qPerB_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 0)
        self.graphWindowLayout.addWidget(qPerB_shape , 1 , 0)
        
                
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        qPerB_shape.mpl_connect('motion_notify_event', on_mouse_move)




        
        dChartX = []
        dChartY = []
                
        dChartX.append(float(self.DBase.text()))
        for i in range (1 , self.steps + 1):
            dChartX.append (float(self.DBase.text()) + (i * float(self.DStep.text())))
            dChartX.append (float(self.DBase.text()) - (i * float(self.DStep.text())))

        dChartX.sort()
        
        for D in dChartX :
            qu = self.calculate_qu_terzaghi(float(self.B.text()) , self.calculate_Nc_terzaghi(self.calculate_Nq_terzaghi()) , self.calculate_Sc_terzaghi(float(self.B.text()) , float(self.L.text())) , self.calculate_q_terzaghi (D), self.calculate_Nq_terzaghi() , self.calculate_Sq_terzaghi() , self.calculate_Ngamma_terzaghi(self.calculate_KPgamma_terzaghi()) , self.calculate_Sgamma_terzaghi(float(self.B.text()), float(self.L.text())))
            qall = self.calculate_qall_terzaghi(qu)
            dChartY.append(qall)
        
        
        qPerD = Figure(figsize=(5, 3), dpi=100)
        qPerD.text(0.4 , 0.9 ,"qall per D base steps", fontsize=10, color='silver')
        qPerD_axes = qPerD.add_subplot(111)

        # static line in graph
        qPerD_axes.axhline(y = dChartY[4], color='#56E419', linestyle='--')
        qPerD_axes.axvline(x = dChartX[4], color='#56E419', linestyle='--')
        ###
        
        
        
        qPerD_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerD_axes.set_xlabel ("D Base steps")
        qPerD_axes.plot(dChartX, dChartY, marker = "o" , color = "green")
        qPerD_axes.grid(linewidth=0.5, alpha=0.5)

        qPerD_shape = FigureCanvas(qPerD)
        tool = NavigationToolbar(qPerD_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 1)
        self.graphWindowLayout.addWidget(qPerD_shape , 1 , 1)
        
        
        qPerD_shape.mpl_connect('motion_notify_event', on_mouse_move)


        lChartX = []
        lChartY = []
        
        lChartX.append(float(self.L.text()))
        for i in range (1 , self.steps + 1):
            lChartX.append (float(self.L.text()) + (i * float(self.LStep.text())))
            lChartX.append (float(self.L.text()) - (i * float(self.LStep.text())))
        
        lChartX.sort()
            
        for L in lChartX :
            qu = self.calculate_qu_terzaghi(float(self.B.text()) , self.calculate_Nc_terzaghi(self.calculate_Nq_terzaghi()) , self.calculate_Sc_terzaghi(float(self.B.text()) , L ) , self.calculate_q_terzaghi (float(self.DBase.text())), self.calculate_Nq_terzaghi() , self.calculate_Sq_terzaghi() , self.calculate_Ngamma_terzaghi(self.calculate_KPgamma_terzaghi()) , self.calculate_Sgamma_terzaghi(float(self.B.text()), L))
            qall = self.calculate_qall_terzaghi(qu)
            lChartY.append(qall)
        
                #[13.628,15.755,17.842,19.890,21.898]
        
        qPerL = Figure(figsize=(5, 3), dpi=100)
        qPerL.text(0.4 , 0.9 ,"qall per L steps", fontsize=10, color='silver')
        qPerL_axes = qPerL.add_subplot(111)


        # static line in graph
        qPerL_axes.axhline(y = lChartY[4], color='#FB903D', linestyle='--')
        qPerL_axes.axvline(x = lChartX[4], color='#FB903D', linestyle='--')
        ###

        qPerL_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerL_axes.set_xlabel ("L steps")
        qPerL_axes.plot(lChartX, lChartY, marker = "o" , color = "red")
        qPerL_axes.grid(linewidth=0.5, alpha=0.5)

        qPerL_shape = FigureCanvas(qPerL)
        tool = NavigationToolbar(qPerL_shape, self)
        self.graphWindowLayout.addWidget(tool, 2 , 0)
        self.graphWindowLayout.addWidget(qPerL_shape , 3 , 0)
        
        qPerL_shape.mpl_connect('motion_notify_event', on_mouse_move)





        self.graphWindow.exec()

    def drawGraph_meyerhof(self):

        self.choosingLayer()
        self.choosingLayerForWater()
        self.graphWindow = QDialog(self)
        self.graphWindow.setWindowTitle("Graphs")
        self.graphWindowLayout = QGridLayout()
        self.graphWindow.setLayout(self.graphWindowLayout)
        
        
        # q(u) per B chart :
        bChartX = []
        bChartY = []
        beta = self.calculate_beta_meyerhof()
        
        bChartX.append(float(self.B.text()))
        for i in range (1 , self.steps + 1):
            bChartX.append (float(self.B.text()) + (i * float(self.BStep.text())))
            bChartX.append (float(self.B.text()) - (i * float(self.BStep.text())))
        
        bChartX.sort()
            
        for B in bChartX :
            qu = self.calculate_qu_meyerhof (self.calculate_Nc_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sc_meyerhof(self.calculate_KP_meyerhof(), float(self.L.text()) , B) , self.calculate_dc_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , B) , self.calculate_ic_meyerhof(beta) , self.calculate_q_terzaghi(float(self.DBase.text())) , self.calculate_Nq_meyerhof() , self.calculate_Sq_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()) , B) , self.calculate_dq_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , B) , self.calculate_iq_meyerhof(beta), B,self.calculate_Ngamma_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()),B) , self.calculate_dgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()),B) , self.calculate_igamma_meyerhof(beta) )
            qall = self.calculate_qall_terzaghi(qu)
            bChartY.append(qall)
        
                #[13.628,15.755,17.842,19.890,21.898]
        
        qPerB = Figure(figsize=(5, 3), dpi=100 )
        qPerB.text(0.4 , 0.9 ,"qall per B steps", fontsize=10, color='silver')
        qPerB_axes = qPerB.add_subplot(111)

        # static line in graph
        qPerB_axes.axhline(y = bChartY[4], color='#3DF1E8', linestyle='--')
        qPerB_axes.axvline(x = bChartX[4], color='#3DF1E8', linestyle='--')
        ###

        qPerB_axes.grid(linewidth=0.5, alpha=0.5)


        qPerB_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerB_axes.set_xlabel ("B steps")
        qPerB_axes.plot(bChartX, bChartY, marker = "o" )
        qPerB_shape = FigureCanvas(qPerB)
        tool = NavigationToolbar(qPerB_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 0)
        self.graphWindowLayout.addWidget(qPerB_shape , 1 , 0)
        
                        
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        qPerB_shape.mpl_connect('motion_notify_event', on_mouse_move)



        
        dChartX = []
        dChartY = []
                
        dChartX.append(float(self.DBase.text()))
        for i in range (1 , self.steps + 1):
            dChartX.append (float(self.DBase.text()) + (i * float(self.DStep.text())))
            dChartX.append (float(self.DBase.text()) - (i * float(self.DStep.text())))
        
        dChartX.sort()
        
        for D in dChartX :
            qu = self.calculate_qu_meyerhof (self.calculate_Nc_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sc_meyerhof(self.calculate_KP_meyerhof(), float(self.L.text()) , float (self.B.text()) ) , self.calculate_dc_meyerhof(self.calculate_KP_meyerhof() , D , float (self.B.text())) , self.calculate_ic_meyerhof(beta) , self.calculate_q_terzaghi(D) , self.calculate_Nq_meyerhof() , self.calculate_Sq_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()) , float (self.B.text()) ) , self.calculate_dq_meyerhof(self.calculate_KP_meyerhof() , D , float (self.B.text()) ) ,self.calculate_iq_meyerhof(beta),float(self.B.text()), self.calculate_Ngamma_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()) ,float (self.B.text()) ) , self.calculate_dgamma_meyerhof(self.calculate_KP_meyerhof() , D , float (self.B.text()) ) , self.calculate_igamma_meyerhof(beta) )
            qall = self.calculate_qall_terzaghi(qu)
            dChartY.append(qall)
        
        
        qPerD = Figure(figsize=(5, 3), dpi=100)
        qPerD.text(0.4 , 0.9 ,"qall per D base steps", fontsize=10, color='silver')
        qPerD_axes = qPerD.add_subplot(111)

        # static line in graph
        qPerD_axes.axhline(y = dChartY[4], color='#56E419', linestyle='--')
        qPerD_axes.axvline(x = dChartX[4], color='#56E419', linestyle='--')
        ###
        

        qPerD_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerD_axes.set_xlabel ("D Base steps")
        qPerD_axes.plot(dChartX, dChartY, marker = "o" , color = "green")
        qPerD_shape = FigureCanvas(qPerD)
        tool = NavigationToolbar(qPerD_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 1)
        self.graphWindowLayout.addWidget(qPerD_shape , 1 , 1)
        qPerD_axes.grid(linewidth=0.5, alpha=0.5)


        qPerD_shape.mpl_connect('motion_notify_event', on_mouse_move)

        
        lChartX = []
        lChartY = []
        
        lChartX.append(float(self.L.text()))
        for i in range (1 , self.steps + 1):
            lChartX.append (float(self.L.text()) + (i * float(self.LStep.text())))
            lChartX.append (float(self.L.text()) - (i * float(self.LStep.text())))
        
        lChartX.sort()
        
        
        for L in lChartX :
            qu = self.calculate_qu_meyerhof (self.calculate_Nc_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sc_meyerhof(self.calculate_KP_meyerhof(), L , float (self.B.text()) ) , self.calculate_dc_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float (self.B.text())) , self.calculate_ic_meyerhof(beta) , self.calculate_q_terzaghi(float(self.DBase.text())) , self.calculate_Nq_meyerhof() , self.calculate_Sq_meyerhof(self.calculate_KP_meyerhof() , L , float (self.B.text()) ) , self.calculate_dq_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float (self.B.text()) ), self.calculate_iq_meyerhof(beta) , float(self.B.text()),self.calculate_Ngamma_meyerhof(self.calculate_Nq_meyerhof()) , self.calculate_Sgamma_meyerhof(self.calculate_KP_meyerhof() , L ,float (self.B.text()) ) , self.calculate_dgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float (self.B.text()) ) , self.calculate_igamma_meyerhof(beta) )
            qall = self.calculate_qall_terzaghi(qu)
            lChartY.append(qall)
        
                #[13.628,15.755,17.842,19.890,21.898]
        
        qPerL = Figure(figsize=(5, 3), dpi=100)
        qPerL.text(0.4 , 0.9 ,"qall per L steps", fontsize=10, color='silver')
        qPerL_axes = qPerL.add_subplot(111)
        
              # static line in graph
        qPerL_axes.axhline(y = lChartY[4], color='#FB903D', linestyle='--')
        qPerL_axes.axvline(x = lChartX[4], color='#FB903D', linestyle='--')

            ###



        qPerL_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerL_axes.set_xlabel ("L steps")
        qPerL_axes.plot(lChartX, lChartY, marker = "o" , color="red")
        qPerL_shape = FigureCanvas(qPerL)
        tool = NavigationToolbar(qPerL_shape, self)
        self.graphWindowLayout.addWidget(tool, 2 , 0)
        self.graphWindowLayout.addWidget(qPerL_shape , 3 , 0)
        qPerL_axes.grid(linewidth=0.5, alpha=0.5)


        qPerL_shape.mpl_connect('motion_notify_event', on_mouse_move)

        
        self.graphWindow.exec()


    def drawGraph_hansen(self):
        
        self.choosingLayer()
        self.choosingLayerForWater()
        self.graphWindow = QDialog(self)
        self.graphWindow.setWindowTitle("Graphs")
        self.graphWindowLayout = QGridLayout()
        self.graphWindow.setLayout(self.graphWindowLayout)
        
        
        # q(u) per B chart :
        bChartX = []
        bChartY = []


        bChartX.append(float(self.B.text()))
        for i in range (1 , self.steps + 1):
            bChartX.append (float(self.B.text()) + (i * float(self.BStep.text())))
            bChartX.append (float(self.B.text()) - (i * float(self.BStep.text())))
        
        bChartX.sort()
            
        for B in bChartX :
            Nq = self.calculate_Nq_hansen()
            Nc = self.calculate_Nc_hansen(self.calculate_Nq_hansen())
            Ngamma = self.calculate_Ngamma_hansen(self.calculate_Nq_hansen())
            Sc = self.calculate_Sc_hansen(self.calculate_Nq_hansen() , self.calculate_Nc_hansen(Nq) , B , float (self.L.text()))
            Sq = self.calculate_Sq_hansen( B , float (self.L.text()) )
            Sgamma = self.calculate_Sgamma_hansen (B , float (self.L.text()))
            dc = self.calculate_dc_hansen( float(self.DBase.text()) , B)
            dq = self.calculate_dq_hansen(float(self.DBase.text()) , B)
            dgamma = self.calculate_dgamma_hansen()
            bc = self.calculate_bc_hansen()
            bq = self.calculate_bq_hansen()
            bgamma = self.calculate_ggamma_hansen()
            gc = self.calculate_gc_hansen()
            gq = self.calculate_gq_hansen()
            ggamma = self.calculate_ggamma_hansen()
            ca = self.calculate_ca_hansen()
            Af = self.calculate_Af_hansen(B , float (self.L.text()))
            m = self.calculate_m_hansen(self.calculate_mB_hansen(B , float (self.L.text())) , self.calculate_mL_hansen(B , float (self.L.text())) )
            iq = self.calculate_iq_hansen(Af , ca , m)
            igamma = self.calculate_igamma_hansen(Af , ca , m)
            ic = self.calculate_ic_hansen(iq , Nq)
            q = self.calculate_q_terzaghi(float(self.DBase.text()))
            
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)

            
            bChartY.append(qall)
            

        
        qPerB = Figure(figsize=(5, 3), dpi=100 )
        qPerB.text(0.4 , 0.9 ,"qall per B steps", fontsize=10, color='silver')
        qPerB_axes = qPerB.add_subplot(111)

        # static line in graph
        qPerB_axes.axhline(y = bChartY[4], color='#3DF1E8', linestyle='--')
        qPerB_axes.axvline(x = bChartX[4], color='#3DF1E8', linestyle='--')
        ###


        qPerB_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerB_axes.set_xlabel ("B steps")
        qPerB_axes.plot(bChartX, bChartY, marker = "o" )
        qPerB_shape = FigureCanvas(qPerB)
        tool = NavigationToolbar(qPerB_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 0)
        self.graphWindowLayout.addWidget(qPerB_shape , 1 , 0)
        qPerB_axes.grid(linewidth=0.5, alpha=0.5)

        
                
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        qPerB_shape.mpl_connect('motion_notify_event', on_mouse_move)


        dChartX = []
        dChartY = []
                
        dChartX.append(float(self.DBase.text()))
        for i in range (1 , self.steps + 1):
            dChartX.append (float(self.DBase.text()) + (i * float(self.DStep.text())))
            dChartX.append (float(self.DBase.text()) - (i * float(self.DStep.text())))
        
        dChartX.sort()
        
        for D in dChartX :
            Nq = self.calculate_Nq_hansen()
            Nc = self.calculate_Nc_hansen(self.calculate_Nq_hansen())
            Ngamma = self.calculate_Ngamma_hansen(self.calculate_Nq_hansen())
            Sc = self.calculate_Sc_hansen(self.calculate_Nq_hansen() , self.calculate_Nc_hansen(Nq) , float (self.B.text()) , float (self.L.text()))
            Sq = self.calculate_Sq_hansen( float (self.B.text()) , float (self.L.text()) )
            Sgamma = self.calculate_Sgamma_hansen (float (self.B.text()) , float (self.L.text()))
            dc = self.calculate_dc_hansen( D , float (self.B.text()))
            dq = self.calculate_dq_hansen(D , float (self.B.text()))
            dgamma = self.calculate_dgamma_hansen()
            bc = self.calculate_bc_hansen()
            bq = self.calculate_bq_hansen()
            bgamma = self.calculate_ggamma_hansen()
            gc = self.calculate_gc_hansen()
            gq = self.calculate_gq_hansen()
            ggamma = self.calculate_ggamma_hansen()
            ca = self.calculate_ca_hansen()
            Af = self.calculate_Af_hansen(float (self.B.text()) , float (self.L.text()))
            m = self.calculate_m_hansen(self.calculate_mB_hansen(float (self.B.text()) , float (self.L.text())) , self.calculate_mL_hansen(float (self.B.text()) , float (self.L.text())) )
            iq = self.calculate_iq_hansen(Af , ca , m)
            igamma = self.calculate_igamma_hansen(Af , ca , m)
            ic = self.calculate_ic_hansen(iq , Nq)
            q = self.calculate_q_terzaghi(D)
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)
                
            dChartY.append(qall)
            
        
        qPerD = Figure(figsize=(5, 3), dpi=100)
        qPerD.text(0.4 , 0.9 ,"qall per D base steps", fontsize=10, color='silver')
        qPerD_axes = qPerD.add_subplot(111)
        
        
        # static line in graph
        qPerD_axes.axhline(y = dChartY[4], color='#56E419', linestyle='--')
        qPerD_axes.axvline(x = dChartX[4], color='#56E419', linestyle='--')
        ###
        


        qPerD_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerD_axes.set_xlabel ("D Base steps")
        qPerD_axes.plot(dChartX, dChartY, marker = "o" , color = "green")
        qPerD_shape = FigureCanvas(qPerD)
        tool = NavigationToolbar(qPerD_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 1)
        self.graphWindowLayout.addWidget(qPerD_shape , 1 , 1)
        qPerD_shape.mpl_connect('motion_notify_event', on_mouse_move)
        qPerD_axes.grid(linewidth=0.5, alpha=0.5)


        
        lChartX = []
        lChartY = []
        
        lChartX.append(float(self.L.text()))
        for i in range (1 , self.steps + 1):
            lChartX.append (float(self.L.text()) + (i * float(self.LStep.text())))
            lChartX.append (float(self.L.text()) - (i * float(self.LStep.text())))
        
        lChartX.sort()
        
        
        for L in lChartX :
            Nq = self.calculate_Nq_hansen()
            Nc = self.calculate_Nc_hansen(self.calculate_Nq_hansen())
            Ngamma = self.calculate_Ngamma_hansen(self.calculate_Nq_hansen())
            Sc = self.calculate_Sc_hansen(self.calculate_Nq_hansen() , self.calculate_Nc_hansen(Nq) , float (self.B.text()) , L)
            Sq = self.calculate_Sq_hansen( float (self.B.text()) , L )
            Sgamma = self.calculate_Sgamma_hansen (float (self.B.text()) , L)
            dc = self.calculate_dc_hansen( float(self.DBase.text()) , float (self.B.text()))
            dq = self.calculate_dq_hansen(float(self.DBase.text()) , float (self.B.text()))
            dgamma = self.calculate_dgamma_hansen()
            bc = self.calculate_bc_hansen()
            bq = self.calculate_bq_hansen()
            bgamma = self.calculate_ggamma_hansen()
            gc = self.calculate_gc_hansen()
            gq = self.calculate_gq_hansen()
            ggamma = self.calculate_ggamma_hansen()
            ca = self.calculate_ca_hansen()
            Af = self.calculate_Af_hansen(float (self.B.text()) , L)
            m = self.calculate_m_hansen(self.calculate_mB_hansen(float (self.B.text()) , L) , self.calculate_mL_hansen(float (self.B.text()) , L) )
            iq = self.calculate_iq_hansen(Af , ca , m)
            igamma = self.calculate_igamma_hansen(Af , ca , m)
            ic = self.calculate_ic_hansen(iq , Nq)
            q = self.calculate_q_terzaghi(float(self.DBase.text()))
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)

            lChartY.append(qall)
        
            
        
        qPerL = Figure(figsize=(5, 3), dpi=100)
        qPerL.text(0.4 , 0.9 ,"qall per L steps", fontsize=10, color='silver')
        qPerL_axes = qPerL.add_subplot(111)
              # static line in graph
        qPerL_axes.axhline(y = lChartY[4], color='#FB903D', linestyle='--')
        qPerL_axes.axvline(x = lChartX[4], color='#FB903D', linestyle='--')
        ###
        qPerL_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerL_axes.set_xlabel ("L steps")
        qPerL_axes.plot(lChartX, lChartY, marker = "o" , color="red")
        qPerL_shape = FigureCanvas(qPerL)
        qPerL_axes.grid(linewidth=0.5, alpha=0.5)

        tool = NavigationToolbar(qPerL_shape, self)
        self.graphWindowLayout.addWidget(tool, 2 , 0)
        self.graphWindowLayout.addWidget(qPerL_shape , 3 , 0)
        
        qPerL_shape.mpl_connect('motion_notify_event', on_mouse_move)

        
        
        self.graphWindow.exec()




    


    def drawGraph_vesic(self):
        
        self.choosingLayer()
        self.choosingLayerForWater()
        self.graphWindow = QDialog(self)
        # screen_geometry = QDesktopWidget().availableGeometry()
        # self.graphWindow.move(screen_geometry.right() - 500, screen_geometry.top())
        self.graphWindow.setWindowTitle("Graphs")
        self.graphWindowLayout = QGridLayout()
        self.graphWindow.setLayout(self.graphWindowLayout)
        
        
        # q(u) per B chart :
        bChartX = []
        bChartY = []


        bChartX.append(float(self.B.text()))
        for i in range (1 , self.steps + 1):
            bChartX.append (float(self.B.text()) + (i * float(self.BStep.text())))
            bChartX.append (float(self.B.text()) - (i * float(self.BStep.text())))
        
        bChartX.sort()
            
        for B in bChartX :
                    
                    
            Nq = self.calculate_Nq_vesic()
            Nc = self.calculate_Nc_vesic(Nq)
            Ngamma = self.calculate_Ngamma_vesic(Nq)
            Sc = self.calculate_Sc_vesic(Nq , Nc ,B , float (self.L.text()))
            Sq = self.calculate_Sq_vesic(B, float (self.L.text()) )
            Sgamma = self.calculate_Sgamma_vesic (B, float (self.L.text()))
            dc = self.calculate_dc_vesic( float(self.DBase.text()) , B)
            dq = self.calculate_dq_vesic(float(self.DBase.text()) , B)
            dgamma = self.calculate_dgamma_vesic()
            bc = self.calculate_bc_vesic()
            bq = self.calculate_bq_vesic()
            bgamma = self.calculate_ggamma_vesic()
            ca = self.calculate_ca_vesic()
            Af = self.calculate_Af_vesic(B, float(self.L.text()))
            mB = self.calculate_mB_vesic(B, float(self.L.text()))
            mL = self.calculate_mL_vesic(B , float(self.L.text()))
            m = self.calculate_m_vesic(mB , mL)
            iq = self.calculate_iq_vesic(Af , ca , m)
            igamma = self.calculate_igamma_vesic( Af , ca , m)
            ic = self.calculate_ic_vesic(iq , Nq)
            gc = self.calculate_gc_vesic ( iq)
            gq = self.calculate_gq_vesic ()
            ggamma = self.calculate_ggamma_vesic()
            q = self.calculate_q_terzaghi(float(self.DBase.text()))
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)

            bChartY.append(qall)
            

        
        qPerB = Figure(figsize=(5, 3), dpi=100 )
        qPerB.text(0.4 , 0.9 ,"qall per B steps", fontsize=10, color='silver')
        qPerB_axes = qPerB.add_subplot(111)
        qPerB_axes.grid(linewidth=0.5, alpha=0.5)


        # static line in graph
        qPerB_axes.axhline(y = bChartY[4], color='#3DF1E8', linestyle='--')
        qPerB_axes.axvline(x = bChartX[4], color='#3DF1E8', linestyle='--')
        ###

        qPerB_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerB_axes.set_xlabel ("B steps")
        qPerB_axes.plot(bChartX, bChartY, marker = "o" )
        qPerB_shape = FigureCanvas(qPerB)
        tool = NavigationToolbar(qPerB_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 0)
        self.graphWindowLayout.addWidget(qPerB_shape , 1 , 0)
        
        
        def on_mouse_move(event):
            if event.xdata is not None and event.ydata is not None:
                tooltip_text = f'({event.xdata:.2f}, {event.ydata:.2f})'
                QToolTip.showText(QCursor.pos(), tooltip_text)

        qPerB_shape.mpl_connect('motion_notify_event', on_mouse_move)






        dChartX = []
        dChartY = []
                
        dChartX.append(float(self.DBase.text()))
        for i in range (1 , self.steps + 1):
            dChartX.append (float(self.DBase.text()) + (i * float(self.DStep.text())))
            dChartX.append (float(self.DBase.text()) - (i * float(self.DStep.text())))
        
        dChartX.sort()
        
        for D in dChartX :
                        
            Nq = self.calculate_Nq_vesic()
            Nc = self.calculate_Nc_vesic(Nq)
            Ngamma = self.calculate_Ngamma_vesic(Nq)
            Sc = self.calculate_Sc_vesic(Nq , Nc , float (self.B.text()) , float (self.L.text()))
            Sq = self.calculate_Sq_vesic( float (self.B.text()) , float (self.L.text()) )
        
            Sgamma = self.calculate_Sgamma_vesic (float (self.B.text()) , float (self.L.text()))
            dc = self.calculate_dc_vesic( D, float (self.B.text()))
            dq = self.calculate_dq_vesic(D , float (self.B.text()))
            dgamma = self.calculate_dgamma_vesic()
            bc = self.calculate_bc_vesic()
            bq = self.calculate_bq_vesic()
            bgamma = self.calculate_ggamma_vesic()
            ca = self.calculate_ca_vesic()
            Af = self.calculate_Af_vesic(float(self.B.text()) , float(self.L.text()))
            mB = self.calculate_mB_vesic(float(self.B.text()) , float(self.L.text()))
            mL = self.calculate_mL_vesic(float(self.B.text()) , float(self.L.text()))
            m = self.calculate_m_vesic(mB , mL)
            iq = self.calculate_iq_vesic(Af , ca , m)
            igamma = self.calculate_igamma_vesic( Af , ca , m)
            ic = self.calculate_ic_vesic(iq , Nq)
            gc = self.calculate_gc_vesic ( iq)
            gq = self.calculate_gq_vesic ()
            ggamma = self.calculate_ggamma_vesic()
            q = self.calculate_q_terzaghi(D)
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)

            dChartY.append(qall)
            
        
        qPerD = Figure(figsize=(5, 3), dpi=100)
        qPerD.text(0.4 , 0.9 ,"qall per D base steps", fontsize=10, color='silver')
        qPerD_axes = qPerD.add_subplot(111)


                # static line in graph
        qPerD_axes.axhline(y = dChartY[4], color='#56E419', linestyle='--')
        qPerD_axes.axvline(x = dChartX[4], color='#56E419', linestyle='--')
        ###
        

        qPerD_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerD_axes.set_xlabel ("D Base steps")
        qPerD_axes.plot(dChartX, dChartY, marker = "o" , color = "green")
        qPerD_shape = FigureCanvas(qPerD)
        tool = NavigationToolbar(qPerD_shape, self)
        self.graphWindowLayout.addWidget(tool, 0 , 1)
        self.graphWindowLayout.addWidget(qPerD_shape , 1 , 1)
        qPerD_axes.grid(linewidth=0.5, alpha=0.5)


        qPerD_shape.mpl_connect('motion_notify_event', on_mouse_move)
        
        lChartX = []
        lChartY = []
        
        lChartX.append(float(self.L.text()))
        for i in range (1 , self.steps + 1):
            lChartX.append (float(self.L.text()) + (i * float(self.LStep.text())))
            lChartX.append (float(self.L.text()) - (i * float(self.LStep.text())))
        
        lChartX.sort()
        
        
        for L in lChartX :
            Nq = self.calculate_Nq_vesic()
            Nc = self.calculate_Nc_vesic(Nq)
            Ngamma = self.calculate_Ngamma_vesic(Nq)
            Sc = self.calculate_Sc_vesic(Nq , Nc , float (self.B.text()) , L)
            Sq = self.calculate_Sq_vesic( float (self.B.text()) , L )
            Sgamma = self.calculate_Sgamma_vesic (float (self.B.text()) , L)
            dc = self.calculate_dc_vesic( float(self.DBase.text()) , float (self.B.text()))
            dq = self.calculate_dq_vesic(float(self.DBase.text()) , float (self.B.text()))
            dgamma = self.calculate_dgamma_vesic()
            bc = self.calculate_bc_vesic()
            bq = self.calculate_bq_vesic()
            bgamma = self.calculate_ggamma_vesic()
            ca = self.calculate_ca_vesic()
            Af = self.calculate_Af_vesic(float(self.B.text()) , L)
            mB = self.calculate_mB_vesic(float(self.B.text()) , L)
            mL = self.calculate_mL_vesic(float(self.B.text()) , L)
            m = self.calculate_m_vesic(mB , mL)
            iq = self.calculate_iq_vesic(Af , ca , m)
            igamma = self.calculate_igamma_vesic( Af , ca , m)
            ic = self.calculate_ic_vesic(iq , Nq)
            gc = self.calculate_gc_vesic ( iq)
            gq = self.calculate_gq_vesic ()
            ggamma = self.calculate_ggamma_vesic()
            q = self.calculate_q_terzaghi(float(self.DBase.text()))
            qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
            qall = self.calculate_qall_terzaghi(qu)

        

            lChartY.append(qall)
      
        
        qPerL = Figure(figsize=(5, 3), dpi=100)
        qPerL.text(0.4 , 0.9 ,"qall per L steps", fontsize=10, color='silver')

        
        qPerL_axes = qPerL.add_subplot(111)

              # static line in graph
        qPerL_axes.axhline(y = lChartY[4], color='#FB903D', linestyle='--')
        qPerL_axes.axvline(x = lChartX[4], color='#FB903D', linestyle='--')
        ###

        qPerL_axes.set_ylabel (u"qall (ton/m\N{SUPERSCRIPT TWO})")
        qPerL_axes.set_xlabel ("L steps")
        qPerL_axes.plot(lChartX, lChartY, marker = "o" , color="red")
        qPerL_shape = FigureCanvas(qPerL)
        tool = NavigationToolbar(qPerL_shape, self)
        qPerL_axes.grid(linewidth=0.5, alpha=0.5)

        self.graphWindowLayout.addWidget(tool, 2 , 0)
        self.graphWindowLayout.addWidget(qPerL_shape , 3 , 0)
        
        
        qPerL_shape.mpl_connect('motion_notify_event', on_mouse_move)

        
        self.graphWindow.exec()



    def resetAll (self , layout):
        theInputs = [self.Dwat , self.gammawat , self.fos ,self.B , self.L , self.DBase , self.eta , self.psi , self.Qh , self.Qv , self.DStep , self.BStep , self.LStep , self.l1_gammawet , self.l1_gammasat , self.l1_fi , self.l1_c , self.l1_d, self.l2_gammawet , self.l2_gammasat , self.l2_fi , self.l2_c , self.l2_d, self.l3_gammawet , self.l3_gammasat , self.l3_fi , self.l3_c , self.l3_d, self.l4_gammawet , self.l4_gammasat , self.l4_fi , self.l4_c , self.l4_d]
        

        for inp in theInputs:
            inp.clear()

        self.graphButton.setEnabled(False)

    # This funtion put the result in the consule under the inputs 
    # def results_terzaghi (self , layout):
        
        
        
    #     self.resultGridLayout = QGridLayout ()
    #     self.resultBox1 = QGroupBox("Results : ")
    #     self.resultBox2 = QGroupBox("")
    #     self.resultPart1 = QFormLayout()
    #     self.resultPart2 = QFormLayout()
        
        
        
    #     self.NqLabel.setText("N۹ = "  + "%.2f" %self.calculate_Nq_terzaghi())
    #     self.NcLabel.setText("N꜀ = "  + "%.2f" %self.calculate_Nc_terzaghi(self.calculate_Nq_terzaghi()))
    #     self.NgammaLabel.setText("N\u03B3 = " + "%.2f" %self.calculate_Ngamma_terzaghi(self.calculate_KPgamma_terzaghi()))
    #     self.ScLabel.setText("S꜀ = " + "%.2f" %self.calculate_Sc_terzaghi(float(self.B.text()) , float(self.L.text())))
    #     self.SqLabel.setText("S۹ = " + "%.2f" %self.calculate_Sq_terzaghi())
    #     self.SgammaLabel.setText("S\u03B3 = " + "%.2f" %self.calculate_Sgamma_terzaghi(float(self.B.text()) , float(self.L.text())))
        

    #     # MISHE BARAYE MOHASEBE QU AZ MAGHAADIIR LABEL HAYE BALA ESTEFADE KARD ...!
    #     qu = self.calculate_qu_terzaghi(float(self.B.text()) , self.calculate_Nc_terzaghi(self.calculate_Nq_terzaghi()) , self.calculate_Sc_terzaghi(float(self.B.text()) , float(self.L.text())) , self.calculate_q_terzaghi (float(self.DBase.text())), self.calculate_Nq_terzaghi() , self.calculate_Sq_terzaghi() , self.calculate_Ngamma_terzaghi(self.calculate_KPgamma_terzaghi()) , self.calculate_Sgamma_terzaghi(float(self.B.text()), float(self.L.text())) )
    #     self.quLabel.setText("qᵤ = " + "%.2f" %qu)
    #     self.qallLabel.setText("qₐₗₗ = " + "%.2f" %self.calculate_qall_terzaghi(qu))
        
        
        
    #     self.resultPart1.addRow (self.NqLabel)
    #     self.resultPart1.addRow (self.NcLabel)
    #     self.resultPart1.addRow (self.NgammaLabel)
        
    #     self.resultPart1.addRow (self.ScLabel)
    #     self.resultPart2.addRow (self.SqLabel)
    #     self.resultPart2.addRow (self.SgammaLabel)
    #     self.resultPart2.addRow (self.quLabel)
    #     self.resultPart2.addRow (self.qallLabel)
        
        
    #     self.resultBox1.setLayout(self.resultPart1)
    #     self.resultBox2.setLayout(self.resultPart2)
 
    
  
    #     self.resultGridLayout.addWidget(self.resultBox1 , 0 , 0 )
    #     self.resultGridLayout.addWidget(self.resultBox2 , 0 , 1 )
        
    #     self.layout.addLayout(self.resultGridLayout , 4 , 0 )
        
        
        
    # This funtion put the result in the consule under the inputs     
    # def results_meyerhof(self , layout):
            
    #     self.resultGridLayout = QGridLayout ()
    #     self.resultBox1 = QGroupBox("Results : ")
    #     self.resultBox2 = QGroupBox("")
    #     self.resultPart1 = QFormLayout()
    #     self.resultPart2 = QFormLayout()
        
        
        
    #     Nq = self.calculate_Nq_meyerhof()
    #     Nc = self.calculate_Nc_meyerhof(self.calculate_Nq_meyerhof())
    #     Ngamma = self.calculate_Ngamma_meyerhof(self.calculate_Nq_meyerhof())
    #     beta = self.calculate_beta_meyerhof()
    #     dc = self.calculate_dc_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float(self.B.text()))
    #     Sc = self.calculate_Sc_meyerhof(self.calculate_KP_meyerhof(), float(self.L.text()) , float(self.B.text()) )
    #     ic = self.calculate_ic_meyerhof(beta)
    #     iq = self.calculate_iq_meyerhof(beta)
    #     Sgamma = self.calculate_Sgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()) , float(self.B.text()) )
    #     Sq = self.calculate_Sq_meyerhof(self.calculate_KP_meyerhof() , float(self.L.text()) , float(self.B.text()) )
    #     dgamma = self.calculate_dgamma_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float(self.B.text()) )
    #     igamma = self.calculate_igamma_meyerhof(beta)
    #     dq = self.calculate_dq_meyerhof(self.calculate_KP_meyerhof() , float(self.DBase.text()) , float(self.B.text()) )
        
        
        
    #     self.NqLabel.setText("N۹ = "  + "%.2f" %Nq)
    #     self.NcLabel.setText("N꜀ = "  + "%.2f" %Nc)
    #     self.NgammaLabel.setText("N\u03B3 = " + "%.2f" %Ngamma)
    #     self.betaLabel.setText("\u03B2 = " + "%.2f" %beta)
    #     self.dcLabel.setText("d꜀ = " + "%.2f" %dc)
    #     self.ScLabel.setText("S꜀ = " + "%.2f" %Sc)
    #     qu = self.calculate_qu_meyerhof( Nc , Sc , dc , ic , self.calculate_q_terzaghi(float(self.DBase.text())) , Nq , Sq , dq , iq , float(self.B.text()) , Ngamma , Sgamma , dgamma , igamma )
    #     self.quLabel.setText("qᵤ = " + "%.2f" %qu)
    #     self.qallLabel.setText("qₐₗₗ = " + "%.2f" %self.calculate_qall_meyerhof(qu))


    #     self.resultPart1.addRow (self.NqLabel)
    #     self.resultPart1.addRow (self.NcLabel)
    #     self.resultPart1.addRow (self.NgammaLabel)
    #     self.resultPart1.addRow (self.betaLabel)
    #     self.resultPart2.addRow (self.dcLabel)
    #     self.resultPart2.addRow (self.ScLabel)
    #     self.resultPart2.addRow (self.quLabel)
    #     self.resultPart2.addRow (self.qallLabel)
        
        
        
    #     self.resultBox1.setLayout(self.resultPart1)
    #     self.resultBox2.setLayout(self.resultPart2)
 
    
  
    #     self.resultGridLayout.addWidget(self.resultBox1 , 0 , 0 )
    #     self.resultGridLayout.addWidget(self.resultBox2 , 0 , 1 )
        
    #     self.layout.addLayout(self.resultGridLayout , 4 , 0 )
        
        
    # This funtion put the result in the consule under the inputs 
    # def results_hansen (self , layout):
                    
    #     self.resultGridLayout = QGridLayout ()
    #     self.resultBox1 = QGroupBox("Results : ")
    #     self.resultBox2 = QGroupBox("")
    #     self.resultPart1 = QFormLayout()
    #     self.resultPart2 = QFormLayout()
        
        
        
    #     Nq = self.calculate_Nq_hansen()
    #     Nc = self.calculate_Nc_hansen(self.calculate_Nq_hansen())
    #     Ngamma = self.calculate_Ngamma_hansen(self.calculate_Nq_hansen())
    #     Sc = self.calculate_Sc_hansen(self.calculate_Nq_hansen() , self.calculate_Nc_hansen(Nq) , float (self.B.text()) , float (self.L.text()))
    #     Sq = self.calculate_Sq_hansen( float (self.B.text()) , float (self.L.text()) )
    #     Sgamma = self.calculate_Sgamma_hansen (float (self.B.text()) , float (self.L.text()))
    #     dc = self.calculate_dc_hansen( float(self.DBase.text()) , float (self.B.text()))
    #     dq = self.calculate_dq_hansen(float(self.DBase.text()) , float (self.B.text()))
    #     dgamma = self.calculate_dgamma_hansen()
    #     bc = self.calculate_bc_hansen()
    #     bq = self.calculate_bq_hansen()
    #     bgamma = self.calculate_ggamma_hansen()
    #     gc = self.calculate_gc_hansen()
    #     gq = self.calculate_gq_hansen()
    #     ggamma = self.calculate_ggamma_hansen()
    #     ca = self.calculate_ca_hansen()
    #     Af = self.calculate_Af_hansen(float (self.B.text()) , float (self.L.text()))
    #     m = self.calculate_m_hansen(self.calculate_mB_hansen(float (self.B.text()) , float (self.L.text())) , self.calculate_mL_hansen(float (self.B.text()) , float (self.L.text())) )
    #     iq = self.calculate_iq_hansen(Af , ca , m)
    #     igamma = self.calculate_igamma_hansen(Af , ca , m)
    #     ic = self.calculate_ic_hansen(iq , Nq)
    #     q = self.calculate_q_terzaghi(float(self.DBase.text()))
        
        
    #     self.NqLabel.setText("N۹ = "  + "%.2f" %Nq)
    #     self.NcLabel.setText("N꜀ = "  + "%.2f" %Nc)
    #     self.NgammaLabel.setText("N gamma = " + "%.2f" %Ngamma)
    #     self.dcLabel.setText("d꜀ = " + "%.2f" %dc)
    #     self.ScLabel.setText("S꜀ = " + "%.2f" %Sc)
        
    #     qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
        
        
        
    #     self.quLabel.setText("qᵤ = " + "%.2f" %qu)
    #     self.qallLabel.setText("qₐₗₗ = " + "%.2f" %self.calculate_qall_meyerhof(qu))


    #     self.resultPart1.addRow (self.NqLabel)
    #     self.resultPart1.addRow (self.NcLabel)
    #     self.resultPart1.addRow (self.NgammaLabel)
    #     self.resultPart2.addRow (self.dcLabel)
    #     self.resultPart2.addRow (self.ScLabel)
    #     self.resultPart2.addRow (self.quLabel)
    #     self.resultPart2.addRow (self.qallLabel)
        
        
        
    #     self.resultBox1.setLayout(self.resultPart1)
    #     self.resultBox2.setLayout(self.resultPart2)
 
    
  
    #     self.resultGridLayout.addWidget(self.resultBox1 , 0 , 0 )
    #     self.resultGridLayout.addWidget(self.resultBox2 , 0 , 1 )
        
    #     self.layout.addLayout(self.resultGridLayout , 4 , 0 )
        
        
  
    # This funtion put the result in the consule under the inputs 
    # def results_vesic(self , layout):
                    
    #     self.resultGridLayout = QGridLayout ()
    #     self.resultBox1 = QGroupBox("Results : ")
    #     self.resultBox2 = QGroupBox("")
    #     self.resultPart1 = QFormLayout()
    #     self.resultPart2 = QFormLayout()
        
        
        
    #     Nq = self.calculate_Nq_vesic()
    #     Nc = self.calculate_Nc_vesic(Nq)
    #     Ngamma = self.calculate_Ngamma_vesic(Nq)
    #     Sc = self.calculate_Sc_vesic(Nq , Nc , float (self.B.text()) , float (self.L.text()))
    #     Sq = self.calculate_Sq_vesic( float (self.B.text()) , float (self.L.text()) )
        
        
    #     Sgamma = self.calculate_Sgamma_vesic (float (self.B.text()) , float (self.L.text()))
    #     dc = self.calculate_dc_vesic( float(self.DBase.text()) , float (self.B.text()))
    #     dq = self.calculate_dq_vesic(float(self.DBase.text()) , float (self.B.text()))
    #     dgamma = self.calculate_dgamma_vesic()
    #     bc = self.calculate_bc_vesic()
    #     bq = self.calculate_bq_vesic()
    #     bgamma = self.calculate_ggamma_vesic()
    #     ca = self.calculate_ca_vesic()
    #     Af = self.calculate_Af_vesic(float(self.B.text()) , float(self.L.text()))
    #     mB = self.calculate_mB_vesic(float(self.B.text()) , float(self.L.text()))
    #     mL = self.calculate_mL_vesic(float(self.B.text()) , float(self.L.text()))
    #     m = self.calculate_m_vesic(mB , mL)
    #     iq = self.calculate_iq_vesic(Af , ca , m)
    #     igamma = self.calculate_igamma_vesic( Af , ca , m)
    #     ic = self.calculate_ic_vesic(iq , Nq)
    #     gc = self.calculate_gc_vesic ( iq)
    #     gq = self.calculate_gq_vesic ()
    #     ggamma = self.calculate_ggamma_vesic()
    #     q = self.calculate_q_terzaghi(float(self.DBase.text()))
        
        

        
    #     self.NqLabel.setText("N۹ = "  + "%.2f" %Nq)
    #     self.NcLabel.setText("N꜀ = "  + "%.2f" %Nc)
    #     self.NgammaLabel.setText("N\u03B3  = " + "%.2f" %Ngamma)
    #     self.dcLabel.setText("d꜀ = " + "%.2f" %dc)
    #     self.ScLabel.setText("S꜀ = " + "%.2f" %Sc)
        
    #     qu = self.calculate_qu_hansen(Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma)
        
        
        
    #     self.quLabel.setText("qᵤ = " + "%.2f" %qu)
    #     self.qallLabel.setText("qₐₗₗ = " + "%.2f" %self.calculate_qall_meyerhof(qu))


    #     self.resultPart1.addRow (self.NqLabel)
    #     self.resultPart1.addRow (self.NcLabel)
    #     self.resultPart1.addRow (self.NgammaLabel)
    #     self.resultPart2.addRow (self.dcLabel)
    #     self.resultPart2.addRow (self.ScLabel)
    #     self.resultPart2.addRow (self.quLabel)
    #     self.resultPart2.addRow (self.qallLabel)
        
        
        
    #     self.resultBox1.setLayout(self.resultPart1)
    #     self.resultBox2.setLayout(self.resultPart2)
 
    
  
    #     self.resultGridLayout.addWidget(self.resultBox1 , 0 , 0 )
    #     self.resultGridLayout.addWidget(self.resultBox2 , 0 , 1 )
        
    #     self.layout.addLayout(self.resultGridLayout , 4 , 0 )
        
            
    def enButton (self ):
        
        flag =0
        if self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False :
            if (self.Dwat.text() == '' or self.gammawat.text() == '' or self.fos.text() == '' or self.B.text() == '' or self.L.text() == '' or self.DBase.text() == '' or self.Qv.text() == '' or self.DStep.text() == ''or self.LStep.text()=='' or self.BStep.text()=='' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == ''):
                self.graphButton.setEnabled(False)
                #self.processButton.setEnabled(False)
                flag = 1
        
        if self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False :
            if (self.Dwat.text() == '' or self.gammawat.text() == '' or self.fos.text() == '' or self.B.text() == '' or self.L.text() == '' or self.DBase.text() == '' or self.Qv.text() == '' or self.DStep.text() == ''or self.LStep.text()=='' or self.BStep.text()=='' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == ''or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == ''):
                self.graphButton.setEnabled(False)
                #self.processButton.setEnabled(False)
                flag = 1

        if self.l3Box.isEnabled() == True and self.l4Box.isEnabled() == False :
            if (self.Dwat.text() == '' or self.gammawat.text() == '' or self.fos.text() == '' or self.B.text() == '' or self.L.text() == '' or self.DBase.text() == '' or self.Qv.text() == '' or self.DStep.text() == ''or self.LStep.text()=='' or self.BStep.text()=='' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == ''or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == '' or self.l3_gammawet.text() == '' or self.l3_gammasat.text() == '' or self.l3_fi.text() == '' or self.l3_c.text() == '' or self.l3_d.text() == ''):
                self.graphButton.setEnabled(False)
                #self.processButton.setEnabled(False)
                flag = 1

        if self.l4Box.isEnabled() == True :
            if (self.Dwat.text() == '' or self.gammawat.text() == '' or self.fos.text() == '' or self.B.text() == '' or self.L.text() == '' or self.DBase.text() == '' or self.Qv.text() == '' or self.DStep.text() == ''or self.LStep.text()=='' or self.BStep.text()=='' or self.l1_gammawet.text() == '' or self.l1_gammasat.text() == '' or self.l1_fi.text() == '' or self.l1_c.text() == '' or self.l1_d.text() == ''or self.l2_gammawet.text() == '' or self.l2_gammasat.text() == '' or self.l2_fi.text() == '' or self.l2_c.text() == '' or self.l2_d.text() == '' or self.l3_gammawet.text() == '' or self.l3_gammasat.text() == '' or self.l3_fi.text() == '' or self.l3_c.text() == '' or self.l3_d.text() == ''or self.l4_gammawet.text() == '' or self.l4_gammasat.text() == '' or self.l4_fi.text() == '' or self.l4_c.text() == '' or self.l4_d.text() == ''):
                self.graphButton.setEnabled(False)
                #self.processButton.setEnabled(False)
                flag = 1

        
        
        
        
        
        
        if (self.method != "Terzaghi" and self.Qh.text() == ''):
            self.graphButton.setEnabled(False)
            #self.processButton.setEnabled(False)
            flag = 1

        if ((self.method in [ "Vesic", "Hansen"]) and (self.psi.text() == '' or self.eta.text() == '' )):
            self.graphButton.setEnabled(False)
            #self.processButton.setEnabled(False)
            flag = 1

        if (flag == 0):
            self.graphButton.setEnabled(True)
            #self.processButton.setEnabled(True)
        

    
        
        
    def inputData(self,layout ):
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

        gridLayout = QGridLayout()

        # GENERAL Part
        # Number Of Layers Part
        self.numberOfLayer = QComboBox()
        self.numberOfLayer.addItems(["One layer", "Two layers", "Three layers", "Four layers"])
        self.numberOfLayer.currentTextChanged.connect(self.activeLayer)
        self.numberOfLayer.currentTextChanged.connect(self.enButton)
        
        # Used method
        self.methodBox = QComboBox()
        self.methodBox.addItems(["Terzaghi", "Vesic", "Hansen", "Meyerhof"])
        self.methodBox.currentTextChanged.connect(self.activeMethod)
        self.method = "Terzaghi"
        
        # D WATER
        self.Dwat = QLineEdit()
        self.Dwat.setValidator(QDoubleValidator())
        self.Dwat.setPlaceholderText("meters")
        self.Dwat.textChanged.connect(self.enButton)
        # gamma WATER
        self.gammawat = QLineEdit()
        self.gammawat.setValidator(QDoubleValidator())
        self.gammawat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.gammawat.textChanged.connect(self.enButton)
        # FOS
        self.fos = QLineEdit()
        self.fos.setValidator(QDoubleValidator())
        self.fos.textChanged.connect(self.enButton)

        # FOUNDATION DIM.
        # B
        self.B = QLineEdit()
        self.B.setValidator(QDoubleValidator())
        self.B.setPlaceholderText("meters")
        self.B.setToolTip("عرض پی سطحی")
        self.B.textChanged.connect(self.enButton)

        # L
        self.L = QLineEdit()
        self.L.setValidator(QDoubleValidator())
        self.L.setPlaceholderText("meters")
        self.L.setToolTip("طول پی سطحی")
        self.L.textChanged.connect(self.enButton)

        # D base
        self.DBase = QLineEdit()
        self.DBase.setValidator(QDoubleValidator())
        self.DBase.setPlaceholderText("meters")
        self.DBase.setToolTip("عمق مدفون پی")
        self.DBase.textChanged.connect(self.enButton)


        # eta
        self.eta = QLineEdit()
        self.eta.setValidator(QDoubleValidator())
        self.eta.setPlaceholderText("degree")
        self.eta.setToolTip("زاویه قرارگیری پی سطحی")
        self.eta.textChanged.connect(self.enButton)


        #psi
        self.psi = QLineEdit()
        self.psi.setValidator(QDoubleValidator())
        self.psi.setPlaceholderText("degree")
        self.psi.setToolTip("زاویه خاک سطح زمین")
        self.psi.textChanged.connect(self.enButton)

        
        # LOADING PART
        # Q h
        self.Qh = QLineEdit()
        self.Qh.setValidator(QDoubleValidator())
        self.Qh.setPlaceholderText("ton")
        self.Qh.setEnabled(False)
        self.Qh.setToolTip("بار افقی")
        self.Qh.textChanged.connect(self.enButton)

        #Q r
        self.Qv = QLineEdit()
        self.Qv.setValidator(QDoubleValidator())
        self.Qv.setPlaceholderText("ton")
        self.Qv.setToolTip("بار عمودی")
        self.Qv.textChanged.connect(self.enButton)

        
        
        # CHART PART
        # Number of steps
        # This part has been deleted by order of ALIASGARI
        #self.numberOfStep = QComboBox()
        #self.numberOfStep.addItems(["1 Step", "2 Steps", "3 Steps", "4 Steps"])
        self.steps = 4
        #self.numberOfStep.currentTextChanged.connect(self.findingSteps)

        # D step
        self.DStep = QLineEdit()
        self.DStep.setValidator(QDoubleValidator())
        self.DStep.setPlaceholderText("meters")
        self.DStep.setToolTip("گام تغییر عمق استقرار پی سطحی")
        self.DStep.textChanged.connect(self.enButton)

        # B step
        self.BStep = QLineEdit()
        self.BStep.setValidator(QDoubleValidator())
        self.BStep.setPlaceholderText("meters")
        self.BStep.setToolTip("گام تغییر عرض پی سطحی")
        self.BStep.textChanged.connect(self.enButton)

        # L step
        self.LStep = QLineEdit()
        self.LStep.setValidator(QDoubleValidator())
        self.LStep.setPlaceholderText("meters")
        self.LStep.setToolTip("گام تغییر طول پی سطحی")
        self.LStep.textChanged.connect(self.enButton)


        # Number Of Layers Part
        self.numberOfLayer = QComboBox()
        self.numberOfLayer.addItems(["One layer", "Two layers", "Three layers", "Four layers"])
        self.numberOfLayer.currentTextChanged.connect(self.activeLayer)
        

        
        self.generalBox = QGroupBox("GENERAL")
        self.generalBox.setStyleSheet(boxesStyle)
        self.generalBox.setAlignment(Qt.AlignCenter)
        self.generalPart = QFormLayout()
        self.MethodLabel = QLabel("Method")
        self.MethodLabel.setToolTip("روش محاسباتی")
        self.generalPart.addRow(self.MethodLabel , self.methodBox)
        self.generalPart.addRow("Layer Number" , self.numberOfLayer)

        self.DwatLabel = QLabel("Dʷᵃᵗ (m)")
        self.DwatLabel.setToolTip("عمق آب")
        self.generalPart.addRow(self.DwatLabel, self.Dwat)
        
        self.gammawatLabel = QLabel("\u03B3ʷᵃᵗ(ton/m\N{SUPERSCRIPT THREE})")
        self.gammawatLabel.setToolTip("وزن مخصوص آب")
        self.generalPart.addRow(self.gammawatLabel, self.gammawat)

        self.FOSLabel = QLabel("FOS")
        self.FOSLabel.setToolTip("ضریب اطمینان")
        self.generalPart.addRow(self.FOSLabel, self.fos)
        self.generalBox.setLayout(self.generalPart)

        self.foundationDimBox = QGroupBox("FOUNDATION DIMENSION")
        self.foundationDimBox.setStyleSheet(boxesStyle)
        self.foundationDimBox.setAlignment(Qt.AlignCenter)

        self.foundationDimPart = QFormLayout()



        Blabel = QLabel("B(m)")
        Blabel.setToolTip("عرض پی سطحی")
        self.foundationDimPart.addRow(Blabel, self.B)

        Llabel = QLabel("L(m)")
        Llabel.setToolTip("طول پی سطحی")
        self.foundationDimPart.addRow(Llabel, self.L)
        
        DBaselabel = QLabel("Dᵇᵃˢᵉ(m)")
        DBaselabel.setToolTip("عمق لایه خاک")
        self.foundationDimPart.addRow(DBaselabel, self.DBase)

        etalabel = QLabel(u"\u03B7(degree)")
        etalabel.setToolTip("زاویه قرارگیری پی سطحی")
        self.foundationDimPart.addRow(etalabel, self.eta)
        self.eta.setEnabled(False)

        psiLabel = QLabel(u"\u03C8(degree)")
        psiLabel.setToolTip("زاویه سطح خاک مجاور پی")
        self.foundationDimPart.addRow(psiLabel, self.psi)
        self.psi.setEnabled(False)
        self.foundationDimBox.setLayout(self.foundationDimPart)

        self.loadingBox = QGroupBox("LOADING")
        self.loadingBox.setStyleSheet(boxesStyle)
        self.loadingBox.setAlignment(Qt.AlignCenter)

        self.loadingPart = QFormLayout()
        QhLabel = QLabel (u"Q\u2095(ton)")
        QhLabel.setToolTip("بار افقی")
        self.loadingPart.addRow(QhLabel, self.Qh)

        QvLabel = QLabel (u"Q\u1D65(ton)")
        QvLabel.setToolTip("بار عمودی")
        self.loadingPart.addRow(QvLabel, self.Qv)
        self.loadingBox.setLayout(self.loadingPart)

        self.numberOfStepBox = QGroupBox("CHART")
        self.numberOfStepBox.setStyleSheet(boxesStyle)
        self.numberOfStepBox.setAlignment(Qt.AlignCenter)

        self.numberOfStepPart = QFormLayout()
        #self.numberOfStepPart.addRow("NO. of steps", self.numberOfStep)
        DStepLabel = QLabel("Dˢᵗᵉᵖ(m)")
        DStepLabel.setToolTip("گام تغییر عمق استقرار پی سطحی")
        self.numberOfStepPart.addRow(DStepLabel, self.DStep)
        
        BStepLabel = QLabel("Bˢᵗᵉᵖ(m)")
        BStepLabel.setToolTip("گام تغییر عرض پی سطحی")
        self.numberOfStepPart.addRow(BStepLabel, self.BStep)

        LStepLabel = QLabel("Lˢᵗᵉᵖ(m)")
        LStepLabel.setToolTip("گام تغییر طول پی سطحی")
        self.numberOfStepPart.addRow(LStepLabel, self.LStep)
        
        self.numberOfStepBox.setLayout(self.numberOfStepPart)

        # first layer PART
        # gamma 1 wet
        self.l1_gammawet = QLineEdit()
        self.l1_gammawet.setValidator(QDoubleValidator())
        self.l1_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l1_gammawet.setToolTip("وزن مخصوص مرطوب خاک")
        self.l1_gammawet.textChanged.connect(self.enButton)
        l1_gammawetLabel = QLabel(u"\u03B3\u2081ʷᵉᵗ(ton/m\N{SUPERSCRIPT THREE})")
        l1_gammawetLabel.setToolTip("وزن مخصوص مرطوب خاک")


        # gamma 1 sat
        self.l1_gammasat = QLineEdit()
        self.l1_gammasat.setValidator(QDoubleValidator())
        self.l1_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l1_gammasat.setToolTip("وزن مخصوص اشباع خاک")
        self.l1_gammasat.textChanged.connect(self.enButton)
        l1_gammasatLabel = QLabel (u"\u03B3\u2081ˢᵃᵗ(ton/m\N{SUPERSCRIPT THREE})")
        l1_gammasatLabel.setToolTip("وزن مخصوص اشباع خاک")

        # fi 1
        self.l1_fi = QLineEdit()
        self.l1_fi.setValidator(QDoubleValidator())
        self.l1_fi.setPlaceholderText("degree")
        self.l1_fi.setToolTip("زاویه اصطکاک خاک")
        self.l1_fi.textChanged.connect(self.enButton)
        l1_fiLabel = QLabel(u"\u03C6\u2081(degree)")
        l1_fiLabel.setToolTip("زاویه اصطکاک خاک")

        # C 1
        self.l1_c = QLineEdit()
        self.l1_c.setValidator(QDoubleValidator())
        self.l1_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l1_c.setToolTip("چسبندگی خاک")
        self.l1_c.textChanged.connect(self.enButton)
        l1_cLabel = QLabel(u"C\u2081(ton/m\N{SUPERSCRIPT TWO})")
        l1_cLabel.setToolTip("چسبندگی خاک")

        # D 1
        self.l1_d = QLineEdit()
        self.l1_d.setValidator(QDoubleValidator())
        self.l1_d.setPlaceholderText("meters")
        self.l1_d.setToolTip("عمق لایه خاک")
        self.l1_d.textChanged.connect(self.enButton)
        l1_dLabel = QLabel (u"D\u2081(m)")
        l1_dLabel.setToolTip("عمق لایه خاک")


        self.l1Box = QGroupBox("1ST LAYER CHARACTERISTIC")
        self.l1Box.setStyleSheet(boxesStyle)
        self.l1Box.setAlignment(Qt.AlignCenter)

        self.l1Part = QFormLayout()
        self.l1Part.addRow(l1_gammawetLabel, self.l1_gammawet)
        self.l1Part.addRow(l1_gammasatLabel, self.l1_gammasat)
        self.l1Part.addRow(l1_fiLabel, self.l1_fi)
        self.l1Part.addRow(l1_cLabel, self.l1_c)
        self.l1Part.addRow(l1_dLabel, self.l1_d)
        self.l1Box.setLayout(self.l1Part)

        # second Layer PART
        # gamma 2 wet
        self.l2_gammawet = QLineEdit()
        self.l2_gammawet.setValidator(QDoubleValidator())
        self.l2_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l2_gammawet.setToolTip("وزن مخصوص مرطوب خاک")
        self.l2_gammawet.textChanged.connect(self.enButton)
        

        # gamma 2 sat
        self.l2_gammasat = QLineEdit()
        self.l2_gammasat.setValidator(QDoubleValidator())
        self.l2_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l2_gammasat.setToolTip("وزن مخصوص اشباع خاک")
        self.l2_gammasat.textChanged.connect(self.enButton)

        # fi 2
        self.l2_fi = QLineEdit()
        self.l2_fi.setValidator(QDoubleValidator())
        self.l2_fi.setPlaceholderText("degree")
        self.l2_fi.setToolTip("زاویه اصطکاک خاک")
        self.l2_fi.textChanged.connect(self.enButton)


        # C 2
        self.l2_c = QLineEdit()
        self.l2_c.setValidator(QDoubleValidator())
        self.l2_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l2_c.setToolTip("چسبندگی خاک")
        self.l2_c.textChanged.connect(self.enButton)


        # D 2
        self.l2_d = QLineEdit()
        self.l2_d.setValidator(QDoubleValidator())
        self.l2_d.setPlaceholderText("meters")
        self.l2_d.setToolTip("عمق لایه خاک")
        self.l2_d.textChanged.connect(self.enButton)


        self.l2Box = QGroupBox("2ND LAYER CHARACTERISTIC")
        self.l2Box.setStyleSheet(boxesStyle)
        self.l2Box.setAlignment(Qt.AlignCenter)
        self.l2Part = QFormLayout()
        self.l2Part.addRow(u"\u03B3\u2082ʷᵉᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l2_gammawet)
        self.l2Part.addRow(u"\u03B3\u2082ˢᵃᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l2_gammasat)
        self.l2Part.addRow(u"\u03C6\u2082(degree)", self.l2_fi)
        self.l2Part.addRow(u"C\u2082(ton/m\N{SUPERSCRIPT TWO})", self.l2_c)
        self.l2Part.addRow(u"D\u2082(m)", self.l2_d)
        self.l2Box.setLayout(self.l2Part)
        self.l2Box.setEnabled(False)

        # third Layer PART
        # gamma 3 wet
        self.l3_gammawet = QLineEdit()
        self.l3_gammawet.setValidator(QDoubleValidator())
        self.l3_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l3_gammawet.setToolTip("وزن مخصوص مرطوب خاک")
        self.l3_gammawet.textChanged.connect(self.enButton)

        # gamma 3 sat
        self.l3_gammasat = QLineEdit()
        self.l3_gammasat.setValidator(QDoubleValidator())
        self.l3_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l3_gammasat.setToolTip("وزن مخصوص اشباع خاک")
        self.l3_gammasat.textChanged.connect(self.enButton)

        # fi 3
        self.l3_fi = QLineEdit()
        self.l3_fi.setValidator(QDoubleValidator())
        self.l3_fi.setPlaceholderText("degree")
        self.l3_fi.setToolTip("زاویه اصطکاک خاک")
        self.l3_fi.textChanged.connect(self.enButton)


        # C 3
        self.l3_c = QLineEdit()
        self.l3_c.setValidator(QDoubleValidator())
        self.l3_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l3_c.setToolTip("چسبندگی خاک")
        self.l3_c.textChanged.connect(self.enButton)


        # D 3
        self.l3_d = QLineEdit()
        self.l3_d.setValidator(QDoubleValidator())
        self.l3_d.setPlaceholderText("meters")
        self.l3_d.setToolTip("عمق لایه خاک")
        self.l3_d.textChanged.connect(self.enButton)


        self.l3Box = QGroupBox("3RD LAYER CHARACTERISTIC")
        self.l3Box.setAlignment(Qt.AlignCenter)
        self.l3Box.setStyleSheet(boxesStyle)
        self.l3Part = QFormLayout()
        self.l3Part.addRow(u"\u03B3\u2083ʷᵉᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l3_gammawet)
        self.l3Part.addRow(u"\u03B3\u2083ˢᵃᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l3_gammasat)
        self.l3Part.addRow(u"\u03C6\u2083(degree)", self.l3_fi)
        self.l3Part.addRow(u"C\u2083(ton/m\N{SUPERSCRIPT TWO})", self.l3_c)
        self.l3Part.addRow(u"D\u2083(m)", self.l3_d)
        self.l3Box.setLayout(self.l3Part)
        self.l3Box.setEnabled(False)



        # fourth Layer PART
        # gamma 4 wet
        self.l4_gammawet = QLineEdit()
        self.l4_gammawet.setValidator(QDoubleValidator())
        self.l4_gammawet.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l4_gammawet.setToolTip("وزن مخصوص مرطوب خاک")
        self.l4_gammawet.textChanged.connect(self.enButton)

        # gamma 4 sat
        self.l4_gammasat = QLineEdit()
        self.l4_gammasat.setValidator(QDoubleValidator())
        self.l4_gammasat.setPlaceholderText("ton/m\N{SUPERSCRIPT THREE}")
        self.l4_gammasat.setToolTip("وزن مخصوص اشباع خاک")
        self.l4_gammasat.textChanged.connect(self.enButton)

        # fi 4
        self.l4_fi = QLineEdit()
        self.l4_fi.setValidator(QDoubleValidator())
        self.l4_fi.setPlaceholderText("degree")
        self.l4_fi.setToolTip("زاویه اصطکاک خاک")
        self.l4_fi.textChanged.connect(self.enButton)


        # C 4
        self.l4_c = QLineEdit()
        self.l4_c.setValidator(QDoubleValidator())
        self.l4_c.setPlaceholderText("ton/m\N{SUPERSCRIPT TWO}")
        self.l4_c.setToolTip("چسبندگی خاک")
        self.l4_c.textChanged.connect(self.enButton)


        # D 4
        self.l4_d = QLineEdit()
        self.l4_d.setValidator(QDoubleValidator())
        self.l4_d.setPlaceholderText("meters")
        self.l4_d.setToolTip("عمق لایه خاک")
        self.l4_d.textChanged.connect(self.enButton)


        self.l4Box = QGroupBox("4ST LAYER CHARACTERISTIC")
        self.l4Box.setStyleSheet(boxesStyle)
        self.l4Box.setAlignment(Qt.AlignCenter)
        self.l4Part = QFormLayout()
        self.l4Part.addRow(u"\u03B3\u2084ʷᵉᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l4_gammawet)
        self.l4Part.addRow(u"\u03B3\u2084ˢᵃᵗ(ton/m\N{SUPERSCRIPT THREE})", self.l4_gammasat)
        self.l4Part.addRow(u"\u03C6\u2084(degree)", self.l4_fi)
        self.l4Part.addRow(u"C\u2084(ton/m\N{SUPERSCRIPT TWO})", self.l4_c)
        self.l4Part.addRow(u"D\u2084(m)", self.l4_d)
        self.l4Box.setLayout(self.l4Part)
        self.l4Box.setEnabled(False)




        gridLayout.addWidget(self.generalBox, 0, 0)
        gridLayout.addWidget(self.foundationDimBox, 1, 0)
        gridLayout.addWidget(self.loadingBox, 0, 1)
        gridLayout.addWidget(self.numberOfStepBox, 1, 1)
        gridLayout.addWidget(self.l1Box, 0, 2)
        gridLayout.addWidget(self.l2Box, 1, 2)
        gridLayout.addWidget(self.l3Box, 0, 3)
        gridLayout.addWidget(self.l4Box, 1, 3)

        layout.addLayout(gridLayout, 2, 0)


    def module1HelpFunction(self):
        #pixmap = QPixmap('module3Help1.png')
        image_label = QLabel()
        #image_label.setPixmap(pixmap)


        message_box = QMessageBox()
        #message_box.layout().addWidget(image_label)
        message_box.setWindowTitle('Module 3 Help')
        about = "شما در حال استفاده از ماژول محاسبه ظرفیت باربری پی سطحی از نرم افزار GeOnion هستید."
        about2 = "یکی از رایج ترین پی ها به خصوص برای پروژه های ساختمانی پی های سطحی اسهت."
        about3 = "معمولا عمق استقرار این نوع پی ها کمتر از عرض شان است. این پی ها پس از گودبرداری و برداشتن خاکهای سطحی، و با عبور از عمق یخبندان و لایه های نامناسب اجرا میشوند و شامل پی های منفرد، نواری و تیرهای متکی بر زمین میشوند."
        about4 = "تعیین روابط تحلیلی ظرفیت باربری پی ها توسط محققین مختلف از قبیل ترزاقی، میرهوف، هنسن و وسیک مورد بررسی قرار گرفته است و در این نرم افزار هر 4 روش برای محاسبه موجود می باشد."
        
        message_box.setText(about + "\n\n    " + about2 + "\n\n    " + about3 + "\n\n    " + about4 + "\n\n")
        message_box.exec_()
    

    # def module1HelpFunction2(self):
    #     pixmap = QPixmap('helpModule1.png')
    #     image_label = QLabel()
    #     image_label.setPixmap(pixmap)
    #     message_box = QMessageBox()
    #     message_box.layout().addWidget(image_label)
    #     message_box.setWindowTitle('Module 3 Help')
    #     #message_box.setStandardButtons(QMessageBox.NoButton)
    #     message_box.exec_()




                    
    def graphButtonFunction(self , layout):
        self.graphButton = QPushButton ("Graph" , self)
        self.graphButton.clicked.connect(self.drawGraph)
        self.graphButton.setEnabled(False)
        layout.addWidget(self.graphButton , alignment = Qt.AlignLeft )

    def resetButtonFunction(self , layout):
        self.resetButton = QPushButton ("Reset" , self)
        self.resetButton.clicked.connect(self.resetAll)
        self.resetButton.setEnabled(True)
        layout.addWidget(self.resetButton ,alignment = Qt.AlignRight)



    
    def choosingLayer (self):
        if (self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False):
            self.n = 1

        elif (self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False):

            if (float(self.DBase.text()) <= float(self.l1_d.text()) ):
                self.n = 1
            elif (float(self.l1_d.text()) < float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text() )):
                self.n = 2
            else :
                self.n = 0


        elif (self.l3Box.isEnabled() == True and self.l4Box.isEnabled == False):
            if (float(self.DBase.text()) <= float(self.l1_d.text()) ):
                self.n = 1
            elif (float(self.l1_d.text()) < float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.n = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.n = 3
            else :
                self.n = 0
            
        elif (self.l4Box.isEnabled() == True):
            if (float(self.DBase.text()) <= float(self.l1_d.text() )):
                self.n = 1
            elif (float(self.l1_d.text()) < float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.n = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.n = 3
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) + float(self.l3_d.text()) <= float(self.DBase.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) + float(self.l4_d.text())):
                self.n = 4
            else :
                self.n = 0
        

    
    def choosingLayerForWater (self):
        if (self.l1Box.isEnabled() == True and self.l2Box.isEnabled() == False):
            self.nWater = 1
        elif (self.l2Box.isEnabled() == True and self.l3Box.isEnabled() == False):
            if (float(self.Dwat.text()) <= float(self.l1_d.text()) ):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text() )):
                self.nWater = 2
            else :
                self.nWater = 0


        elif (self.l3Box.isEnabled() == True and self.l4Box.isEnabled == False):
            if (float(self.Dwat.text()) <= float(self.l1_d.text()) ):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.nWater = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.nWater = 3
            else :
                self.nWater = 0
            
        elif (self.l4Box.isEnabled() == True ):
            if (float(self.Dwat.text()) <= float(self.l1_d.text() )):
                self.nWater = 1
            elif (float(self.l1_d.text()) < float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) ):
                self.nWater = 2
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) < float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text())):
                self.nWater = 3
            elif (float(self.l1_d.text() )+ float(self.l2_d.text()) + float(self.l3_d.text()) <= float(self.Dwat.text()) <= float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) + float(self.l4_d.text())):
                self.nWater = 4
            else :
                self.nWater = 0
        

    
    def calculate_Nq_terzaghi (self):
        Nq = 0
        try:       
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Nq = (math.pow( math.e , (1.5 * math.pi - math.radians(float(self.l1_fi.text())))*math.tan(math.radians(float(self.l1_fi.text()))))) / (2 * math.pow(math.cos(math.radians(45+(float(self.l1_fi.text())/2 ))), 2))
            
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nq = (math.pow( math.e , (1.5 * math.pi - math.radians(float(self.l2_fi.text())))*math.tan(math.radians(float(self.l2_fi.text()))))) / (2 * math.pow(math.cos(math.radians(45+(float(self.l2_fi.text())/2 ))), 2))
            
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nq = (math.pow( math.e , (1.5 * math.pi - math.radians(float(self.l3_fi.text())))*math.tan(math.radians(float(self.l3_fi.text()))))) / (2 * math.pow(math.cos(math.radians(45+(float(self.l3_fi.text())/2 ))), 2))
            
            if (self.n == 4):
                Nq = (math.pow( math.e , (1.5 * math.pi - math.radians(float(self.l4_fi.text())))*math.tan(math.radians(float(self.l4_fi.text()))))) / (2 * math.pow(math.cos(math.radians(45+(float(self.l4_fi.text())/2 ))), 2))
            
            return (Nq)
        except :
            raise Exception(u"\u03C6")

    def calculate_Nc_terzaghi(self , Nq):
        try:
            Nc = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Nc = (Nq - 1)* (1/math.tan(math.radians(float(self.l1_fi.text()))))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nc = (Nq - 1)* (1/math.tan(math.radians(float(self.l2_fi.text()))))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nc = (Nq - 1) * (1 / math.tan(math.radians(float(self.l3_fi.text()))))
            if (self.n == 4):
                Nc = (Nq - 1) * (1 / math.tan(math.radians(float (self.l4_fi.text()))))
            return (Nc)
        except:
            raise Exception(u"\u03C6")
    
    def calculate_KPgamma_terzaghi (self):
        KPgamma = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            KPgamma = (7.5 * math.pow(math.e , (0.0628 *float(self.l1_fi.text())) )) + (0.001542 * pow(math.e , (0.2583)*float(self.l1_fi.text())))
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            KPgamma = (7.5 * math.pow(math.e , (0.0628 *float(self.l2_fi.text())) )) + (0.001542 * pow(math.e , (0.2583)*float(self.l2_fi.text())))
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            KPgamma = (7.5 * math.pow(math.e, (0.0628 * float(self.l3_fi.text())))) + (0.001542 * pow(math.e, (0.2583) * float(self.l3_fi.text())))
        if (self.n == 4):
            KPgamma = (7.5 * math.pow(math.e, (0.0628 * float (self.l4_fi.text())))) + (0.001542 * pow(math.e, (0.2583) * float (self.l4_fi.text())))
        return (KPgamma)
        
        
        
    def calculate_Ngamma_terzaghi(self , KPgamma):
        try:
            Ngamma = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Ngamma = (0.5 * math.tan(math.radians(float(self.l1_fi.text())))) * ((KPgamma /math.pow(math.cos(math.radians(float(self.l1_fi.text()))), 2)) - 1)
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Ngamma = (0.5 * math.tan(math.radians(float(self.l2_fi.text())))) * ((KPgamma /math.pow(math.cos(math.radians(float(self.l2_fi.text()))), 2)) - 1)
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Ngamma = (0.5 * math.tan(math.radians(float(self.l3_fi.text())))) * ((KPgamma / math.pow(math.cos(math.radians(float(self.l3_fi.text()))), 2)) - 1)
            if (self.n == 4):
                Ngamma = (0.5 * math.tan(math.radians(float (self.l4_fi.text())))) * ((KPgamma / math.pow(math.cos(math.radians(float (self.l4_fi.text()))), 2)) - 1)
            return (Ngamma)
        except:
            raise Exception(u"\u03C6")
    
    def calculate_Sc_terzaghi (self , B , L ):
        try:
            if L / B >= 5 :
                return 1
            else :
                Sc = 1 + (0.3 * B / L)
                return (Sc)
        except:
            raise Exception("L")


    def calculate_Sq_terzaghi (self):
        sq = 1
        return (sq)

    def calculate_Sgamma_terzaghi (self , B , L ):
        try:
            if L / B >= 5 :
                return 1
            else :
                Sgamma = 1 - (0.2 * B / L)
                return (Sgamma)
        except:
            raise Exception("L")

    def calculate_q_terzaghi (self , DBase):
        q = 0

        if (float(self.Dwat.text()) > DBase):
        
            if (self.n == 1):
                q = float(self.l1_gammawet.text()) * (DBase)
            if (self.n == 2):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * (DBase - float(self.l1_d.text()))
            
            if (self.n == 3):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * float(self.l2_d.text()) +  (DBase - float(self.l1_d.text())- float(self.l2_d.text()))*float(self.l3_gammawet.text())
            
            if (self.n == 4):
                q = float(self.l1_gammawet.text()) * float(self.l1_d.text()) + float(self.l2_gammawet.text()) * float(self.l2_d.text())+ float(self.l3_gammawet.text()) * float(self.l3_d.text()) +  (DBase - float(self.l1_d.text())- float(self.l2_d.text())- float(self.l3_d.text()))*float(self.l4_gammawet.text())
            
            
        elif (float(self.Dwat.text()) <= DBase) :

            if (self.n == 1 and self.nWater == 1):
                q = float(self.Dwat.text()) * float(self.l1_gammawet.text()) + (DBase - float(self.Dwat.text()))*(float(self.l1_gammasat.text()) - float(self.gammawat.text()))
            if (self.n == 2 and self.nWater == 1):
                q = float(self.Dwat.text())*float(self.l1_gammawet.text())+(float(self.l1_d.text()) - float(self.Dwat.text()))*(float(self.l1_gammasat.text()) - float(self.gammawat.text())) + (DBase - float(self.l1_d.text()))*(float(self.l2_gammasat.text()) - float(self.gammawat.text()))
            
            if (self.n == 2 and self.nWater == 1):
                q = float(self.l1_d.text())*float(self.l1_gammawet.text()) + (float(self.Dwat.text())- float(self.l1_d.text()))*(float(self.l2_gammawet.text())) + (DBase - float(self.Dwat.text()))*(float(self.l2_gammasat.text()) -float(self.gammawat.text()) )
            
            if (self.n == 3 and self.nWater == 1):
                q = float(self.Dwat.text())*float(self.l1_gammawet.text()) + (float(self.l1_d.text()) - float(self.Dwat.text()))*(float(self.l1_gammasat.text()) - float(self.gammawat.text())) + (float(self.l2_d.text()))*(float(self.l2_gammasat.text()) - float(self.gammawat.text())) + (DBase - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammasat.text()) - float(self.gammawat.text()))
            
                    
            if (self.n == 3 and self.nWater == 2):
                q = (float(self.l1_d.text()) * float(self.l1_gammawet.text())) + (float(self.Dwat.text()) - float(self.l1_d.text())) * (float(self.l2_gammawet.text()))+ (float(self.l1_d.text()) + float(self.l2_d.text()) - float(self.Dwat.text())) * ( float(self.l2_gammasat.text()) - float(self.gammawat.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammasat.text())-float(self.gammawat.text()))
            
            if (self.n == 3 and self.nWater == 3):
                q = (float(self.l1_d.text()) * float(self.l1_gammawet.text())) + (float(self.l2_d.text()) * float(self.l2_gammawet.text())) + (float(self.Dwat.text()) - float(self.l1_d.text()) - float(self.l2_d.text()))*(float(self.l3_gammawet.text()))+ (DBase - float(self.Dwat.text()))*(float(self.l3_gammasat.text())-float(self.gammawat.text()))


            if (self.n == 4 and self.nWater == 1):
                q = float(self.Dwat.text()) * float(self.l1_gammawet.text()) + (float(self.l1_d.text()) - float(self.Dwat.text()))* (float(self.l1_gammasat.text()) - float(self.gammawat.text())) + (float(self.l2_d.text()))*(float(self.l2_gammasat.text()) - float(self.gammawat.text())) + (float(self.l3_d.text()))*(float(self.l3_gammasat.text()) - float(self.gammawat.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.gammawat.text()))

            
            if (self.n == 4 and self.nWater == 2):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) + (float(self.Dwat.text())-float(self.l1_d.text()))*float(self.l2_gammawet.text()) + (float(self.l1_d.text()) + float(self.l2_d.text()) - float(self.Dwat.text())) *(float(self.l2_gammasat.text()) - float(self.gammawat.text()) ) + (float(self.l3_d.text()))*(float(self.l3_gammasat.text()) - float(self.gammawat.text())) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.gammawat.text()))
                            
            if (self.n == 4 and self.nWater == 3):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) +float(self.l2_d.text()) * float(self.l2_gammawet.text())+ (float(self.Dwat.text())-float(self.l1_d.text())-float(self.l2_d.text()))*float(self.l3_gammawet.text()) + (float(self.l1_d.text()) + float(self.l2_d.text()) + float(self.l3_d.text()) - float(self.Dwat.text())) *(float(self.l3_gammasat.text()) - float(self.gammawat.text()) ) + (float(self.DBase.text()) - float(self.l1_d.text()) - float(self.l2_d.text())- float(self.l3_d.text()))*(float(self.l4_gammasat.text())-float(self.gammawat.text()))
            if (self.n == 4 and self.nWater == 4):
                q = float(self.l1_d.text()) * float(self.l1_gammawet.text()) +float(self.l2_d.text()) * float(self.l2_gammawet.text())+ float(self.l3_d.text()) * float(self.l3_gammawet.text()) + (float(self.Dwat.text())-float(self.l1_d.text())-float(self.l2_d.text())-float(self.l3_d.text()))*float(self.l4_gammawet.text()) + (DBase - float(self.Dwat.text()))*(float(self.l4_gammasat.text())-float(self.gammawat.text()))




        return (q)
    

    def calculate_qu_terzaghi (self, B , Nc , Sc , q , Nq , Sq , Ngamma , Sgamma):
        c = 0
        gammaforQu = 0
                        
        # what is c in this formula :
        # what is gamma in this formula :
        if (self.n == 1 ):
            c = float(self.l1_c.text())
            gammaforQu = float(self.l1_gammawet.text())
        if (self.n == 2 ):
            c = float(self.l2_c.text())
            gammaforQu = float(self.l2_gammawet.text())
        if (self.n == 3 ):
            c = float(self.l3_c.text())
            gammaforQu = float(self.l3_gammawet.text())
        if (self.n == 4 ):
            c = float(self.l4_c.text())
            gammaforQu = float(self.l4_gammawet.text())
        
                
        qu = (c * Nc * Sc) + (q * Nq * Sq) + (0.5 * gammaforQu * B * Ngamma * Sgamma)
        return (qu)

    def calculate_qall_terzaghi (self , qu):
        try:
            if (float(self.fos.text()) != 0 ):
                qall = qu / float(self.fos.text())
            else :
                qall = float ("inf")
            return (qall)
        except:
            raise Exception("FOS")
    
    
    
    # This function return the result in the console under the inputs 

    
    # def process_terzaghi(self ):
    #     #chooice self.n
    #     self.NqLabel = QLabel()
    #     self.NcLabel = QLabel()
    #     self.NgammaLabel = QLabel()
    #     self.KPgammaLabel = QLabel()
    #     self.ScLabel = QLabel()
    #     self.SqLabel = QLabel()
    #     self.SgammaLabel = QLabel()
    #     self.quLabel = QLabel()
    #     self.qallLabel = QLabel()
 
 
 
    #     self.clear(self.layout)
    #     self.choosingLayer()
    #     self.choosingLayerForWater()
        
        
        
        
    #     self.results_terzaghi(self.layout)
    
    
    ############################Meyerhof method

    def calculate_Nq_meyerhof (self):
        try:
            Nq = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :

                Nq = (math.pow(math.e , (math.pi * math.tan(math.radians(float(self.l1_fi.text())))))) * math.pow(math.tan(math.radians(45 + (float(self.l1_fi.text())/2))),2)
            
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nq = (math.pow(math.e , (math.pi * math.tan(math.radians(float(self.l2_fi.text())))))) * math.pow(math.tan(math.radians(45 + (float(self.l2_fi.text())/2))),2)
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nq = (math.pow(math.e , (math.pi * math.tan(math.radians(float(self.l3_fi.text())))))) * math.pow(math.tan(math.radians(45 + (float(self.l3_fi.text())/2))),2)
            if (self.n == 4):
                Nq = (math.pow(math.e , (math.pi * math.tan(math.radians(float(self.l4_fi.text())))))) * math.pow(math.tan(math.radians(45 + (float(self.l4_fi.text())/2))),2)
            return (Nq)
        except :
            raise Exception(u"\u03C6")
            
    def calculate_Nc_meyerhof (self , Nq):
        try:
            Nc = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Nc = ( Nq - 1 )/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nc = ( Nq - 1 )/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nc = ( Nq - 1 )/math.tan(math.radians(float(self.l3_fi.text())))
            if (self.n == 4):
                Nc = ( Nq - 1 )/math.tan(math.radians(float(self.l4_fi.text())))
                
            return (Nc)
        except :
            raise Exception(u"\u03C6")
        
        
    def calculate_Ngamma_meyerhof (self , Nq):
        try:
            Ngamma = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Ngamma = (Nq - 1) * math.tan(math.radians(1.4 * float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Ngamma = (Nq - 1) * math.tan(math.radians(1.4 * float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Ngamma = (Nq - 1) * math.tan(math.radians(1.4 * float(self.l3_fi.text())))
            if (self.n == 4):
                Ngamma = (Nq - 1) * math.tan(math.radians(1.4 * float(self.l4_fi.text())))
                
            return(Ngamma)
        except :
            raise Exception(u"\u03C6")
            
    def calculate_beta_meyerhof (self):
        try:
            beta = 0
            beta = math.degrees (math.atan( float(self.Qh.text())/float(self.Qv.text()) ))
            return(beta)
        except :
            return (0)

    def calculate_iq_meyerhof (self , beta):
        iq = 0
        iq = math.pow ((1 - beta/90 ), 2)
        return (iq)
        
                
    def calculate_ic_meyerhof (self , beta):
        ic = 0
        ic = math.pow ((1 - beta/90 ), 2)
        return (ic)
        
    def calculate_igamma_meyerhof (self , beta):
        igamma = 0
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                if (float(self.l1_fi.text()) == 0 ):
                    igamma = 0
                if ( 0 < float(self.l1_fi.text()) and float(self.l1_fi.text()) < 10):
                    igamma = (float(self.l1_fi.text())/10) * math.pow((1 - beta/10) , 2 )
                if ( float(self.l1_fi.text()) >= 10):
                    igamma = math.pow( (1 - beta/float(self.l1_fi.text())) , 2)
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                if (float(self.l2_fi.text()) == 0 ):
                    igamma = 0
                if ( 0 < float(self.l2_fi.text()) and float(self.l2_fi.text()) < 10):
                    igamma = (float(self.l2_fi.text())/10) * math.pow((1 - beta/10) , 2 )
                if ( float(self.l2_fi.text()) >= 10):
                    igamma = math.pow( (1 - beta/float(self.l2_fi.text())) , 2)
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                if (float(self.l3_fi.text()) == 0 ):
                    igamma = 0
                if ( 0 < float(self.l3_fi.text()) and float(self.l3_fi.text()) < 10):
                    igamma = (float(self.l3_fi.text())/10) * math.pow((1 - beta/10) , 2 )
                if ( float(self.l3_fi.text()) >= 10):
                    igamma = math.pow( (1 - beta/float(self.l3_fi.text())) , 2)
            if (self.n == 4):
                if (float(self.l4_fi.text()) == 0 ):
                    igamma = 0
                if ( 0 < float(self.l4_fi.text()) and float(self.l4_fi.text()) < 10):
                    igamma = (float(self.l4_fi.text())/10) * math.pow((1 - beta/10) , 2 )
                if ( float(self.l4_fi.text()) >= 10):
                    igamma = math.pow( (1 - beta/float(self.l4_fi.text())) , 2)
            return (igamma)
        except :
            raise Exception("i gamma")
            
    
    def calculate_KP_meyerhof (self):
        try:
            KP = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :

                KP = math.pow( math.tan( math.radians( 45 + float(self.l1_fi.text())/2)) , 2 )

            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                KP = math.pow( math.tan( math.radians( 45 + float(self.l2_fi.text())/2 ) ) , 2 )
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                KP = math.pow( math.tan( math.radians( 45 + float(self.l3_fi.text())/2 ) ) , 2 )
            if (self.n == 4):
                KP = math.pow( math.tan( math.radians( 45 + float(self.l4_fi.text())/2 ) ) , 2 )
        
            return (KP)
        except :
            raise Exception(u"\u03C6")
        
    def calculate_dc_meyerhof (self , KP , DBase , B ):
        dc = 0
        dc = 1 + 0.2*math.pow (KP , 1/2)*DBase/B
        return (dc)
    
    def calculate_dq_meyerhof (self , KP , DBase , B ):
        dq = 0
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                if (float(self.l1_fi.text()) == 0 ):
                    dq = 1
                if ( 0 < float(self.l1_fi.text()) and float(self.l1_fi.text()) < 10):
                    dq = 1 + 0.0119*float(self.l1_fi.text())*DBase/B
                if ( float(self.l1_fi.text()) >= 10):
                    dq = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                if (float(self.l2_fi.text()) == 0 ):
                    dq = 1
                if ( 0 < float(self.l2_fi.text()) and float(self.l2_fi.text()) < 10):
                    dq = 1 + 0.0119*float(self.l2_fi.text())*DBase/B
                if ( float(self.l2_fi.text()) >= 10):
                    dq = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                if (float(self.l3_fi.text()) == 0 ):
                    dq = 1
                if ( 0 < float(self.l3_fi.text()) and float(self.l3_fi.text()) < 10):
                    dq = 1 + 0.0119*float(self.l3_fi.text())*DBase/B
                if ( float(self.l3_fi.text()) >= 10):
                    dq = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
            if (self.n == 4):
                if (float(self.l4_fi.text()) == 0 ):
                    dq = 1
                if ( 0 < float(self.l4_fi.text()) and float(self.l4_fi.text()) < 10):
                    dq = 1 + 0.0119*float(self.l4_fi.text())*DBase/B
                if ( float(self.l4_fi.text()) >= 10):
                    dq = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
            return (dq)
        except :
            raise Exception("dq")
        
    
    def calculate_dgamma_meyerhof (self , KP , DBase , B ):
        dgamma = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            if (float(self.l1_fi.text()) == 0 ):
                dgamma = 1
            if ( 0 < float(self.l1_fi.text()) and float(self.l1_fi.text()) < 10):
                dgamma = 1 + 0.0119*float(self.l1_fi.text())*DBase/B
            if ( float(self.l1_fi.text()) >= 10):
                dgamma = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            if (float(self.l2_fi.text()) == 0 ):
                dgamma = 1
            if ( 0 < float(self.l2_fi.text()) and float(self.l2_fi.text()) < 10):
                dgamma = 1 + 0.0119*float(self.l2_fi.text())*DBase/B
            if ( float(self.l2_fi.text()) >= 10):
                dgamma = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            if (float(self.l3_fi.text()) == 0 ):
                dgamma = 1
            if ( 0 < float(self.l3_fi.text()) and float(self.l3_fi.text()) < 10):
                dgamma = 1 + 0.0119*float(self.l3_fi.text())*DBase/B
            if ( float(self.l3_fi.text()) >= 10):
                dgamma = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
        if (self.n == 4):
            if (float(self.l4_fi.text()) == 0 ):
                dgamma = 1
            if ( 0 < float(self.l4_fi.text()) and float(self.l4_fi.text()) < 10):
                dgamma = 1 + 0.0119*float(self.l4_fi.text())*DBase/B
            if ( float(self.l4_fi.text()) >= 10):
                dgamma = 1 + 0.1*math.pow (KP , 1/2)*DBase/B
        return (dgamma)
    
    def calculate_Sc_meyerhof(self , KP , L , B ):
        Sc = 0
        Sc = 1 + (0.2*KP*(B/L))
        return (Sc)
    
    
    def calculate_Sgamma_meyerhof(self , KP , L , B ):
        Sgamma = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            if (float(self.l1_fi.text()) == 0 ):
                Sgamma = 1
            if ( 0 < float(self.l1_fi.text()) and float(self.l1_fi.text()) < 10):
                Sgamma = (0.0142*float(self.l1_fi.text())*B/L) + 1
            if ( float(self.l1_fi.text()) >= 10):
                Sgamma = 1 + 0.1*KP*B/L
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            if (float(self.l2_fi.text()) == 0 ):
                Sgamma = 1
            if ( 0 < float(self.l2_fi.text()) and float(self.l2_fi.text()) < 10):
                Sgamma = (0.0142*float(self.l2_fi.text())*B/L) + 1
            if ( float(self.l2_fi.text()) >= 10):
                Sgamma = 1 + 0.1*KP*B/L
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            if (float(self.l3_fi.text()) == 0 ):
                Sgamma = 1
            if ( 0 < float(self.l3_fi.text()) and float(self.l3_fi.text()) < 10):
                Sgamma = (0.0142*float(self.l3_fi.text())*B/L) + 1
            if ( float(self.l3_fi.text()) >= 10):
                Sgamma = 1 + 0.1*KP*B/L
        if (self.n == 4):
            if (float(self.l4_fi.text()) == 0 ):
                Sgamma = 1
            if ( 0 < float(self.l4_fi.text()) and float(self.l4_fi.text()) < 10):
                Sgamma = (0.0142*float(self.l4_fi.text())*B/L) + 1
            if ( float(self.l4_fi.text()) >= 10):
                Sgamma = 1 + 0.1*KP*B/L
        return (Sgamma)
        
        
    
    def calculate_Sq_meyerhof(self , KP , L , B ):
        Sq = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            if (float(self.l1_fi.text()) == 0 ):
                Sq = 1
            if ( 0 < float(self.l1_fi.text()) and float(self.l1_fi.text()) < 10):
                Sq = (0.0142*float(self.l1_fi.text())*B/L) + 1
            if ( float(self.l1_fi.text()) >= 10):
                Sq = 1 + (0.1*KP*(B/L))
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            if (float(self.l2_fi.text()) == 0 ):
                Sq = 1
            if ( 0 < float(self.l2_fi.text()) and float(self.l2_fi.text()) < 10):
                Sq = (0.0142*float(self.l2_fi.text())*B/L) + 1
            if ( float(self.l2_fi.text()) >= 10):
                Sq = 1 + 0.1*KP*B/L
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            if (float(self.l3_fi.text()) == 0 ):
                Sq = 1
            if ( 0 < float(self.l3_fi.text()) and float(self.l3_fi.text()) < 10):
                Sq = (0.0142*float(self.l3_fi.text())*B/L) + 1
            if ( float(self.l3_fi.text()) >= 10):
                Sq = 1 + 0.1*KP*B/L
        if (self.n == 4):
            if (float(self.l4_fi.text()) == 0 ):
                Sq = 1
            if ( 0 < float(self.l4_fi.text()) and float(self.l4_fi.text()) < 10):
                Sq = (0.0142*float(self.l4_fi.text())*B/L) + 1
            if ( float(self.l4_fi.text()) >= 10):
                Sq = 1 + 0.1*KP*B/L
        return (Sq)
        
        
    def calculate_qu_meyerhof(self , Nc , Sc , dc , ic , q , Nq , Sq , dq , iq , B , Ngamma , Sgamma , dgamma , igamma):
        c = 0
        gammaforQu = 0
                        
        # what is c in this formula :
        # what is gamma in this formula :
        if (self.n == 1 ):
            c = float(self.l1_c.text())
            gammaforQu = float(self.l1_gammawet.text())
        if (self.n == 2 ):
            c = float(self.l2_c.text())
            gammaforQu = float(self.l2_gammawet.text())
        if (self.n == 3 ):
            c = float(self.l3_c.text())
            gammaforQu = float(self.l3_gammawet.text())
        if (self.n == 4 ):
            c = float(self.l4_c.text())
            gammaforQu = float(self.l4_gammawet.text())
            
        qu = 0
        qu = (c * Nc * Sc * dc * ic) + (q * Nq * Sq * dq * iq) + (0.5 * B * gammaforQu * Ngamma * Sgamma * dgamma * igamma)
        return (qu)
    
    def calculate_qall_meyerhof (self , qu):
        if (float(self.fos.text()) != 0 ):
            qall = qu / float(self.fos.text())
        else :
            qall = float ("inf")
        return (qall)

        
    # This function will print the output in the consule and put it under the inputs 

    # def process_meyerhof (self):
    #     self.NqLabel = QLabel()
    #     self.NcLabel = QLabel()
    #     self.NgammaLabel = QLabel()
    #     self.betaLabel = QLabel()
    #     self.dcLabel = QLabel()
    #     self.ScLabel = QLabel()
    #     self.quLabel = QLabel()
    #     self.qallLabel = QLabel()
        

    #     self.clear(self.layout)
    #     self.choosingLayer()
    #     self.choosingLayerForWater()
        
    #     self.results_meyerhof(self.layout)
    
    
    
            
    # This function will print the output in the consule and put it under the inputs 
    
        
    
    # def process_hansen(self ):
    #     #chooice self.n
    #     self.NqLabel = QLabel()
    #     self.NcLabel = QLabel()
    #     self.NgammaLabel = QLabel()
    #     self.ScLabel = QLabel()
    #     self.dcLabel = QLabel()
    #     self.SqLabel = QLabel()
    #     self.SgammaLabel = QLabel()
    #     self.quLabel = QLabel()
    #     self.qallLabel = QLabel()
 
 
 
    #     self.choosingLayer()
    #     self.choosingLayerForWater()
        
        
    #     self.results_hansen(self.layout)
    
    
    def calculate_Nq_hansen (self):
        try:
            Nq = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Nq = math.pow (math.e , (math.pi * math.tan(math.radians(float(self.l1_fi.text()))))) * math.pow(math.tan(math.radians(45 + float(self.l1_fi.text())/2)) , 2 )
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nq = math.pow (math.e , (math.pi * math.tan(math.radians(float(self.l2_fi.text()))))) * math.pow(math.tan(math.radians(45 + float(self.l2_fi.text())/2)) , 2 )
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nq = math.pow (math.e , (math.pi * math.tan(math.radians(float(self.l3_fi.text()))))) * math.pow(math.tan(math.radians(45 + float(self.l3_fi.text())/2)) , 2 )
            if (self.n == 4):
                Nq = math.pow (math.e , (math.pi * math.tan(math.radians(float(self.l4_fi.text()))))) * math.pow(math.tan(math.radians(45 + float(self.l4_fi.text())/2)) , 2 )
            return (Nq)
        except :
            raise Exception(u"\u03C6")

    
    def calculate_Nc_hansen (self , Nq):
        try:
            Nc = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Nc = (Nq - 1)/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Nc = (Nq - 1)/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Nc = (Nq - 1)/math.tan(math.radians(float(self.l3_fi.text())))
            if (self.n == 4):
                Nc = (Nq - 1)/math.tan(math.radians(float(self.l4_fi.text())))
            return(Nc)
        except :
            raise Exception(u"\u03C6")
    
    
    def calculate_Ngamma_hansen (self , Nq ):
        try:
            Ngamma = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                Ngamma = 1.5 *(Nq - 1)*math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                Ngamma = 1.5 *(Nq - 1)*math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                Ngamma = 1.5 *(Nq - 1)*math.tan(math.radians(float(self.l3_fi.text())))
            if (self.n == 4):
                Ngamma = 1.5 *(Nq - 1)*math.tan(math.radians(float(self.l4_fi.text())))
            return (Ngamma)
        except :
            raise Exception(u"\u03C6")
    
    
    
    def calculate_Sc_hansen (self , Nq , Nc , B , L):
        Sc = 1 + (Nq/Nc)*(B/L)
        return (Sc)
    
    def calculate_Sq_hansen (self , B , L):
        Sq = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            Sq = 1 + (B / L)*math.sin(math.radians(float(self.l1_fi.text())))
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            Sq = 1 + (B / L)*math.sin(math.radians(float(self.l2_fi.text())))
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            Sq = 1 + (B / L)*math.sin(math.radians(float(self.l3_fi.text())))
        if (self.n == 4):
            Sq = 1 + (B / L)*math.sin4(math.radians(float(self.l4_fi.text())))
        return(Sq)
    
    
    
    def calculate_Sgamma_hansen (self , B , L):
        Sgamma = 1 - 0.4 * B / L
        if (Sgamma >= 0.6):
            pass
        else :
            Sgamma = 0.6
        
        return (Sgamma)
        
    def calculate_dc_hansen (self , DBase , B ):
        dc = 0
        if (DBase <= B ):
            dc = 1 + 0.4*DBase/B
        else :
            dc = 1 + 0.4*math.atan(DBase/B)
        return (dc)
    
    def calculate_dq_hansen (self , DBase , B):
        dq = 0
        if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
            if (DBase <= B ):
                dq = 1 + 2 * math.tan(math.radians(float(self.l1_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l1_fi.text())))) , 2) * DBase / B
            else :
                dq = 1 + 2 * math.tan(math.radians(float(self.l1_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l1_fi.text())))) , 2) * math.atan(DBase / B)
        if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
            if (DBase <= B ):
                dq = 1 + 2 * math.tan(math.radians(float(self.l2_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l2_fi.text())))) , 2) * DBase / B
            else :
                dq = 1 + 2 * math.tan(math.radians(float(self.l2_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l2_fi.text())))) , 2) * math.atan(DBase / B)
        if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
            if (DBase <= B ):
                dq = 1 + 2 * math.tan(math.radians(float(self.l3_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l3_fi.text())))) , 2) * DBase / B
            else :
                dq = 1 + 2 * math.tan(math.radians(float(self.l3_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l3_fi.text())))) , 2) * math.atan(DBase / B)
        if (self.n == 4):
            if (DBase <= B ):
                dq = 1 + 2 * math.tan(math.radians(float(self.l4_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l4_fi.text())))) , 2) * DBase / B
            else :
                dq = 1 + 2 * math.tan(math.radians(float(self.l4_fi.text())))*math.pow ((1-math.sin(math.radians(float(self.l4_fi.text())))) , 2) * math.atan(DBase / B)
        
        
        return (dq)



    def calculate_dgamma_hansen (self):
        return (1)
    
    def calculate_bc_hansen (self):
        bc = 1 - float(self.eta.text())/147
        return(bc)
    
    
    def calculate_bq_hansen (self):
        try:
            bq = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                bq = math.pow(math.e , (-2*float(self.eta.text())*(math.pi/180)* math.tan(math.radians(float(self.l1_fi.text())) )))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                bq = math.pow(math.e , (-2*float(self.eta.text())*(math.pi/180)* math.tan(math.radians(float(self.l2_fi.text())) )))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                bq = math.pow(math.e , (-2*float(self.eta.text())*(math.pi/180)* math.tan(math.radians(float(self.l3_fi.text())) )))
            if (self.n == 4 ):
                bq = math.pow(math.e , (-2*float(self.eta.text())*(math.pi/180)* math.tan(math.radians(float(self.l4_fi.text())) )))
            return(bq)
        except :
            raise Exception(u"\u03C6")
        
    def calculate_bgamma_hansen (self):
        try:
            bgamma = 0
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                bgamma = math.pow(math.e , (-2.7*float(self.eta.text()) *(math.pi/180)*math.tan(math.radians(floatself.l1_fi.text())) ))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                bgamma = math.pow(math.e , (-2.7*float(self.eta.text()) *(math.pi/180)*math.tan(math.radians(floatself.l2_fi.text())) ))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                bgamma = math.pow(math.e , (-2.7*float(self.eta.text()) *(math.pi/180)*math.tan(math.radians(floatself.l3_fi.text())) ))
            if (self.n ==4 ) :
                bgamma = math.pow(math.e , (-2.7*float(self.eta.text()) *(math.pi/180)*math.tan(math.radians(floatself.l4_fi.text())) ))
        
            return(bgamma)
        except :
            raise Exception(u"\u03C6")
        
    def calculate_gc_hansen (self):
        gc = 0
        gc = 1 - float(self.psi.text())/147
        return(gc)
    
    def calculate_gq_hansen(self):
        try:
            gq = math.pow((1-0.5*math.tan(math.radians(float(self.psi.text())))),5)
            return(gq)
        except :
            raise Exception(u"\u03C8")

    def calculate_ggamma_hansen (self):
        try:
            return( math.pow((1-0.5*math.tan(math.radians(float(self.psi.text())))),5))
        except :
            raise Exception(u"\u03C8")
    def calculate_ca_hansen (self):
        ca = 0
        if (self.n == 1):
            ca = 0.8 * float(self.l1_c.text())
        if (self.n == 2):
            ca = 0.8 * float(self.l2_c.text())
        if (self.n == 3):
            ca = 0.8 * float(self.l3_c.text())
        if (self.n == 4):
            ca = 0.8 * float(self.l4_c.text())
        
        return(ca)
        
    def calculate_Af_hansen (self , B , L):
        return(B*L)
    
    def calculate_mB_hansen (self , B , L):
        try:
            mB = (2 + B/L)/(1 + B/L)
            return (mB)
        except :
            raise Exception("L")
            
    def calculate_mL_hansen (self , B , L):
        try:
            mL = (2 + L/B)/(1 + L/B)
            return (mL)
        except :
            raise Exception("B")


    def calculate_m_hansen (self , mB , mL):
        m = math.pow (((mB*mB) + (mL*mL)) , 1/2)
        return(m)
    
    def calculate_iq_hansen(self , Af , ca , m):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                y = 1/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l3_fi.text())))
            elif (self.n == 4):
                y = 1/math.tan(math.radians(float(self.l4_fi.text())))
            
            x = 1 - (0.5*float(self.Qh.text()))/(float(self.Qv.text())+ (Af*ca*y))
            return (math.pow (x , m))
        except :
            raise Exception(u"\u03C6")

        
    def calculate_igamma_hansen (self , Af , ca , m):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                y = 1/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l3_fi.text())))
            elif (self.n == 4):
                y = 1/math.tan(math.radians(float(self.l4_fi.text())))
            
            x = 1 - ((0.7 - float(self.eta.text())/450)*float(self.Qh.text()))/(float(self.Qv.text())+(Af*ca*y))
            
            return(math.pow(x , m+1))
        except :
            raise Exception(u"\u03C6")

        
    def calculate_ic_hansen (self , iq , Nq):
        try:
            ic = iq - ((1-iq)/(Nq-1))
            return(ic)
        except :
            raise Exception(u"\u03C6")

    
    def calculate_qu_hansen (self , Nc , Sc , dc , ic , gc , bc , q , Nq , Sq , dq , iq , gq , bq , Ngamma , Sgamma , dgamma , igamma , ggamma , bgamma ):
        c = 0
        gammaforQu = 0
                        
        # what is c in this formula :
        # what is gamma in this formula :
        if (self.n == 1 ):
            c = float(self.l1_c.text())
            gammaforQu = float(self.l1_gammawet.text())
        if (self.n == 2 ):
            c = float(self.l2_c.text())
            gammaforQu = float(self.l2_gammawet.text())
        if (self.n == 3 ):
            c = float(self.l3_c.text())
            gammaforQu = float(self.l3_gammawet.text())
        if (self.n == 4 ):
            c = float(self.l4_c.text())
            gammaforQu = float(self.l4_gammawet.text())
            
        qu = 0
        qu = (c * Nc * Sc * dc * ic * gc * bc)+(q * Nq * Sq * dq * iq * gq * bq)+(0.5 * float(self.B.text()) * gammaforQu * Ngamma * Sgamma * dgamma * igamma * ggamma * bgamma)
        return (qu)
    
    
    
    
    
        
    
    
    def calculate_Nq_vesic (self):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            
            Nq = math.pow(math.e , (math.pi*math.tan(math.radians(fi)))) * math.pow (math.tan(math.radians(45+fi/2)) , 2)
            return(Nq)
        except :
            raise Exception(u"\u03C6")

        
    def calculate_Nc_vesic (self , Nq ):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            
            Nc = (Nq - 1)/math.tan(math.radians(fi))
            return(Nc)
        except :
            raise Exception(u"\u03C6")

    
    def calculate_Ngamma_vesic (self , Nq):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            
            Ngamma = 2*(1+Nq)*math.tan(math.radians(fi))
            return(Ngamma)
        except :
            raise Exception(u"\u03C6")


    def calculate_Sc_vesic (self , Nq , Nc , B , L):
        try:
            Sc = 1 + (Nq/Nc)*(B/L)
            return(Sc)
        except :
            raise Exception(u"\u03C6")

    def calculate_Sq_vesic (self , B , L):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())

            return (1+(B/L)*math.tan(math.radians(fi)))
            
        except :
            raise Exception(u"\u03C6")

    def calculate_Sgamma_vesic (self , B , L ):
        try:
            Sgamma = 1 - 0.4 * B / L
            if (Sgamma >= 0.6):
                pass
            else :
                Sgamma = 0.6
            
            return (Sgamma)
        except :
            raise Exception("L")

    
    
    
    def calculate_dc_vesic (self , DBase , B ):
        try:
            if (DBase <= B ):
                dc = 1 + 0.4 * DBase / B
            else :
                dc = 1 + 0.4 * math.atan(DBase/B)
            return (dc)
        except :
            raise Exception("B")

        
    def calculate_dq_vesic (self , DBase , B):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            fi = math.radians(fi)
                    
            if (DBase <= B ):
                dq = 1 + 2 * math.tan(fi) * math.pow ((1-math.sin(fi)) , 2)*DBase/B
            else :
                dq = 1 + 2 * math.tan(fi) * math.pow ((1-math.sin(fi)) , 2)* math.atan (DBase/B)

            return (dq)
        except :
            raise Exception(u"\u03C6")


    def calculate_dgamma_vesic (self):
        return (1)
  
    def calculate_bc_vesic (self):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            fi = math.radians(fi)
            
            bc = 1 - (2 * math.radians(float(self.eta.text()))/5.14*math.tan(fi))
            return (bc)
        
        except :
            raise Exception(u"\u03C6")
    
    
    def calculate_bq_vesic (self):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            fi = math.radians(fi)
            
            bq = math.pow ( 1 - math.radians(float(self.eta.text()))*math.tan(fi) , 2 )
            return (bq)
        except :
            raise Exception(u"\u03C6")

            
        
    def calculate_bgamma_vesic (self):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                fi = float(self.l1_fi.text())
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                fi = float(self.l2_fi.text())
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())
            fi = math.radians(fi)
            
            bgamma = math.pow ( 1 - math.radians(float(self.eta.text()))*math.tan(fi) , 2 )
            return (bgamma)
        except :
            raise Exception(u"\u03C6")

        
    def calculate_ca_vesic (self):
        ca = 0
        if (self.n == 1):
            ca = 0.8 * float(self.l1_c.text())
        if (self.n == 2):
            ca = 0.8 * float(self.l2_c.text())
        if (self.n == 3):
            ca = 0.8 * float(self.l3_c.text())
        if (self.n == 4):
            ca = 0.8 * float(self.l4_c.text())
        
        return(ca)
    
    def calculate_Af_vesic (self , B , L):
        return(B*L)
    
    def calculate_mB_vesic (self , B , L):
        try:
            mB = (2 + B/L)/(1 + B/L)
            return (mB)
        except :
            raise Exception("L")

    
        
    def calculate_mL_vesic (self , B , L):
        try:
            mL = (2 + L/B)/(1 + L/B)
            return (mL)
        except :
            raise Exception("B")

    
    
    def calculate_m_vesic (self , mB , mL):
        m = math.pow (((mB*mB) + (mL*mL)) , 1/2)
        return(m)
    
    def calculate_iq_vesic (self , Af , ca , m):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                y = 1/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l3_fi.text())))
            elif (self.n == 4):
                y = 1/math.tan(math.radians(float(self.l4_fi.text())))
            
            x = 1 - (float(self.Qh.text()))/(float(self.Qv.text())+ (Af*ca*y))
            return (math.pow (x , m))
        except :
            raise Exception(u"\u03C6")

    
    def calculate_igamma_vesic(self , Af , ca , m):
        try:
            if (self.n == 1 and float(self.DBase.text()) != float(self.l1_d.text())) :
                y = 1/math.tan(math.radians(float(self.l1_fi.text())))
            if ((self.n == 2 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text()) ) or (self.n == 1 and float(self.DBase.text()) == float(self.l1_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l2_fi.text())))
            if ((self.n == 3 and float(self.DBase.text()) != float(self.l1_d.text())+ float(self.l2_d.text())+ float(self.l3_d.text()) ) or (self.n == 2 and float(self.DBase.text()) == float(self.l1_d.text())+float(self.l2_d.text()))) :
                y = 1/math.tan(math.radians(float(self.l3_fi.text())))
            elif (self.n == 4):
                y = 1/math.tan(math.radians(float(self.l4_fi.text())))
            
            x = 1 - ((float(self.Qh.text()))/(float(self.Qv.text())+(Af*ca*y)))
            
            return(math.pow(x , m+1))
        except :
            raise Exception(u"\u03C6")

    
    def calculate_ic_vesic (self , iq , Nq ):
        try:
            return (iq - (1 - iq)/(Nq - 1))
        except :
            raise Exception(u"\u03C6")

    def calculate_gc_vesic (self , iq ):
        try:
            if (self.n == 1):
                fi = float(self.l1_fi.text())
            if (self.n == 2):
                fi = float(self.l2_fi.text())
            if (self.n == 3):
                fi = float(self.l3_fi.text())
            if (self.n == 4):
                fi = float(self.l4_fi.text())

            fi = math.radians(fi)
            gc = iq - (1 - iq)/(5.14 * math.tan(fi))
            return (gc)
        except :
            raise Exception(u"\u03C6")

        
    def calculate_gq_vesic (self):
        try:
            fi = float(self.psi.text())
            fi = math.radians(fi)
            
            return(math.pow (1-math.tan(fi) , 2))
        except :
            raise Exception(u"\u03A8")

            
    def calculate_ggamma_vesic (self):
        try:
            fi = float(self.psi.text())
            fi = math.radians(fi)
            
            return(math.pow (1-math.tan(fi) , 2))
        except :
            raise Exception(u"\u03A8")

    # def process_vesic(self ):
    #     #chooice self.n
    #     self.NqLabel = QLabel()
    #     self.NcLabel = QLabel()
    #     self.NgammaLabel = QLabel()
    #     self.ScLabel = QLabel()
    #     self.dcLabel = QLabel()
    #     self.SqLabel = QLabel()
    #     self.SgammaLabel = QLabel()
    #     self.quLabel = QLabel()
    #     self.qallLabel = QLabel()
 
 
 
    #     self.choosingLayer()
    #     self.choosingLayerForWater()
        
        
    #     self.results_vesic(self.layout)
    
    
    
    
    
    

    def findingSteps (self , s):
        if s == "1 Step":
            self.steps = 1
        elif s == "2 Steps":
            self.steps = 2
        elif s == "3 Steps":
            self.steps = 3
        elif s == "4 Steps":
            self.steps = 4
    

    def activeMethod (self , s ):
        if (s == "Terzaghi"):
            self.method = "Terzaghi"
            self.psi.setEnabled(False)
            self.Qh.setEnabled(False)
            self.eta.setEnabled(False)
        if (s == "Vesic"):
            self.method = "Vesic"
            self.psi.setEnabled(True)
            self.Qh.setEnabled(True)
            self.eta.setEnabled(True)
        if (s == "Hansen"):
            self.method = "Hansen"
            self.psi.setEnabled(True)
            self.Qh.setEnabled(True)
            self.eta.setEnabled(True)
        if (s == "Meyerhof"):
            self.method = "Meyerhof"
            self.psi.setEnabled(False)
            self.Qh.setEnabled(True)
            self.eta.setEnabled(False)
        
        
        
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


    # def process(self):
    #     self.handelBbiggerThanL()
    #     if (self.method == "Terzaghi"):
    #         self.process_terzaghi()
    #     if (self.method == "Meyerhof"):
    #         self.process_meyerhof()
    #     if (self.method == "Hansen"):
    #         self.process_hansen()
    #     if (self.method == "Vesic"):
    #         self.process_vesic()

    

    def drawGraph (self):
        
        if self.handelInvalidFOS() :
            return
        if self.handelInvalidLorB():
            return 
        if self.handelInvalidfi():
            return

        self.handelBbiggerThanL()

        try:
            if (self.method == "Terzaghi"):
                self.drawGraph_terzaghi()
            if (self.method == "Meyerhof"):
                self.drawGraph_meyerhof()
            if (self.method == "Hansen"):
                self.drawGraph_hansen()
            if (self.method == "Vesic"):
                self.drawGraph_vesic()
        except Exception as e:
       
            self.inputError(str(e))


    def handelBbiggerThanL(self):
        if float(self.L.text()) < float(self.B.text()):
            temp = float(self.L.text())
            self.L.setText(self.B.text())
            self.B.setText(str(temp))
            
            error_dialog = QErrorMessage()
            error_dialog.showMessage(' مقدار ورودی عرض پی سطحی شما بزرگتر از مقدار طول پس سطحی است بنابراین برنامه مقدار ورودی طول و عرض را با یکدیگر جابجا کرد !')
            error_dialog.exec_()
            

    def handelInvalidFOS(self):
        if float(self.fos.text()) < 1 :
            error_dialog = QErrorMessage()
            error_dialog.showMessage('مقدار FOS وارد شده نامعتبر است')
            error_dialog.exec_()
            return (1)
        return 0

    def handelInvalidLorB(self):
        if float(self.B.text()) < 0  :
            error_dialog = QErrorMessage()
            error_dialog.showMessage('مقدار B وارد شده نامعتبر است')
            error_dialog.exec_()
            return (1)
        if float(self.L.text()) < 0  :
            error_dialog = QErrorMessage()
            error_dialog.showMessage('مقدار L وارد شده نامعتبر است')
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

    
