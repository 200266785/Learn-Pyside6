''' 4 Basic layouts
Layout	Behaviour
QHBoxLayout	Linear horizontal layout
QVBoxLayout	Linear vertical layout
QGridLayout	In indexable grid XxY
QStackedLayout	Stacked (z) in front of one another

'''
import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QGridLayout, 
    QStackedLayout,
    QPushButton,
    QLabel,
    QTabWidget,
)
from PySide6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow): # QVBoxLayout
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
class MainWindow_2(QMainWindow): # QHBoxLayout
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        
        layout = QHBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)       

class MainWindow_3(QMainWindow): # Nesting layouts
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)
        
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
        
        layout1.addLayout(layout2)
        
        layout1.addWidget(Color('green'))
        
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
        
        layout1.addLayout(layout3)
        
        widget = QWidget()
        widget.setLayout(layout1)
        
        self.setCentralWidget(widget)   

class MainWindow_4(QMainWindow): # QGridLayout widgets arranged in a grid
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        layout = QGridLayout()
        
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('green'),1,0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)
        layout.addWidget(Color('purple'), 3, 2)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainWindow_5(QMainWindow): # QStackedLayout multiple widgets in the same space
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        layout = QStackedLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))
        
        layout.setCurrentIndex(3)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainWindow_6(QMainWindow): # A custom tab-like interface implemented using QStackedLayout.
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        
        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))
        
        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))
        
        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))
        
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

class MainWindow_7(QMainWindow): # QTabWidget
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        
        for n,color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
            
        self.setCentralWidget(tabs)
        
app = QApplication(sys.argv)
window = MainWindow_7()
window.show()

app.exec()