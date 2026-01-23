# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RGBWidgetpMLtiu.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(528, 370)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_1)

        self.spinBox_1 = QSpinBox(Form)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setMaximum(255)

        self.verticalLayout_2.addWidget(self.spinBox_1)

        self.verticalSlider_1 = QSlider(Form)
        self.verticalSlider_1.setObjectName(u"verticalSlider_1")
        self.verticalSlider_1.setMaximum(255)
        self.verticalSlider_1.setValue(0)
        self.verticalSlider_1.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider_1, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(Form)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(255)

        self.verticalLayout_3.addWidget(self.spinBox_2)

        self.verticalSlider_2 = QSlider(Form)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setValue(0)
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(Form)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(255)

        self.verticalLayout_4.addWidget(self.spinBox_3)

        self.verticalSlider_3 = QSlider(Form)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setValue(0)
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSlider_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)
        self.verticalSlider_1.valueChanged.connect(self.spinBox_1.setValue)
        self.spinBox_1.valueChanged.connect(self.verticalSlider_1.setValue)
        self.verticalSlider_2.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.verticalSlider_2.setValue)
        self.verticalSlider_3.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged.connect(self.verticalSlider_3.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"RED", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"GREEN", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"BLUE", None))
    # retranslateUi

