import sys
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        
class MainWindow(QMainWindow):  # Creating a new window #1
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
    
    def show_new_window(self,checked):
        self.w = AnotherWindow()
        self.w.show()
        
class MainWindow_2(QMainWindow): # Creating a new window #2
        def __init__(self):
            super().__init__()
            self.w = None # No external window yet.
            self.button = QPushButton("Push for Window")
            self.button.clicked.connect(self.show_new_window_2)
            self.setCentralWidget(self.button)
        def show_new_window(self,checked):
            if self.w is None:
                self.w = AnotherWindow()
            self.w.show()

class MainWindow_3(QMainWindow): # Toggling a window
        def __init__(self):
            super().__init__()
            self.w = None # No external window yet.
            self.button = QPushButton("Push for Window")
            self.button.clicked.connect(self.show_new_window)
            self.setCentralWidget(self.button)
        def show_new_window(self,checked):
            if self.w is None:
                self.w = AnotherWindow()
                self.w.show()  
            else:
                self.w = None # Discard reference, close window.
                
        def show_new_window_2(self, checked): # call .close()
            if self.w is None:
                self.w = AnotherWindow()
                self.w.show()

            else:
                self.w.close()  # Close window.
                self.w = None  # Discard reference.
                  
class MainWindow_4(QMainWindow): # Persistent windows
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow() # create new window at start-up
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        self.w.show()  # use .show() to display them when needed      

class MainWindow_5(QMainWindow): # Showing & hiding persistent windows
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)
    def toggle_window(self,checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

class MainWindow_6(QMainWindow): # Multiple windows
    def __init__(self):
        super().__init__()
        self.w1 = AnotherWindow()
        self.w2 = AnotherWindow()
        self.button1 = QPushButton("Push for Window_1")
        self.button2 = QPushButton("Push for Window_2")
        
        self.button1.clicked.connect(self.toggle_window_1)
        self.button2.clicked.connect(self.toggle_window_2)        
        
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        
        w = QWidget()
        w.setLayout(layout)
        
        self.setCentralWidget(w)        
       
    def toggle_window_1(self,checked):
        if self.w1.isVisible():
            self.w1.hide()
        else:
            self.w1.show()
    def toggle_window_2(self,checked):
        if self.w2.isVisible():
            self.w2.hide()
        else:
            self.w2.show()

class MainWindow_7(QMainWindow): # Multiple windows 2
    '''
        The example below shows that in action, using a lambda function to intercept the signal from each button and pass through the appropriate window. We can also discard the checked value since we aren't using it.
    '''
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

        
app = QApplication(sys.argv)
w = MainWindow_7()
w.show()
app.exec()