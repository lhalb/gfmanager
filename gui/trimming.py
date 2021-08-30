# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/trimming.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 680)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.but_openImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_openImage.setObjectName("but_openImage")
        self.horizontalLayout_2.addWidget(self.but_openImage)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cb_edgeGrains = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cb_edgeGrains.setObjectName("cb_edgeGrains")
        self.horizontalLayout_2.addWidget(self.cb_edgeGrains)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txt_kalwert = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_kalwert.setMinimumSize(QtCore.QSize(40, 0))
        self.txt_kalwert.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.txt_kalwert.setFont(font)
        self.txt_kalwert.setObjectName("txt_kalwert")
        self.horizontalLayout_2.addWidget(self.txt_kalwert)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.imagePlot = MplWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePlot.sizePolicy().hasHeightForWidth())
        self.imagePlot.setSizePolicy(sizePolicy)
        self.imagePlot.setMinimumSize(QtCore.QSize(0, 200))
        self.imagePlot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imagePlot.setObjectName("imagePlot")
        self.verticalLayout.addWidget(self.imagePlot)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cb_cols = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cb_cols.setObjectName("cb_cols")
        self.horizontalLayout_3.addWidget(self.cb_cols)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dataPlot = MplWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataPlot.sizePolicy().hasHeightForWidth())
        self.dataPlot.setSizePolicy(sizePolicy)
        self.dataPlot.setMinimumSize(QtCore.QSize(0, 200))
        self.dataPlot.setObjectName("dataPlot")
        self.verticalLayout_2.addWidget(self.dataPlot)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lab_cut = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cut.sizePolicy().hasHeightForWidth())
        self.lab_cut.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lab_cut.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lab_cut.setFont(font)
        self.lab_cut.setObjectName("lab_cut")
        self.horizontalLayout.addWidget(self.lab_cut)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.sliderTRIM = QtWidgets.QSlider(Dialog)
        self.sliderTRIM.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTRIM.setObjectName("sliderTRIM")
        self.verticalLayout_3.addWidget(self.sliderTRIM)
        self.bBox = QtWidgets.QDialogButtonBox(Dialog)
        self.bBox.setOrientation(QtCore.Qt.Horizontal)
        self.bBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bBox.setObjectName("bBox")
        self.verticalLayout_3.addWidget(self.bBox)

        self.retranslateUi(Dialog)
        self.bBox.accepted.connect(Dialog.accept)
        self.bBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.but_openImage.setText(_translate("Dialog", "FileOpen"))
        self.cb_edgeGrains.setText(_translate("Dialog", "Exclude Edge Grains"))
        self.label_2.setText(_translate("Dialog", "Kalibrierwert:"))
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