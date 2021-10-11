import sys
from PySide6.QtCore import Qt
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
  
class MainWindow_1(QMainWindow): # 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")







  
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()