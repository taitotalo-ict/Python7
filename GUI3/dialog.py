from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton('Press me')
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        result = QMessageBox.warning(self, 'title', 'Hello', buttons=QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Ok:
            print('Ok')
        elif result == QMessageBox.StandardButton.Cancel:
            print('Cancel')
        # print(repr(result))

        # dialog.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard)
        # dialog.exec()

app = QApplication()
window = MainWindow()
window.show()
app.exec()