import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
	QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
)

class MainWindow(QMainWindow): # A quick demo
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Widgets App")
        
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        
        for w in widgets:
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
  
class MainWindow_1(QMainWindow): # QLabel
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        widget = QLabel("Hello")
        widget.setText("Hello World!")
        
        font = widget.font()
        font.setPointSize(30)
        
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        """
        For horizontal alignment 
            Flag	Behavior
            Qt.AlignLeft	Aligns with the left edge.
            Qt.AlignRight	Aligns with the right edge.
            Qt.AlignHCenter	Centers horizontally in the available space.
            Qt.AlignJustify	Justifies the text in the available space.
        For vertical alignment
            Qt.AlignTop	Aligns with the top.
            Qt.AlignBottom	Aligns with the bottom.
            Qt.AlignVCenter	Centers vertically in the available space.
            
            Qt.AlignCenter	Centers horizontally and vertically
        You can combine flags together using pipes (|), however note that you can only use vertical or horizontal alignment flag at a time.
            align_top_left = Qt.AlignLeft | Qt.AlignTop
        """
        #widget.setPixmap(QPixmap('1.jpg'))
        #widget.setScaledContents(False)
        self.setCentralWidget(widget)

class MainWindow_2(QMainWindow): # QCheckBox
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        widget = QCheckBox()
        widget.setCheckState(Qt.PartiallyChecked)
        
        widget.stateChanged.connect(self.show_state)
        # checked = 2, unchecked = 0, and partially checked = 1
        self.setCentralWidget(widget)
        
    def show_state(self,s):
        print(f"checked:{s == Qt.Checked}")
        print(f"Unchecked:{s == Qt.Unchecked}")
        print(f"PartiallyChecked:{s == Qt.PartiallyChecked}")
        print(s)

class MainWindow_3(QMainWindow): # QComboBox
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        widget = QComboBox()
        widget.addItems(["one","Two","Three"])
        
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        widget.setEditable(True)
        widget.setMaxCount(10)
        self.setCentralWidget(widget)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        """
            Flag	        Behavior
            QComboBox.NoInsert	No insert
            QComboBox.InsertAtTop	Insert as first item
            QComboBox.InsertAtCurrent	Replace currently selected item
            QComboBox.InsertAtBottom	Insert after last item
            QComboBox.InsertAfterCurrent	Insert after current item
            QComboBox.InsertBeforeCurrent	Insert before current item
            QComboBox.InsertAlphabetically	Insert in alphabetical order
        """
        
    def index_changed(self,i): # i is an int
        print(i)
    def text_changed(self,s): #s is a str
        print(s)

class MainWindow_4(QMainWindow): # QListWidget
    def __init__(self):
        super(MainWindow_4, self).__init__()
        self.setWindowTitle("My App")
        
        widget = QListWidget()
        widget.addItems(["one","Two","Three"])
        
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)
        
    def index_changed(self,i): # Not an index, i is a QListItem
        print(i.text())
    def text_changed(self,s): # s is a str
        print(s)
        
class MainWindow_5(QMainWindow): # QLineEdit
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")
        
       #widget.setReadOnly(True) # uncomment this to make readonly
        
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        widget.setInputMask('000.000.000.000;_')
        
        self.setCentralWidget(widget)
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")
        
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
        
    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

class MainWindow_6(QMainWindow): # QSpinBox and QDoubleSpinBox
    def __init__(self):
        super().__init__()
        self. setWindowTitle("My App")
        
        widget = QSpinBox()   # integers
        # Or: widget = QDoubleSpinBox() # floats
        
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
        
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)
        
        self.setCentralWidget(widget)
        
    def value_changed(self,i):
        print(i)
        
    def value_changed_str(self,s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow_6()
window.show()

app.exec()