import sys
from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,QCheckBox,
)
from PySide6.QtGui import QAction,QIcon,QKeySequence

class MainWindow(QMainWindow): # Adding a toolbar
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
    def onMyToolBarButtonClick(self,s):
        print("click",s)
        
class MainWindow_2(QMainWindow): # Adding a QAction
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        
    def onMyToolBarButtonClick(self,s):
        print("click",s)
    
class MainWindow_3(QMainWindow): # Status bar
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)   
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("Your button",self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
       
        toolbar.addAction(button_action)
        
        self.setStatusBar(QStatusBar(self))   
        
    def onMyToolBarButtonClick(self, s):
            print("click", s)

class MainWindow_4(QMainWindow): # QIcon
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        '''
            Flag	Behavior
            Qt.ToolButtonIconOnly	Icon only, no text
            Qt.ToolButtonTextOnly	Text only, no icon
            Qt.ToolButtonTextBesideIcon	Icon and text, with text beside the icon
            Qt.ToolButtonTextUnderIcon	Icon and text, with text under the icon
  (default) Qt.ToolButtonFollowStyle	Follow the host desktop style
        '''
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon("fish.png"), " Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        self.setStatusBar(QStatusBar(self))
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
    
class MainWindow_5(QMainWindow): # QToolbar Summary
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon("fish.png"),"Your button",self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        
        button_action2 = QAction(QIcon("fish.png"),"Your button2",self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        
        toolbar.addAction(button_action)
        toolbar.addAction(button_action2)
        
        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
class MainWindow_6(QMainWindow): # Menus
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        button_action = QAction(QIcon("fish.png"),"Your button",self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # add a keyboard shortcut
        # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)       
        button_action.setShortcut(Qt.CTRL+Qt.Key_P)
        # or button_action.setShortcut(QKeySequence("Ctrl+p"))
        
        button_action2 = QAction(QIcon("fish.png"),"Your button2",self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        
        toolbar.addAction(button_action)
        toolbar.addAction(button_action2)
        
        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        # add a submenu
        file_submenu =file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
    
    
    
    
app = QApplication(sys.argv)
w = MainWindow_6()
w.show()
app.exec()    