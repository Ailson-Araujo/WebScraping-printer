# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Biblioteca\Documentos\MEGAsync\Projetos\Impressora\GUI_UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 383)
        MainWindow.setStyleSheet("QFrame{\n"
"    background-color: #2a2c37;\n"
"    border: 2px solid #22212c;\n"
"    border-radius: 11px;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #787878;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"\n"
"#btn_config{\n"
"    background-image: url(:/icon/image/cil-settings.png);\n"
"}\n"
"\n"
"#btn_close{\n"
"    background-image: url(:/icon/image/cil-x.png);\n"
"}\n"
"\n"
"#frame_move{\n"
"    border: none;\n"
"    border-top: 6px solid #22212c;\n"
"}\n"
"\n"
"#frame_dev {\n"
"    background-color: #151320;\n"
"    border: none;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"#frame_container{\n"
"    border: none;\n"
"}\n"
"\n"
"#label_device_uno,  #label_device_dois {\n"
"    color: #9580ff;\n"
"    font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"#frame_device_uno, #frame_device_dois{\n"
"    border: 1px solid  #22212c;\n"
"}\n"
"\n"
"#label_value_print, #label_value_copy, #label_value_total,\n"
"#label_value_print_dois, #label_value_copy_dois, #label_value_total_dois{\n"
"    color: #8aff80;\n"
"    font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"#label_print, #label_copy, #label_total,\n"
"#label_print_dois, #label_copy_dois, #label_total_dois{\n"
"    color: #ff80bf;\n"
"    font: 700 11pt \"Segoe UI\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout_2.setContentsMargins(0, 1, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_container = QtWidgets.QFrame(self.frame_main)
        self.frame_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_container.setObjectName("frame_container")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_container)
        self.gridLayout_5.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_close = QtWidgets.QPushButton(self.frame_container)
        self.btn_close.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_5.addWidget(self.btn_close, 0, 4, 1, 1)
        self.frame_device_dois = QtWidgets.QFrame(self.frame_container)
        self.frame_device_dois.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_device_dois.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_device_dois.setObjectName("frame_device_dois")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_device_dois)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_value_copy_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_value_copy_dois.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_copy_dois.setObjectName("label_value_copy_dois")
        self.gridLayout_4.addWidget(self.label_value_copy_dois, 3, 3, 1, 1)
        self.label_value_total_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_value_total_dois.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_total_dois.setObjectName("label_value_total_dois")
        self.gridLayout_4.addWidget(self.label_value_total_dois, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.label_device_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_device_dois.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device_dois.setObjectName("label_device_dois")
        self.gridLayout_4.addWidget(self.label_device_dois, 0, 0, 1, 5)
        self.label_print_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_print_dois.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_print_dois.setObjectName("label_print_dois")
        self.gridLayout_4.addWidget(self.label_print_dois, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 4, 1, 1)
        self.label_total_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_total_dois.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_total_dois.setObjectName("label_total_dois")
        self.gridLayout_4.addWidget(self.label_total_dois, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 2, 1, 1)
        self.label_copy_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_copy_dois.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_copy_dois.setObjectName("label_copy_dois")
        self.gridLayout_4.addWidget(self.label_copy_dois, 3, 1, 1, 1)
        self.label_value_print_dois = QtWidgets.QLabel(self.frame_device_dois)
        self.label_value_print_dois.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_print_dois.setObjectName("label_value_print_dois")
        self.gridLayout_4.addWidget(self.label_value_print_dois, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 5, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_device_dois, 2, 0, 1, 5)
        self.frame_move = QtWidgets.QFrame(self.frame_container)
        self.frame_move.setMinimumSize(QtCore.QSize(30, 0))
        self.frame_move.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_move.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame_move.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_move.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_move.setObjectName("frame_move")
        self.gridLayout_5.addWidget(self.frame_move, 0, 2, 1, 1)
        self.btn_config = QtWidgets.QPushButton(self.frame_container)
        self.btn_config.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_config.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_config.setText("")
        self.btn_config.setObjectName("btn_config")
        self.gridLayout_5.addWidget(self.btn_config, 0, 0, 1, 1)
        self.frame_device_uno = QtWidgets.QFrame(self.frame_container)
        self.frame_device_uno.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_device_uno.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_device_uno.setObjectName("frame_device_uno")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_device_uno)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_copy = QtWidgets.QLabel(self.frame_device_uno)
        self.label_copy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_copy.setObjectName("label_copy")
        self.gridLayout_3.addWidget(self.label_copy, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 3, 2, 1, 1)
        self.label_total = QtWidgets.QLabel(self.frame_device_uno)
        self.label_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_total.setObjectName("label_total")
        self.gridLayout_3.addWidget(self.label_total, 5, 1, 1, 1)
        self.label_print = QtWidgets.QLabel(self.frame_device_uno)
        self.label_print.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_print.setObjectName("label_print")
        self.gridLayout_3.addWidget(self.label_print, 3, 1, 1, 1)
        self.label_device_uno = QtWidgets.QLabel(self.frame_device_uno)
        self.label_device_uno.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device_uno.setObjectName("label_device_uno")
        self.gridLayout_3.addWidget(self.label_device_uno, 0, 0, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 3, 4, 1, 1)
        self.label_value_print = QtWidgets.QLabel(self.frame_device_uno)
        self.label_value_print.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_print.setObjectName("label_value_print")
        self.gridLayout_3.addWidget(self.label_value_print, 3, 3, 1, 1)
        self.label_value_copy = QtWidgets.QLabel(self.frame_device_uno)
        self.label_value_copy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_copy.setObjectName("label_value_copy")
        self.gridLayout_3.addWidget(self.label_value_copy, 4, 3, 1, 1)
        self.label_value_total = QtWidgets.QLabel(self.frame_device_uno)
        self.label_value_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_value_total.setObjectName("label_value_total")
        self.gridLayout_3.addWidget(self.label_value_total, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_device_uno, 1, 0, 1, 5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem11, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.frame_container, 1, 0, 1, 1)
        self.frame_dev = QtWidgets.QFrame(self.frame_main)
        self.frame_dev.setMinimumSize(QtCore.QSize(0, 26))
        self.frame_dev.setMaximumSize(QtCore.QSize(16777215, 26))
        self.frame_dev.setStyleSheet("")
        self.frame_dev.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dev.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dev.setObjectName("frame_dev")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_dev)
        self.gridLayout_6.setContentsMargins(-1, 1, -1, 1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_dev = QtWidgets.QLabel(self.frame_dev)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_dev.setFont(font)
        self.label_dev.setStyleSheet("")
        self.label_dev.setObjectName("label_dev")
        self.gridLayout_6.addWidget(self.label_dev, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 0, 1, 1, 1)
        self.label_version = QtWidgets.QLabel(self.frame_dev)
        self.label_version.setObjectName("label_version")
        self.gridLayout_6.addWidget(self.label_version, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_dev, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contador de Impressão"))
        self.label_value_copy_dois.setText(_translate("MainWindow", "456465"))
        self.label_value_total_dois.setText(_translate("MainWindow", "456546"))
        self.label_device_dois.setText(_translate("MainWindow", "IMPRESSORA DOIS"))
        self.label_print_dois.setText(_translate("MainWindow", "Impressões"))
        self.label_total_dois.setText(_translate("MainWindow", "Total"))
        self.label_copy_dois.setText(_translate("MainWindow", "Cópias"))
        self.label_value_print_dois.setText(_translate("MainWindow", "156465465"))
        self.label_copy.setText(_translate("MainWindow", "Cópias"))
        self.label_total.setText(_translate("MainWindow", "Total"))
        self.label_print.setText(_translate("MainWindow", "Impressões"))
        self.label_device_uno.setText(_translate("MainWindow", "IMPRESSORA UNO"))
        self.label_value_print.setText(_translate("MainWindow", "156465465"))
        self.label_value_copy.setText(_translate("MainWindow", "456465"))
        self.label_value_total.setText(_translate("MainWindow", "456546"))
        self.label_dev.setText(_translate("MainWindow", "By: Ailson Araujo"))
        self.label_version.setText(_translate("MainWindow", "Version: 1.0"))
import Gui.resource_rc