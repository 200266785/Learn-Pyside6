import sys
from random import choice
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QMenu, \
    QPushButton


class MainWindow_1(QMainWindow): # Signals and Receiving data
    def __init__(self):
        super().__init__()
        self.button_is_checked = True

        self.setWindowTitle("My app")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked")
    def the_button_was_toggled(self,checked):
        print("Checked?",checked)

class MainWindow_2(QMainWindow): # Storing data
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)

        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

class MainWindow_3(QMainWindow): # Changing the interface
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        self.setWindowTitle("My Oneshot App")


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]
class MainWindow_4(QMainWindow): # QMainWindow's signals example
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self,window_title):
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

class MainWindow_5(QMainWindow): # Connecting widgets together directly
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        #MainWindow->container->layout->widget(input and label)

class MainWindow_6(QMainWindow): # Events, Mouse events
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
    """
    [Event handler]	[Event type moved]
    mouseMoveEvent	Mouse moved
    mousePressEvent	Mouse button pressed
    mouseReleaseEvent	Mouse button released
    mouseDoubleClickEvent	Double click detected

     [Method]	   [Returns]
    .button()	Specific button that triggered this event
    .buttons()	State of all mouse buttons (OR'ed flags)
    .globalPos()	Application-global position as a QPoint
    .globalX()	Application-global horizontal X position
    .globalY()	Application-global vertical Y position
    .pos()	Widget-relative position as a QPoint integer
    .posF()	Widget-relative position as a QPointF float
    """
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

class MainWindow_7(QMainWindow): # Context menus (event based)
    def __init__(self):
        super().__init__()
    def contextMenuEvent(self,e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

class MainWindow_8(QMainWindow): # Context menus (singal based)
    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        context.exec(self.mapToGlobal(pos))

class CustomButton(QPushButton): # Layout forwarding
    def mousePressEvent(self,e):
        e.accept()  # mark an event as handled

    def event(sel,e):
        e.ignore()  # mark it as unhandled, will continue to bubble up the hierarchy

app = QApplication(sys.argv)
window = MainWindow_8()
window.show()
app.exec()