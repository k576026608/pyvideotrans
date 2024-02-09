# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from videotrans.configure import config

class Ui_geminiform(object):
    def setupUi(self, geminiform):
        geminiform.setObjectName("geminiform")
        geminiform.setWindowModality(QtCore.Qt.NonModal)
        geminiform.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(geminiform.sizePolicy().hasHeightForWidth())
        geminiform.setSizePolicy(sizePolicy)
        geminiform.setMaximumSize(QtCore.QSize(600, 400))
        self.gemini_template = QtWidgets.QPlainTextEdit(geminiform)
        self.gemini_template.setGeometry(QtCore.QRect(10, 180, 571, 151))
        self.gemini_template.setObjectName("gemini_template")
        self.gemini_template.setReadOnly(True)
        self.gemini_template.setDisabled(True)
        self.label_4 = QtWidgets.QLabel(geminiform)
        self.label_4.setGeometry(QtCore.QRect(10, 155, 571, 21))
        # font = QtGui.QFont()
        # font.setFamily("黑体")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.set_gemini = QtWidgets.QPushButton(geminiform)
        self.set_gemini.setGeometry(QtCore.QRect(10, 350, 93, 35))
        self.set_gemini.setMinimumSize(QtCore.QSize(0, 35))
        self.set_gemini.setObjectName("set_gemini")
        self.gemini_key = QtWidgets.QLineEdit(geminiform)
        self.gemini_key.setGeometry(QtCore.QRect(150, 60, 431, 35))
        self.gemini_key.setMinimumSize(QtCore.QSize(0, 35))
        self.gemini_key.setObjectName("gemini_key")
        self.label_2 = QtWidgets.QLabel(geminiform)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(geminiform)
        QtCore.QMetaObject.connectSlotsByName(geminiform)

    def retranslateUi(self, geminiform):
        geminiform.setWindowTitle( "Gemini Pro")
        self.gemini_template.setPlaceholderText( "prompt")
        self.label_4.setText( "{lang}代表目标语言名称，不要删除。可在 videotrans/gemini.txt中修改提示语" if config.defaulelang =='zh' else  "{lang} represents the target language name, do not delete it. You can modify the prompt language in videotrans/gemini.txt")
        self.set_gemini.setText('保存' if config.defaulelang=='zh' else "Save")
        self.gemini_key.setPlaceholderText("secret key")
        self.label_2.setText( "Gemini  Key ")
