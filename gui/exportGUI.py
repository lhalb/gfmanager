import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from gui import save as sv
from gui import boxes as BOX

from lib import gfHelper as gfh


class SaveDialog(QtWidgets.QDialog, sv.Ui_Dialog):
    def __init__(self, data, col_dict=None):
        super(SaveDialog, self).__init__()
        self.setupUi(self)
        self.data = data
        self.col_dict = col_dict
        self.create_cols()
        self.setup_triggers()

    def setup_triggers(self):
        self.but_fout.clicked.connect(self.export_data)
        self.but_select_all.clicked.connect(lambda: self.select_items(True))
        self.but_select_none.clicked.connect(lambda: self.select_items(False))

    def create_cols(self):
        cols = list(self.data.columns)
        cols.sort()
        for i, col in enumerate(cols):
            item = QtWidgets.QListWidgetItem()
            item.setText(col)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidget.addItem(item)
            try:
                long_version = list(self.col_dict.keys())[list(self.col_dict.values()).index(col)]
            except ValueError:
                long_version = ''
            self.listWidget.item(i).setToolTip(long_version)

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
        else:
            out_file = \
                QtWidgets.QFileDialog.getSaveFileName(self, 'Speicherort wählen', '',
                                                      'Excel-Files (*.xlsx);;All Files (*)')[0]
            if not out_file:
                return
            # Setze Daten auf ausgewählte Spalten
            data = self.data[checked_items]

            # Exportiere Daten in Excel
            gfh.export_to_excel(data, out_file)

            # Falls Quantile exportiert werden sollen
            if self.gb_quantile.isChecked():
                try:
                    quantiles = [int(j.strip()) for j in self.txt_quantiles.text().split(',')]
                    q_data = {k: np.percentile(self.data[k], quantiles) for k in self.data[checked_items].columns}
                    qf = pd.DataFrame(data=q_data, index=quantiles)
                    gfh.export_to_excel(qf, out_file, mode='a', sheet='statistics')
                except ValueError:
                    BOX.show_error_box('Fehlerhafte Quantile angegeben.')
                    return

            if self.gb_class.isChecked():
                # exportiere klassierte Daten
                txt = str(self.cb_classification.currentText())

                datas = {}
                for col in data.columns:
                    cls = gfh.get_number_of_classes(data[col], txt)
                    if cls == 0:
                        continue
                    else:
                        val = pd.cut(data[col], cls, retbins=True, include_lowest=True)

                        name_counts = val[0].name + '_counts'
                        name_bins = name_counts + '_bins'

                        bins = val[1]
                        counts = val[0].value_counts().values

                        datas[name_bins] = bins
                        datas[name_counts] = counts

                bd = pd.DataFrame({key: pd.Series(value) for key, value in datas.items()})

                gfh.export_to_excel(bd, out_file, mode='a', sheet='classes')

            BOX.show_info_box('Daten erfolgreich exportiert.')
