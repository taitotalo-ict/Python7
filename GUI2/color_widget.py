from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
)

from PySide6.QtGui import QPalette, QColor


class ColorWidget(QWidget):
    def __init__(self, color: str):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

        # self.show()


app = QApplication()
window = QWidget()
layout = QHBoxLayout(window)
column1 = QVBoxLayout()
column2 = QVBoxLayout()
column3 = QVBoxLayout()

column1.addWidget(ColorWidget('red'))
column1.addWidget(ColorWidget('green'))
column1.addWidget(ColorWidget('blue'))

column2.addWidget(ColorWidget('yellow'))

column3.addWidget(ColorWidget('brown'))
column3.addWidget(ColorWidget('purple'))

layout.addLayout(column1)
layout.addLayout(column2)
layout.addLayout(column3)

# layout.addWidget(ColorWidget('red'))
# layout.addWidget(ColorWidget('green'))
window.show()
window.setMinimumSize(100,100)
app.exec()