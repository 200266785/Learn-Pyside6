import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog,QVBoxLayout,QLabel,QDialogButtonBox,QMessageBox

class MainWindow(QMainWindow): # add a QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        button.setCheckable(True)
        self.setCentralWidget(button)
        
    def button_clicked(self,s):
        print("click",s)
        
        dlg = QDialog(self)
        dlg.setWindowTitle("Hello!")
        dlg.exec()
        
class CustomDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hello!")
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        '''
            QDialogButtonBox.Ok
            QDialogButtonBox.Open
            QDialogButtonBox.Save
            QDialogButtonBox.Cancel
            QDialogButtonBox.Close
            QDialogButtonBox.Discard
            QDialogButtonBox.Apply
            QDialogButtonBox.Reset
            QDialogButtonBox.RestoreDefaults
            QDialogButtonBox.Help
            QDialogButtonBox.SaveAll
            QDialogButtonBox.Yes
            QDialogButtonBox.YesToAll
            QDialogButtonBox.No
            QDialogButtonBox.Abort
            QDialogButtonBox.Retry
            QDialogButtonBox.Ignore
            QDialogButtonBox.NoButton
        '''
        
        self.buttonbox = QDialogButtonBox(QBtn)
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel("Something happened,is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonbox)
        self.setLayout(self.layout)
        
class MainWindow_2(QMainWindow): # use CustomDialog to add a QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        button.setCheckable(True)
        self.setCentralWidget(button)
        
    def button_clicked(self,s):
        print("click",s)
        
        dlg = CustomDialog(parent=self) # == CustomDialog(self)
        # dlg = CustomDialog()  the dialog be in center of the window
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

class MainWindow_3(QMainWindow): # QMessageBox
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self,s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        #dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #dlg.setIcon(QMessageBox.Question)
        
        button = dlg.exec()
        
        if button == QMessageBox.Ok:
            print("OK")
        elif button == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")
    '''
        QMessageBox.Ok
        QMessageBox.Open
        QMessageBox.Save
        QMessageBox.Cancel
        QMessageBox.Close
        QMessageBox.Discard
        QMessageBox.Apply
        QMessageBox.Reset
        QMessageBox.RestoreDefaults
        QMessageBox.Help
        QMessageBox.SaveAll
        QMessageBox.Yes
        QMessageBox.YesToAll
        QMessageBox.No
        QMessageBox.NoToAll
        QMessageBox.Abort
        QMessageBox.Retry
        QMessageBox.Ignore
        QMessageBox.NoButton
        
        Icon state	Description
        QMessageBox.NoIcon	    The message box does not have an icon.
        QMessageBox.Question	The message is asking a question.
        QMessageBox.Information	The message is informational only.
        QMessageBox.Warning	    The message is warning.
        QMessageBox.Critical	The message indicates a critical problem.

    '''
    
class MainWindow_4(QMainWindow): # Built in QMessageBox dialogs
    ''' methods:
        QMessageBox.about(parent, title, message)
        QMessageBox.critical(parent, title, message)
        QMessageBox.information(parent, title, message)
        QMessageBox.question(parent, title, message)
        QMessageBox.warning(parent, title, message)
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked_2)
        self.setCentralWidget(button)
        
    def button_clicked(self,s):
    
        button = QMessageBox.question(self,"Question dialog","The longer message")
        
        if button == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")
            
    def button_clicked_2(self,s): # change default button
        button = QMessageBox.critical(
            self,
            "Opps",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )
        
        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


app = QApplication(sys.argv)

window = MainWindow_4()
window.show()

app.exec()