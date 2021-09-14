from PyQt5 import QtGui, QtWidgets
from gui import mingui as GUI
from lib import gfDatabase as DB
from lib import gfHelper as gfh
from gui.trimGui import TrimDialog as TD
from gui.plotUI import PlotDialog as PD
from gui.exportGUI import SaveDialog as SD
from gui import boxes as BOX


class App(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)  # Laden der UI-Datei

        self.setup_triggers()
        self.data = DB.DataBase()
        self.class_option = ''

    def setup_triggers(self):
        # Buttons
        self.but_plot.clicked.connect(self.open_plot_dialog)
        self.but_fopen.clicked.connect(self.file_open)
        self.but_save_data.clicked.connect(self.open_export_dialog)
        self.but_trim.clicked.connect(self.open_trim_dialog)
        self.but_delete_data.clicked.connect(self.delete_data)
        self.info_load.clicked.connect(self.get_data_info)
        
    def open_trim_dialog(self):
        all_data = self.get_data()
        pd = all_data[['area', 'dia', 'pos-x', 'pos-y', 'edge', 'ASTM']]
        td = TD(pd)
        ret_val = td.exec_()
        if ret_val:
            curr_text = td.cb_cols.currentText()
            exclude = td.cb_edgeGrains.isChecked()
            thresh_1 = td.sliderTRIM_min.value()
            thresh_2 = td.sliderTRIM_max.value()

            cond_1 = (all_data['edge'] == 0)
            cond_2 = (all_data[curr_text] >= thresh_1) & (all_data[curr_text] <= thresh_2)

            if exclude:
                data = all_data[cond_1 & cond_2]
            else:
                data = all_data[cond_2]
            self.data.write_to_df(data)
            BOX.show_info_box('Daten erfolgreich bereinigt.')
        else:
            return

    def get_data(self):
        data = self.data.df

        if data is not None:
            pass
        else:
            BOX.show_error_box('Es wurden keine Daten angegeben')
            return

        return data

    def open_plot_dialog(self):
        all_data = self.get_data()
        plot_data = all_data[['area', 'dia', 'pos-x', 'pos-y', 'edge', 'ASTM']]
        if len(plot_data) < 2:
            BOX.show_error_box('Der Datensatz enthält zu wenig Datenpunkte.\nPlotten nicht möglich.')
            return
        pd = PD(plot_data)
        ret_val = pd.exec_()
        if ret_val:
            self.class_option = pd.cb_classification.currentText()
        else:
            return

    def file_open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Wähle eine Quelldatei', filter='*.txt')[0]
        # Wenn Nutzer Dateipfadauswahl abbricht
        if not fname:
            return

        try:
            # Wenn neuer Dateipfad = alter Dateipfad --> lade nichts neu
            if fname == self.data.path:
                return
            else:
                # Wenn alte Datei vorhanden, aber Unterschied im Dateinamen
                # Lösche alte Daten
                self.data.clear_data()
                # Lade dann neu
                self.data.write_to_path(fname)
                pass
        # Wenn noch gar keine alten Daten vorhanden --> lade normal die Date
        except AttributeError:
            self.data.write_to_path(fname)
            pass

        self.load_data(fname)

    def load_data(self, path=None, short_cols=None):
        try:
            path = self.test_path(path)
        except AttributeError:
            return

        if not short_cols:
            short_cols = self.get_short_cols(path)
            if not short_cols:
                return

        try:
            data = gfh.read_text(path, cols=short_cols)
        except FileNotFoundError:
            BOX.show_error_box('Datei nicht gefunden')
            return
        except IndexError:
            BOX.show_error_box('Es gab einen Indexfehler.\nDaten prüfen.')
            return
        except AttributeError:
            BOX.show_error_box('Es gab einen Attributsfehler.\nDaten prüfen.')
            return

        self.data.write_to_df(data)

        BOX.show_info_box('Daten erfolgreich geladen')
        self.check_data()
        self.but_delete_data.setEnabled(True)
        self.but_plot.setEnabled(True)
        self.but_trim.setEnabled(True)
        self.but_save_data.setEnabled(True)
        return

    def delete_data(self):
        self.data.clear_data()
        self.but_delete_data.setEnabled(False)
        self.but_plot.setEnabled(False)
        self.but_trim.setEnabled(False)
        self.but_save_data.setEnabled(False)
        self.check_data()
        BOX.show_info_box('Alle Daten entfernt.')

    def check_data(self):
        on_icon = QtGui.QIcon(":/img/icons/green_light.png")
        off_icon = QtGui.QIcon(":/img/icons/red_light.png")
        if self.data.df is not None:
            ico = on_icon
        else:
            ico = off_icon

        self.info_load.setIcon(ico)

    def get_data_info(self):
        if self.data.df is not None:
            p = self.data.path
            BOX.show_info_box(f'Datei\n{p}\n  geladen')
        else:
            BOX.show_info_box('Keine Daten geladen')

    def test_path(self, p=None):
        if not hasattr(self.data, 'path'):
            pass
        else:
            path = self.data.path
        if not p:
            BOX.show_error_box('Kein Pfad angegeben!')
            raise AttributeError
        else:
            return path
    
    def get_short_cols(self, path, col_dict=None):
        if not self.test_path(path):
            return False
        try:
            head = gfh.get_header(path)
            coldata = gfh.parse_header(head)
        except ValueError as VE:
            err_code = VE.args[0]
            BOX.show_error_box(f'Es gab einen Zuordnungsfehler.\nDer Zeileninhalt lautet:\n{err_code}\nImport abgebrochen.')
            return False

        if not col_dict:
            col_dict = self.data.col_dict
        return gfh.get_shortforms_of_columns(coldata[1], col_dict)

    def open_export_dialog(self):
        data = self.get_data()
        col_dict = self.data.col_dict
        sd = SD(data, col_dict)
        sd.exec_()

