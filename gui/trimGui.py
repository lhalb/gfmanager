from PyQt5 import QtWidgets


import seaborn as sns

from gui import trimming as tri
import matplotlib.image as mpimg
from math import floor, ceil
import numpy as np


class TrimDialog(QtWidgets.QDialog, tri.Ui_Dialog):
    def __init__(self, data=None):
        super(TrimDialog, self).__init__()
        self.setupUi(self)

        self.trim_data = data
        self.cal_val = None

        # Fill Combo-Box
        additems = [i for i in data.columns if i not in ['pos-x', 'pos-y', 'edge']]
        self.cb_cols.addItems(additems)

        # Init Data-Plot
        self.plt_data = self.dataPlot.canvas
        self.data_ax = self.plt_data.fig.add_subplot(111)
        self.init_slider()

        self.update_violin()

        self.vline = self.data_ax.axvline(data[self.cb_cols.currentText()].min(), color='r')

        # Init Image-Plot
        self.imagePlot.hide()
        self.plt_image = self.imagePlot.canvas
        self.image_ax = self.plt_image.fig.add_subplot(111)
        self.scat, = self.image_ax.plot([], [], marker='o', ms=5, ls='', color='r')

        # trigger am Ende laden
        self.setup_triggers()

    def setup_triggers(self):
        self.sliderTRIM.valueChanged.connect(self.update_data)
        self.but_openImage.clicked.connect(self.load_image)
        self.cb_cols.currentTextChanged.connect(self.update_element)
        self.cb_edgeGrains.clicked.connect(self.update_element)
        self.txt_kalwert.returnPressed.connect(self.update_cal_val)

    def update_element(self):
        self.update_violin()
        self.init_vline()
        self.init_slider()
        self.update_scatter_data()

    def update_violin(self):
        self.data_ax.clear()
        curr_text = self.cb_cols.currentText()
        if self.cb_edgeGrains.isChecked():
            corr_data = self.trim_data[self.trim_data['edge'] == 0]
        else:
            corr_data = self.trim_data
        data = corr_data[curr_text]

        sns.violinplot(x=data, ax=self.data_ax, cut=0)

        self.plt_data.fig.tight_layout()
        self.plt_data.draw_idle()

    def init_vline(self):
        curr_text = self.cb_cols.currentText()
        min_val = self.trim_data[curr_text].min()
        self.vline = self.data_ax.axvline(min_val, color='r')
        self.plt_data.draw_idle()


    def init_slider(self):
        sli = self.sliderTRIM

        curr_text = self.cb_cols.currentText()
        if self.cb_edgeGrains.isChecked():
            data = self.trim_data[self.trim_data['edge'] == 0]
        else:
            data = self.trim_data
        min_val = floor(data[curr_text].min())
        max_val = ceil(data[curr_text].max())

        sli.setMinimum(min_val)
        sli.setMaximum(max_val)

        sli.setValue(min_val)

        self.lab_cut.setText(str(min_val))

    def update_vline(self):
        act_val = self.sliderTRIM.value()
        self.vline.set_xdata(act_val)
        self.plt_data.draw_idle()

        self.lab_cut.setText(str(act_val))

    def load_image(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Bilddatei laden',
                                                      filter='Bilddateien (*.png *.jpeg *.jpg *.bmp)')[0]
        # Wenn Nutzer Dateipfadauswahl abbricht
        if not fname:
            return

        img = mpimg.imread(fname)
        y_max = img.shape[0]
        x_max = img.shape[1]

        x_cal = self.trim_data['pos-x'].max()/x_max
        y_cal = self.trim_data['pos-y'].max() / y_max

        self.cal_val = max(x_cal, y_cal)
        self.txt_kalwert.setText(str(self.cal_val))
        self.image_ax.imshow(img, origin='upper', extent=None)
        self.plt_image.draw_idle()
        self.plt_image.fig.tight_layout()
        self.show_image_widget()

    def update_cal_val(self):
        self.cal_val = float(self.txt_kalwert.text())

    def show_image_widget(self):
        self.imagePlot.show()

    def get_excluded_values(self):
        data = self.trim_data

        thresh = self.sliderTRIM.value()
        curr_text = self.cb_cols.currentText()

        if self.cb_edgeGrains.isChecked():
            cut_data = data.loc[(data['edge'] == 1) | (data[curr_text] <= thresh)]
        else:
            cut_data = data.loc[data[curr_text] <= thresh]

        x_data = cut_data['pos-x'].values / self.cal_val
        y_data = cut_data['pos-y'].values / self.cal_val

        return x_data, y_data

    def update_scatter_data(self):
        x, y = self.get_excluded_values()
        self.scat.set_xdata(x)
        self.scat.set_ydata(y)
        self.plt_image.draw_idle()

    def update_data(self):
        self.update_vline()
        self.update_scatter_data()


