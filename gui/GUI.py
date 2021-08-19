# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_fopen = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_fopen.setObjectName("txt_fopen")
        self.horizontalLayout.addWidget(self.txt_fopen)
        self.but_fopen = QtWidgets.QToolButton(self.centralwidget)
        self.but_fopen.setObjectName("but_fopen")
        self.horizontalLayout.addWidget(self.but_fopen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cb_plotchoice = QtWidgets.QComboBox(self.centralwidget)
        self.cb_plotchoice.setAutoFillBackground(True)
        self.cb_plotchoice.setPlaceholderText("")
        self.cb_plotchoice.setFrame(True)
        self.cb_plotchoice.setObjectName("cb_plotchoice")
        self.cb_plotchoice.addItem("")
        self.horizontalLayout_5.addWidget(self.cb_plotchoice)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rb_hist = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_hist.setChecked(True)
        self.rb_hist.setObjectName("rb_hist")
        self.verticalLayout_3.addWidget(self.rb_hist)
        self.rb_vio = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_vio.setObjectName("rb_vio")
        self.verticalLayout_3.addWidget(self.rb_vio)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.cb_classification = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_classification.sizePolicy().hasHeightForWidth())
        self.cb_classification.setSizePolicy(sizePolicy)
        self.cb_classification.setMaximumSize(QtCore.QSize(190, 16777215))
        self.cb_classification.setObjectName("cb_classification")
        self.cb_classification.addItem("")
        self.cb_classification.addItem("")
        self.cb_classification.addItem("")
        self.cb_classification.addItem("")
        self.verticalLayout_4.addWidget(self.cb_classification)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gb_histogram = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_histogram.setObjectName("gb_histogram")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_histogram)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_cumulated = QtWidgets.QCheckBox(self.gb_histogram)
        self.cb_cumulated.setObjectName("cb_cumulated")
        self.verticalLayout_2.addWidget(self.cb_cumulated)
        self.verticalLayout_8.addWidget(self.gb_histogram)
        self.gb_violine = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_violine.setEnabled(False)
        self.gb_violine.setObjectName("gb_violine")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_violine)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_outliner = QtWidgets.QCheckBox(self.gb_violine)
        self.cb_outliner.setObjectName("cb_outliner")
        self.verticalLayout_5.addWidget(self.cb_outliner)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cb_quantile = QtWidgets.QCheckBox(self.gb_violine)
        self.cb_quantile.setObjectName("cb_quantile")
        self.horizontalLayout_7.addWidget(self.cb_quantile)
        self.txt_quantile = QtWidgets.QLineEdit(self.gb_violine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_quantile.sizePolicy().hasHeightForWidth())
        self.txt_quantile.setSizePolicy(sizePolicy)
        self.txt_quantile.setMaximumSize(QtCore.QSize(81, 16777215))
        self.txt_quantile.setObjectName("txt_quantile")
        self.horizontalLayout_7.addWidget(self.txt_quantile)
        self.label_4 = QtWidgets.QLabel(self.gb_violine)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addWidget(self.gb_violine)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.but_plot = QtWidgets.QPushButton(self.centralwidget)
        self.but_plot.setObjectName("but_plot")
        self.horizontalLayout_2.addWidget(self.but_plot)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txt_fout = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_fout.setObjectName("txt_fout")
        self.horizontalLayout_3.addWidget(self.txt_fout)
        self.but_fout = QtWidgets.QToolButton(self.centralwidget)
        self.but_fout.setObjectName("but_fout")
        self.horizontalLayout_3.addWidget(self.but_fout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.but_save_data = QtWidgets.QPushButton(self.centralwidget)
        self.but_save_data.setObjectName("but_save_data")
        self.horizontalLayout_4.addWidget(self.but_save_data)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Source:"))
        self.but_fopen.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "Welche Daten?"))
        self.cb_plotchoice.setItemText(0, _translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Art"))
        self.rb_hist.setText(_translate("MainWindow", "Histogramm"))
        self.rb_vio.setText(_translate("MainWindow", "Violin-Plot"))
        self.label_3.setText(_translate("MainWindow", "Klassierung nach"))
        self.cb_classification.setItemText(0, _translate("MainWindow", "Freedman–Diaconis"))
        self.cb_classification.setItemText(1, _translate("MainWindow", "Square-Root"))
        self.cb_classification.setItemText(2, _translate("MainWindow", "Sturges"))
        self.cb_classification.setItemText(3, _translate("MainWindow", "Rice"))
        self.gb_histogram.setTitle(_translate("MainWindow", "Histogramm-Ploteinstellungen"))
        self.cb_cumulated.setText(_translate("MainWindow", "Zeige kumulierte Häufigkeit"))
        self.gb_violine.setTitle(_translate("MainWindow", "Violin-Ploteinstellungen"))
        self.cb_outliner.setText(_translate("MainWindow", "zeige Ausreißer"))
        self.cb_quantile.setText(_translate("MainWindow", "zeige"))
        self.txt_quantile.setText(_translate("MainWindow", "25, 50, 75"))
        self.label_4.setText(_translate("MainWindow", "Quantile"))
        self.but_plot.setText(_translate("MainWindow", "PLOT"))
        self.label_2.setText(_translate("MainWindow", "Dest:"))
        self.but_fout.setText(_translate("MainWindow", "..."))
        self.but_save_data.setText(_translate("MainWindow", "Write to XLS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionSave_File.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
