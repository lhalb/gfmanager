from PyQt5.QtWidgets import QMessageBox as QMB
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import GUI
from lib import gfDatabase as DB
from lib import gfHelper as gfh


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
        self.but_plot.clicked.connect(self.plot_data)

    def get_text(self):
        p = 'data/Grain_File_200x.txt'

        col_dict = {
            'Integer identifying grain': 'n',
            'Average orientation (phi1, PHI, phi2) in degrees': 'ori-d',
            'Average orientation (phi1, PHI, phi2) in radians': 'ori-r',
            'Average Position (x, y) in microns': 'pos',
            'Average Image Quality (IQ)': 'iq',
            'Average Confidence Index (CI)': 'ci',
            'An integer identifying the phase': 'phase',
            'Edge grain (1) or interior grain (0)': 'edge',
            'Number of measurement points in the grain': 'points',
            'Area of grain in square microns': 'area',
            'Diameter of grain in microns': 'dia',
            'ASTM grain size': 'ASTM',
            'Aspect ratio of ellipse fit to grain': 'aspect',
            'Length of major axis of ellipse fit to grain in microns': 'majEll',
            'Length of minor axis of ellipse fit to grain in microns': 'minEll',
            'Grain ellipticity': 'ellipt',
            'Grain circularity': 'circul',
            'Maximmum Feret diameter': 'maxFeret',
            'Minimum Feret diameter': 'minFeret'
        }

        head = gfh.get_header(p)

        coldata = gfh.parse_header(head)

        short_cols = gfh.get_shortforms_of_columns(coldata[1], col_dict)

        print(short_cols)

        data = gfh.read_text(p, cols=short_cols)


        self.data.write_to_df(data)

        print(self.data.df)

        outpath = 'data/output.xlsx'

        gfh.export_to_excel(self.data.df, outpath)


    def plot_data(self):
        self.show_info_box('Das hat funktioniert')
        return

    # Hilffunktionen für Buttons und Hervorhebungen

    def un_highlight(self, field):
        field.setStyleSheet('border: 1px solid black')
        self.statusBar().setStyleSheet('color:black; font-weight:normal')

    def highlight_field(self, field):
        field.setStyleSheet('border: 2px solid red;')
        self.statusBar().setStyleSheet('color:red; font-weight:bold')

    def file_save(self):
        out_file = \
            QtWidgets.QFileDialog.getSaveFileName(self, 'Speicherort wählen', '',
                                                  'Excel-Files (*.xlsx);;All Files (*)')[0]
        if not out_file:
            return
        self.proc_path(self.txt_output_file, out_file)

    def file_open(self):
        self.un_highlight(self.txt_input_file)
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Wähle eine Quelldatei', filter='*.txt')[0]
        # Wenn Nutzer Dateipfadauswahl abbricht
        if not fname:
            return

        try:
            # Wenn neuer Dateipfad = alter Dateipfad --> lade nichts neu
            if fname == self.fname:
                return
            else:
                # Wenn alte Datei vorhanden, aber Unterschied im Dateinamen
                # Lösche alte Daten
                self.clear_df()
                # Lade dann neu
                self.fname = fname
                pass
        # Wenn noch gar keine alten Daten vorhanden --> lade normal die Date
        except AttributeError:
            self.fname = fname
            pass

        #  Setze den Pfad in die Felder ein
        self.proc_path(self.txt_input_file, self.fname)
        # Ziehe die Frequenz oder die Geschwindigkeit aus den Daten
        self.get_frequency(self.fname)
        self.df = self.load_data()
        self.statusBar().showMessage('Datei erfolgreich geladen', 2000)

    def folder_open(self, dest):
        self.un_highlight(dest)
        path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Wähle einen Quellordner')
        if not path:
            return
        self.proc_path(dest, path)
        self.statusBar().showMessage('Ordner erfolgreich geladen', 2000)

    def show_msg_box(self, text='Dies ist eine Warnung.'):
        msg = QMB()
        msg.setWindowTitle("Warnung")
        msg.setText(text)
        msg.setIcon(QMB.Warning)
        msg.setStandardButtons(QMB.Cancel | QMB.Ok)
        msg.setDefaultButton(QMB.Ok)

        returnvalue = msg.exec()
        if returnvalue == QMB.Ok:
            press = True
        else:
            press = False

        return press

    def show_error_box(self, text='Fehler'):
        msg = QMB()
        msg.setWindowTitle("Hinweis")
        msg.setText(text)
        msg.setIcon(QMB.Critical)
        msg.setStandardButtons(QMB.Ok)
        msg.setDefaultButton(QMB.Ok)

        msg.exec()

    def show_info_box(self, text='Info'):
        msg = QMB()
        msg.setWindowTitle("Information")
        msg.setText(text)
        msg.setIcon(QMB.Information)
        msg.setStandardButtons(QMB.Ok)
        msg.setDefaultButton(QMB.Ok)

        msg.exec()
