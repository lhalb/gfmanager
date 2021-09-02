from PyQt5 import QtCore, QtGui, QtWidgets

from gui import save as sv
from gui import boxes as BOX


class SaveDialog(QtWidgets.QDialog, sv.Ui_Dialog):
    def __init__(self, data, class_mode=''):
        super(SaveDialog, self).__init__()
        self.setupUi(self)
        self.data = data
        self.create_cols()

        self.setup_triggers()

    def setup_triggers(self):
        self.but_fout.clicked.connect(self.export_data)
        self.but_select_all.clicked.connect(lambda: self.select_items(True))
        self.but_select_none.clicked.connect(lambda: self.select_items(False))

    def create_cols(self):
        for col in self.data.columns:
            item = QtWidgets.QListWidgetItem()
            item.setText(col)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidget.addItem(item)

    def select_items(self, all=False):
        if all:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        for index in range(self.listWidget.count()):
            self.listWidget.item(index).setCheckState(state)

    def export_data(self):
        checked_items = []
        for index in range(self.listWidget.count()):
            if self.listWidget.item(index).checkState() == QtCore.Qt.Checked:
                checked_items.append(self.listWidget.item(index).text())

        if not checked_items:
            BOX.show_error_box('Keine Spalten zum Export ausgewählt.')


