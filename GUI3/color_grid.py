from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout,
    QMainWindow,
    QPushButton,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor


class ColorCard(QPushButton):
    color_clicked = Signal(object)
    
    def __init__(self, color: str):
        super().__init__()
        self.setText(color)
        self.color = color
        self.setupUi()

    def setupUi(self):
        # Background color
        # Font
        self.setStyleSheet(f'background-color: {self.color}; font-size: 30px;')
        # self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clicked.connect(lambda: self.color_clicked.emit(self))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.COLORS_PER_ROW = 2
        self.setupUi()
    
    def setupUi(self):
        layout = QGridLayout()
        for index, color in enumerate(QColor.colorNames()):
            row = index // self.COLORS_PER_ROW
            column = index % self.COLORS_PER_ROW
            widget = ColorCard(color)
            widget.color_clicked.connect(lambda widget: print(widget.color))
            layout.addWidget(widget, row, column)
        
        widget = QWidget()
        widget.setLayout(layout)

        scrollArea = QScrollArea()
        scrollArea.setWidget(widget)
        
        self.setCentralWidget(scrollArea)
        
        self.resize(widget.width()+16,600)

app = QApplication()
window = MainWindow()
window.show()
app.exec()