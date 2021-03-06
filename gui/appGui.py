from PyQt5.QtWidgets import QMessageBox as QMB
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import GUI
from lib import gfDatabase as DB
from lib import gfHelper as gfh
from gui.trimGui import TrimDialog as TD




class App(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)  # Laden der UI-Datei

        # # Setze icon
        # root = QtCore.QFileInfo(__file__).absolutePath()
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(root + "/Icons/ico.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        # self.setWindowIcon(icon)

        self.setup_triggers()
        self.data = DB.DataBase()

    def setup_triggers(self):
        # Buttons
        self.but_plot.clicked.connect(self.plot_data)
        self.but_fopen.clicked.connect(self.file_open)
        self.but_fout.clicked.connect(self.file_save)
        self.but_save_data.clicked.connect(self.export_data)
        self.but_trim.clicked.connect(self.show_trim_window)

        # Aktivieren und Deaktivieren
        self.rb_vio.clicked.connect(self.set_visibility)
        self.rb_hist.clicked.connect(self.set_visibility)

        # Aktionen
        self.actionOpen_File.triggered.connect(self.file_open)
        self.actionSave_File.triggered.connect(self.file_save)

    def show_trim_window(self):
        data = self.data.df

        if data is not None:
            self.un_highlight(self.txt_fopen)
            pass
        else:
            self.show_error_box('Es wurden keine Daten angegeben')
            self.highlight_field(self.txt_fopen)
            return

        calc_data = data[['area', 'dia', 'pos-x', 'pos-y', 'edge', 'ASTM']]
        td = TD(calc_data)
        ret_val = td.exec_()
        if ret_val:
            curr_text = td.cb_cols.currentText()
            exclude = td.cb_edgeGrains.isChecked()
            thresh = td.sliderTRIM.value()
            if exclude:
                data = data[(data['edge'] == 0) | (data[curr_text] >= thresh)]
            else:
                data = data[data[curr_text] >= thresh]
            self.data.write_to_df(data)
            self.show_info_box('Daten erfolgreich bereinigt.')
        else:
            return

    def get_short_cols(self, path, col_dict=None):
        if not self.test_path(path):
            return

        head = gfh.get_header(path)
        coldata = gfh.parse_header(head)

        if not col_dict:
            col_dict = self.data.col_dict
        return gfh.get_shortforms_of_columns(coldata[1], col_dict)

    def test_path(self, p=None):
        self.un_highlight(self.txt_fopen)
        if not hasattr(self.data, 'path'):
            pass
        else:
            path = self.data.path
        if not p:
            self.show_error_box('Kein Pfad angegeben!')
            self.highlight_field(self.txt_fopen)
            raise AttributeError
        else:
            return path

    def start_load_data(self):
        pfad = self.txt_fopen.text()
        if pfad == '':
            self.load_data()
        else:
            self.load_data(pfad)

    def load_data(self, path=None, short_cols=None):
        try:
            path = self.test_path(path)
        except AttributeError:
            return

        if not short_cols:
            short_cols = self.get_short_cols(path)

        try:
            data = gfh.read_text(path, cols=short_cols)
        except FileNotFoundError:
            self.show_error_box('Datei nicht gefunden')
        except IndexError:

            return

        self.data.write_to_df(data)

        # additems = [i for i in data.columns if i not in ['pos-x', 'pos-y', 'edge']]
        # self.cb_plotchoice.addItems(additems)
        #
        # combo = self.cb_plotchoice
        # index = combo.findText('area', QtCore.Qt.MatchFixedString)
        # if index >= 0:
        #     combo.setCurrentIndex(index)

        self.show_info_box('Daten erfolgreich geladen')

        return

    def export_data(self):
        print(self.data.df)
        self.un_highlight(self.txt_fout)
        path = self.txt_fout.text()
        if path == '':
            self.show_error_box('Kein Ausgabepfad angegeben')
            self.highlight_field(self.txt_fout)
            return
        if self.data.outpath and self.data.outpath != path:
            answer = self.show_msg_box('Die zuvor ge??ffnete Datei stimmt nicht mit der Eingabezeile ??berein.\nFortfahren?')
            if not answer:
                return
        if self.data.df is not None:
            try:
                gfh.export_to_excel(self.data.df, path)
            except FileNotFoundError:
                self.show_error_box('Datei nicht gefunden')
                return
            self.show_info_box('Daten erfolgreich exportiert.')
        else:
            answer = self.show_msg_box(
                'Es gibt keine Daten zum Exportieren.\nFortfahren?')
            if not answer:
                return



    def plot_data(self):
        data = self.data.df

        if data is not None:
            self.un_highlight(self.txt_fopen)
            pass
        else:
            self.show_error_box('Es wurden keine Daten angegeben')
            self.highlight_field(self.txt_fopen)
            return

        inner_grains = data[data['edge'] == 0]

        current_text = self.cb_plotchoice.currentText()
        calc_data = inner_grains[current_text]

        class_mode = self.get_class_mode()

        if not class_mode:
            return

        classes = gfh.get_number_of_classes(calc_data, mode=class_mode)

        if self.gb_histogram.isEnabled() and self.rb_hist.isChecked():

            gfh.plot_data_hist(calc_data, bins=classes, show_cumulated=self.cb_cumulated.isChecked())

        elif self.gb_violine.isEnabled() and self.rb_vio.isChecked():
            if self.cb_cut_data.isChecked():
                cut = 0
            else:
                cut = 2
            kernel_size = float(self.txt_bw.text())
            gfh.plot_data_violin(data=calc_data, cut=cut, bw=kernel_size)

        else:
            self.show_info_box('Hier fehlte eine Zuordnung zum Plotmodus')

        return

    # Hilffunktionen f??r Buttons und Hervorhebungen

    def un_highlight(self, field):
        field.setStyleSheet('border: 1px solid black')
        self.statusBar().setStyleSheet('color:black; font-weight:normal')

    def highlight_field(self, field):
        field.setStyleSheet('border: 2px solid red;')
        self.statusBar().setStyleSheet('color:red; font-weight:bold')

    def proc_path(self, dest, text):
        dest.setText(text)
        return

    def file_save(self):
        out_file = \
            QtWidgets.QFileDialog.getSaveFileName(self, 'Speicherort w??hlen', '',
                                                  'Excel-Files (*.xlsx);;All Files (*)')[0]
        if not out_file:
            return
        self.proc_path(self.txt_fout, out_file)
        self.data.write_outpath(out_file)
        self.un_highlight(self.txt_fout)

    def file_open(self):
        self.un_highlight(self.txt_fopen)
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'W??hle eine Quelldatei', filter='*.txt')[0]
        # Wenn Nutzer Dateipfadauswahl abbricht
        if not fname:
            return

        try:
            # Wenn neuer Dateipfad = alter Dateipfad --> lade nichts neu
            if fname == self.data.path:
                return
            else:
                # Wenn alte Datei vorhanden, aber Unterschied im Dateinamen
                # L??sche alte Daten
                self.data.clear_data()
                # Lade dann neu
                self.data.write_to_path(fname)
                pass
        # Wenn noch gar keine alten Daten vorhanden --> lade normal die Date
        except AttributeError:
            self.data.write_to_path(fname)
            pass

        self.load_data(fname)

        #  Setze den Pfad in die Felder ein
        self.proc_path(self.txt_fopen, fname)

        self.statusBar().showMessage('Datei erfolgreich geladen', 2000)

    def folder_open(self, dest):
        self.un_highlight(dest)
        path = QtWidgets.QFileDialog.getExistingDirectory(self, 'W??hle einen Quellordner')
        if not path:
            return
        self.proc_path(dest, path)
        self.statusBar().showMessage('Ordner erfolgreich geladen', 2000)
