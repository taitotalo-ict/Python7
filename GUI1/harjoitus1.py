from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titles = ['Text1', 'Text2', 'Text3']
        self.index = 0
        self.setup_ui()

    def setup_ui(self):
        button = QPushButton('Press me')
        button.clicked.connect(self.change_title)
        self.setCentralWidget(button)


        self.show()

    def change_title(self):
        self.index = (self.index + 1) % len(self.titles)
        self.setWindowTitle(self.titles[self.index])
        print('Button has been clicked')


app = QApplication()
window = CustomWindow()
app.exec()