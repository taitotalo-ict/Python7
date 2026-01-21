from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QLabel,
    QVBoxLayout,
)

app = QApplication()

window = QWidget()
label = QLabel('')
# font = label.font()
# font.setPointSize(30)
# label.setFont(font)
line_edit = QLineEdit(placeholderText='Kirjoita jotain tähän')
# font = line_edit.font()
# font.setPointSize(30)
# line_edit.setFont(font)
line_edit.textEdited.connect(label.setText)
layout = QVBoxLayout(window)
layout.addWidget(label)
layout.addWidget(line_edit)

window.show()
app.exec()