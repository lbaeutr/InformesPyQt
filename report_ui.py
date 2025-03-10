# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 746)
        MainWindow.setMinimumSize(QSize(702, 746))
        MainWindow.setMaximumSize(QSize(702, 746))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #2c3e50; /* Azul oscuro elegante */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3498db; /* Azul claro */\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1f6690;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 40, 311, 301))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"Logo.png"))
        self.label.setScaledContents(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 350, 291, 351))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.informe = QPushButton(self.widget)
        self.informe.setObjectName(u"informe")

        self.verticalLayout.addWidget(self.informe)

        self.informe2 = QPushButton(self.widget)
        self.informe2.setObjectName(u"informe2")

        self.verticalLayout.addWidget(self.informe2)

        self.informe3 = QPushButton(self.widget)
        self.informe3.setObjectName(u"informe3")

        self.verticalLayout.addWidget(self.informe3)

        self.informe4 = QPushButton(self.widget)
        self.informe4.setObjectName(u"informe4")

        self.verticalLayout.addWidget(self.informe4)

        self.informe5 = QPushButton(self.widget)
        self.informe5.setObjectName(u"informe5")

        self.verticalLayout.addWidget(self.informe5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.informe.raise_()
        self.informe2.raise_()
        self.informe3.raise_()
        self.informe4.raise_()
        self.informe5.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.informe.setText(QCoreApplication.translate("MainWindow", u"Informe 1", None))
        self.informe2.setText(QCoreApplication.translate("MainWindow", u"Informe 2", None))
        self.informe3.setText(QCoreApplication.translate("MainWindow", u"Informe 3", None))
        self.informe4.setText(QCoreApplication.translate("MainWindow", u"Informe 4", None))
        self.informe5.setText(QCoreApplication.translate("MainWindow", u"Informe  5", None))
    # retranslateUi

