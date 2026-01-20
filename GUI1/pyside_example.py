from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QCheckBox, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Minun ikkuna')

        button = QPushButton('Paina mua')

        self.setCentralWidget(button)
        self.show()

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