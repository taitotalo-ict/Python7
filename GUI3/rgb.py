from ui_RGBWidget import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget

class RGBWidget(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateColor()
        self.spinBox_1.valueChanged.connect(self.updateColor)
        self.spinBox_2.valueChanged.connect(self.updateColor)
        self.spinBox_3.valueChanged.connect(self.updateColor)

    def updateColor(self):
        r = self.verticalSlider_1.value()
        g = self.verticalSlider_2.value()
        b = self.verticalSlider_3.value()
        self.widget.setStyleSheet(f'background-color: rgb({r},{g},{b});')


app = QApplication()
window = RGBWidget()
window.show()
app.exec()