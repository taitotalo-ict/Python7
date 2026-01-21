from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QComboBox,
    QLabel,
    QVBoxLayout,
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # COLORS = ['red', 'yellow', 'green', 'blue']
        COLORS = QColor.colorNames()
        start_color = COLORS[0]

        # Label
        label = QLabel(start_color)
        # label.setAutoFillBackground(True)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = label
        self.set_label_color(start_color)

        # ComboBox
        combo = QComboBox()
        combo.addItems(COLORS)
        combo.setCurrentText(start_color)
        combo.currentTextChanged.connect(self.set_label_color)
        combo.currentTextChanged.connect(label.setText)
        font = combo.font()
        font.setPointSize(20)
        combo.setFont(font)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(combo)

        # Central Widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()
    
    def set_label_color(self, color:str):
        # palette = self.label.palette()
        # palette.setColor(QPalette.ColorRole.Window, QColor(color))
        # self.label.setPalette(palette)
        self.setStyleSheet(f'QLabel {{ background-color: {color}; border-radius: 15px; }}')


app = QApplication()
window = MainWindow()
app.exec()