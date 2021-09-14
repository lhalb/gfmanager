from PyQt5 import QtGui, QtWidgets

import seaborn as sns
from lib.gfHelper import get_number_of_classes
from gui import plotting as pg
from gui import boxes as BOX
from math import ceil


class PlotDialog(QtWidgets.QDialog, pg.Ui_Dialog):
    def __init__(self, data):
        super(PlotDialog, self).__init__()
        self.setupUi(self)
        self.data = data

        # Setze icon
        icon = QtGui.QIcon(":/img/icons/chart.png")
        self.setWindowIcon(icon)

        # Fill Combo-Box
        additems = [i for i in data.columns if i not in ['pos-x', 'pos-y', 'edge']]
        self.cb_plotchoice.addItems(additems)

        # Init Data-Plot
        self.plt_data = self.plotWidget.canvas
        self.data_ax = self.plt_data.fig.add_subplot(111)
        self.plot_data()
        self.setup_triggers()

    def setup_triggers(self):
        self.cb_plotchoice.currentTextChanged.connect(self.plot_data)
        self.tabWidget.currentChanged.connect(self.plot_data)
        self.cb_cumulated.stateChanged.connect(self.plot_data)
        self.cb_classification.currentTextChanged.connect(self.plot_data)
        self.cb_cut_data.stateChanged.connect(self.plot_data)
        self.txt_bw.returnPressed.connect(self.plot_data)
        self.but_replot.clicked.connect(self.plot_data)

    def plot_data(self):
        current_text = self.cb_plotchoice.currentText()
        calc_data = self.data[current_text]

        if self.tabWidget.currentIndex() == 0:
            if current_text != 'ASTM':
                txt = str(self.cb_classification.currentText())
                classes = get_number_of_classes(calc_data, mode=txt)
            else:
                classes = ceil(calc_data.max())

            self.plot_data_hist(calc_data, bins=classes, show_cumulated=self.cb_cumulated.isChecked())

        else:
            if self.cb_cut_data.isChecked():
                cut = 0
            else:
                cut = 2
            kernel_size = float(self.txt_bw.text())
            self.plot_data_violin(data=calc_data, cut=cut, bw=kernel_size)

    def plot_data_hist(self, x, bins=10, show_cumulated=False, title=''):
        self.data_ax.clear()
        bar = sns.histplot(data=x, kde=show_cumulated, ax=self.data_ax, bins=bins)
        bar.set_xlabel(x.name)
        self.plt_data.fig.tight_layout()
        self.plt_data.draw_idle()

    def plot_data_violin(self, data, cut=0, bw=1.0):
        self.data_ax.clear()
        sns.violinplot(x=data, ax=self.data_ax, cut=cut, bw=bw)
        self.plt_data.fig.tight_layout()
        self.plt_data.draw_idle()