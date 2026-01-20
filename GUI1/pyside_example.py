from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QLabel,
    QLineEdit,
    QCheckBox,
    QComboBox,
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Minun ikkuna')

        self.button = QPushButton('Paina mua')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.log_click)
        self.button.clicked.connect(self.log_click2)
        self.count = 0

        self.line_edit = QLineEdit('Title')
        self.line_edit.textChanged.connect(self.setWindowTitle)

        label = QLabel('Hello world')
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(label)
        self.show()

    def log_click(self, is_checked):
        print(f'Button clicked ({is_checked})')
        self.button.setText(f'Paina mua ({is_checked})')

    def log_click2(self):
        self.count += 1
        print(f'Button has been click {self.count} times')
        

app = QApplication()

# window = QWidget()
# window = QPushButton('Paina mua')
# window = QMainWindow()
# label = QLabel('Hello world')
# button = QPushButton('Paina mua')
# line_edit = QLineEdit('Nimi')
# checkbox = QCheckBox('Option 1')
# combo_box = QComboBox()
# combo_box.addItems(['Item 1', 'Item 2', 'Item 3'])

# window.setCentralWidget(combo_box)
window = MainWindow()
# window.show()

app.exec()      # Event loop