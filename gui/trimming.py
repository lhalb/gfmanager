# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\trimming.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 744)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.but_openImage = QtWidgets.QPushButton(Dialog)
        self.but_openImage.setObjectName("but_openImage")
        self.horizontalLayout_2.addWidget(self.but_openImage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dataPlot = MplWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataPlot.sizePolicy().hasHeightForWidth())
        self.dataPlot.setSizePolicy(sizePolicy)
        self.dataPlot.setMinimumSize(QtCore.QSize(0, 200))
        self.dataPlot.setObjectName("dataPlot")
        self.gridLayout.addWidget(self.dataPlot, 2, 0, 1, 1)
        self.imagePlot = MplWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePlot.sizePolicy().hasHeightForWidth())
        self.imagePlot.setSizePolicy(sizePolicy)
        self.imagePlot.setMinimumSize(QtCore.QSize(0, 400))
        self.imagePlot.setObjectName("imagePlot")
        self.gridLayout.addWidget(self.imagePlot, 0, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lab_cut = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cut.sizePolicy().hasHeightForWidth())
        self.lab_cut.setSizePolicy(sizePolicy)
        self.lab_cut.setObjectName("lab_cut")
        self.horizontalLayout.addWidget(self.lab_cut)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sliderTRIM = QtWidgets.QSlider(Dialog)
        self.sliderTRIM.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTRIM.setObjectName("sliderTRIM")
        self.verticalLayout.addWidget(self.sliderTRIM)
        self.bBox = QtWidgets.QDialogButtonBox(Dialog)
        self.bBox.setOrientation(QtCore.Qt.Horizontal)
        self.bBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bBox.setObjectName("bBox")
        self.verticalLayout.addWidget(self.bBox)

        self.retranslateUi(Dialog)
        self.bBox.accepted.connect(Dialog.accept)
        self.bBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.but_openImage.setText(_translate("Dialog", "FileOpen"))
        self.label.setText(_translate("Dialog", "Abzuschneidende Klassen:"))
        self.lab_cut.setText(_translate("Dialog", "test"))
from gui.mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
