from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QFormLayout, QLineEdit

app = QApplication()
window = QWidget()
window.show()

# layout = QVBoxLayout(window)
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('Yksi'))
# layout.addWidget(QPushButton('Kaksi'))
# layout.addWidget(QPushButton('Kolme'))
# layout = QGridLayout()
# layout.addWidget(QPushButton('Yksi'), 0, 0)
# layout.addWidget(QPushButton('Kaksi'), 0, 1)
# layout.addWidget(QPushButton('Kolme'), 1, 1)

main_layout = QHBoxLayout()

left_layout = QVBoxLayout()
left_layout.addWidget(QPushButton('Yksi'))
left_layout.addWidget(QPushButton('Kaksi'))

right_layout = QVBoxLayout()
right_layout.addWidget(QLineEdit())

main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)

layout = QFormLayout()
layout.addRow('Nimi:', QLineEdit())
layout.addRow('Sähköposti', QLineEdit())

main_layout.addLayout(layout)

window.setLayout(main_layout)

app.exec()