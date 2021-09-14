from PyQt5 import QtGui, QtWidgets


import seaborn as sns

from gui import trimming as tri
from gui import boxes as BOX
import matplotlib.image as mpimg
from math import floor, ceil


class TrimDialog(QtWidgets.QDialog, tri.Ui_Dialog):
    def __init__(self, data=None):
        super(TrimDialog, self).__init__()
        self.setupUi(self)

        # Setze icon
        icon = QtGui.QIcon(":/img/icons/trim.png")
        self.setWindowIcon(icon)

        self.trim_data = data
        self.cal_val = 1

        # Fill Combo-Box
        additems = [i for i in data.columns if i not in ['pos-x', 'pos-y', 'edge']]
        self.cb_cols.addItems(additems)

        # Init Data-Plot
        self.plt_data = self.dataPlot.canvas
        self.data_ax = self.plt_data.fig.add_subplot(111)
        self.init_slider()

        self.update_violin()

        self.vline = self.data_ax.axvline(data[self.cb_cols.currentText()].min(), color='r')
        self.vline_max = self.data_ax.axvline(ceil(data[self.cb_cols.currentText()].max()), color='b')

        # Init Image-Plot
        self.imagePlot.hide()
        self.plt_image = self.imagePlot.canvas
        self.image_ax = self.plt_image.fig.add_subplot(111)
        self.scat, = self.image_ax.plot([], [], marker='o', ms=5, ls='', color='r')

        # trigger am Ende laden
        self.setup_triggers()

    def setup_triggers(self):
        self.sliderTRIM_min.valueChanged.connect(self.update_data)
        self.sliderTRIM_max.valueChanged.connect(self.update_data)
        self.but_openImage.clicked.connect(self.load_image)
        self.cb_cols.currentTextChanged.connect(self.update_element)
        self.cb_edgeGrains.clicked.connect(self.update_element)
        self.txt_kalwert.returnPressed.connect(self.update_cal_val)
        self.lab_cut_min.editingFinished.connect(self.set_min_slider)
        self.lab_cut_max.editingFinished.connect(self.set_max_slider)
        self.but_cut_min.clicked.connect(self.manipulate_max)
        self.but_cut_max.clicked.connect(self.manipulate_min)

    def update_element(self):
        self.update_violin()
        self.init_vline()
        bool_max = self.but_cut_min.isChecked()
        bool_min = self.but_cut_max.isChecked()
        self.init_slider(h_max=bool_max, h_min=bool_min)
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
        max_val = self.trim_data[curr_text].max()
        self.vline = self.data_ax.axvline(min_val, color='r')
        self.vline_max = self.data_ax.axvline(max_val, color='b')
        self.plt_data.draw_idle()

    def init_slider(self, h_min=False, h_max=False):
        sli_min = self.sliderTRIM_min
        sli_max = self.sliderTRIM_max

        curr_text = self.cb_cols.currentText()
        if self.cb_edgeGrains.isChecked():
            data = self.trim_data[self.trim_data['edge'] == 0]
        else:
            data = self.trim_data
        min_val = floor(data[curr_text].min())

        max_val = ceil(data[curr_text].max())
        # Wenn die Mitte am Beginn der Daten liegen soll (nur Max-Slider aktiv)
        if h_min and not h_max:
            half_min = min_val
        # Wenn die Mitte am Ende der Daten liegen soll (nur Min-Slider aktiv)
        elif h_max and not h_min:
            half_min = max_val
        else:
            half_min = floor((max_val-min_val)/2)

        half_max = half_min + 1

        sli_min.setMinimum(min_val)
        sli_min.setMaximum(half_min)

        if half_min != min_val and half_max != max_val:
            if half_min > 10:
                ticks = 10
            else:
                ticks = half_min - min_val
            sli_min.setTickInterval(int((half_min-min_val)/ticks))
            sli_max.setTickInterval(int((max_val-half_min)/ticks))

        sli_max.setMinimum(half_max)
        sli_max.setMaximum(max_val)

        sli_min.setValue(min_val)
        sli_max.setValue(max_val)

        self.lab_cut_min.setText(str(min_val))
        self.lab_cut_max.setText(str(max_val))

    def update_vline_max(self):
        act_val = self.sliderTRIM_max.value()
        self.vline_max.set_xdata(act_val)
        self.plt_data.draw_idle()

        self.lab_cut_max.setText(str(act_val))

    def update_vline(self):
        act_val = self.sliderTRIM_min.value()
        self.vline.set_xdata(act_val)
        self.plt_data.draw_idle()

        self.lab_cut_min.setText(str(act_val))

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

        thresh_1 = self.sliderTRIM_min.value()
        thresh_2 = self.sliderTRIM_max.value()
        curr_text = self.cb_cols.currentText()

        cond_1 = (data['edge'] == 1)
        cond_2 = (data[curr_text] <= thresh_1) | (data[curr_text] >= thresh_2)

        if self.cb_edgeGrains.isChecked():
            cut_data = data.loc[cond_1 | cond_2]
        else:
            cut_data = data.loc[cond_2]

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
        self.update_vline_max()
        self.update_scatter_data()

    def set_min_slider(self):
        try:
            val = int(self.lab_cut_min.text())
        except ValueError:
            BOX.show_error_box('Falscher Wert eingegeben.')
            return
        self.sliderTRIM_min.setValue(val)
        self.update_data()

    def set_max_slider(self):
        try:
            val = int(self.lab_cut_max.text())
        except ValueError:
            BOX.show_error_box('Falscher Wert eingegeben.')
            return
        self.sliderTRIM_max.setValue(val)
        self.update_data()

    def manipulate_max(self):
        if self.but_cut_min.isChecked():
            self.sliderTRIM_max.hide()
            self.lab_cut_max.hide()
            self.but_cut_max.hide()
            self.init_slider(h_max=True)
        else:
            self.sliderTRIM_max.show()
            self.lab_cut_max.show()
            self.but_cut_min.show()
            self.init_slider()

    def manipulate_min(self):
        if self.but_cut_max.isChecked():
            self.sliderTRIM_min.hide()
            self.lab_cut_min.hide()
            self.but_cut_min.hide()
            self.init_slider(h_min=True)
        else:
            self.sliderTRIM_min.show()
            self.lab_cut_min.show()
            self.but_cut_min.show()
            self.init_slider()
