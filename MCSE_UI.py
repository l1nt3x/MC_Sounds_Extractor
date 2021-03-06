# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MCSE.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MCSE(object):
    def setupUi(self, MCSE):
        MCSE.setObjectName("MCSE")
        MCSE.resize(1060, 180)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        MCSE.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MCSE)
        self.centralwidget.setObjectName("centralwidget")
        self.mcse_label = QtWidgets.QLabel(self.centralwidget)
        self.mcse_label.setGeometry(QtCore.QRect(10, 10, 240, 20))
        self.mcse_label.setObjectName("mcse_label")
        self.mc_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.mc_dir_label.setGeometry(QtCore.QRect(10, 40, 180, 30))
        self.mc_dir_label.setObjectName("mc_dir_label")
        self.mc_dir_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mc_dir_lineEdit.setGeometry(QtCore.QRect(190, 40, 530, 30))
        self.mc_dir_lineEdit.setObjectName("mc_dir_lineEdit")
        self.mc_dir_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mc_dir_pushButton.setGeometry(QtCore.QRect(730, 40, 120, 30))
        self.mc_dir_pushButton.setObjectName("mc_dir_pushButton")
        self.out_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.out_dir_label.setGeometry(QtCore.QRect(10, 80, 180, 30))
        self.out_dir_label.setObjectName("out_dir_label")
        self.out_dir_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.out_dir_lineEdit.setGeometry(QtCore.QRect(190, 80, 530, 30))
        self.out_dir_lineEdit.setObjectName("out_dir_lineEdit")
        self.out_dir_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.out_dir_pushButton.setGeometry(QtCore.QRect(730, 80, 120, 30))
        self.out_dir_pushButton.setObjectName("out_dir_pushButton")
        self.extract_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.extract_pushButton.setGeometry(QtCore.QRect(730, 120, 120, 30))
        self.extract_pushButton.setObjectName("extract_pushButton")
        self.ver_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ver_comboBox.setGeometry(QtCore.QRect(939, 40, 130, 30))
        self.ver_comboBox.setObjectName("ver_comboBox")
        self.ver_label = QtWidgets.QLabel(self.centralwidget)
        self.ver_label.setGeometry(QtCore.QRect(860, 40, 70, 30))
        self.ver_label.setObjectName("ver_label")
        MCSE.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MCSE)
        self.statusBar.setObjectName("statusBar")
        MCSE.setStatusBar(self.statusBar)

        self.retranslateUi(MCSE)
        QtCore.QMetaObject.connectSlotsByName(MCSE)

    def retranslateUi(self, MCSE):
        _translate = QtCore.QCoreApplication.translate
        MCSE.setWindowTitle(_translate("MCSE", "Minecraft Sounds Extractor"))
        self.mcse_label.setText(_translate("MCSE", "Minecraft Sounds Extractor"))
        self.mc_dir_label.setText(_translate("MCSE", "Minecraft directory:"))
        self.mc_dir_pushButton.setText(_translate("MCSE", "Browse"))
        self.out_dir_label.setText(_translate("MCSE", "Output directory"))
        self.out_dir_pushButton.setText(_translate("MCSE", "Browse"))
        self.extract_pushButton.setText(_translate("MCSE", "Extract"))
        self.ver_label.setText(_translate("MCSE", "Version:"))
