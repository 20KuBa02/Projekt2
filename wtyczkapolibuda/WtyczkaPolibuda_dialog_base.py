# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WtyczkaPolibuda_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WtyczkaNaZajeciahDialogBase(object):
    def setupUi(self, WtyczkaNaZajeciahDialogBase):
        WtyczkaNaZajeciahDialogBase.setObjectName("WtyczkaNaZajeciahDialogBase")
        WtyczkaNaZajeciahDialogBase.resize(716, 620)
        self.button_box = QtWidgets.QDialogButtonBox(WtyczkaNaZajeciahDialogBase)
        self.button_box.setGeometry(QtCore.QRect(70, 570, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.Przycisk1 = QtWidgets.QPushButton(WtyczkaNaZajeciahDialogBase)
        self.Przycisk1.setGeometry(QtCore.QRect(60, 30, 93, 28))
        self.Przycisk1.setObjectName("Przycisk1")
        self.label = QtWidgets.QLabel(WtyczkaNaZajeciahDialogBase)
        self.label.setGeometry(QtCore.QRect(60, 175, 141, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.mMapLayerComboBox = QgsMapLayerComboBox(WtyczkaNaZajeciahDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(140, 220, 160, 27))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label_2 = QtWidgets.QLabel(WtyczkaNaZajeciahDialogBase)
        self.label_2.setGeometry(QtCore.QRect(100, 305, 291, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Przycisk2 = QtWidgets.QPushButton(WtyczkaNaZajeciahDialogBase)
        self.Przycisk2.setGeometry(QtCore.QRect(160, 30, 161, 28))
        self.Przycisk2.setObjectName("Przycisk2")
        self.textEdit = QtWidgets.QTextEdit(WtyczkaNaZajeciahDialogBase)
        self.textEdit.setGeometry(QtCore.QRect(40, 300, 441, 251))
        self.textEdit.setObjectName("textEdit")
        self.Przycisk3 = QtWidgets.QPushButton(WtyczkaNaZajeciahDialogBase)
        self.Przycisk3.setGeometry(QtCore.QRect(330, 30, 131, 28))
        self.Przycisk3.setObjectName("Przycisk3")
        self.Przycisk4 = QtWidgets.QPushButton(WtyczkaNaZajeciahDialogBase)
        self.Przycisk4.setGeometry(QtCore.QRect(470, 30, 93, 28))
        self.Przycisk4.setObjectName("Przycisk4")

        self.retranslateUi(WtyczkaNaZajeciahDialogBase)
        self.button_box.accepted.connect(WtyczkaNaZajeciahDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(WtyczkaNaZajeciahDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WtyczkaNaZajeciahDialogBase)

    def retranslateUi(self, WtyczkaNaZajeciahDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaNaZajeciahDialogBase.setWindowTitle(_translate("WtyczkaNaZajeciahDialogBase", "moja wtyczka"))
        self.Przycisk1.setText(_translate("WtyczkaNaZajeciahDialogBase", "policz"))
        self.Przycisk2.setText(_translate("WtyczkaNaZajeciahDialogBase", "współrzędne punktów"))
        self.Przycisk3.setText(_translate("WtyczkaNaZajeciahDialogBase", "różnica wyskości"))
        self.Przycisk4.setText(_translate("WtyczkaNaZajeciahDialogBase", "pole"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WtyczkaNaZajeciahDialogBase = QtWidgets.QDialog()
    ui = Ui_WtyczkaNaZajeciahDialogBase()
    ui.setupUi(WtyczkaNaZajeciahDialogBase)
    WtyczkaNaZajeciahDialogBase.show()
    sys.exit(app.exec_())
