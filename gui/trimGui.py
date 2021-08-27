from PyQt5 import QtWidgets


import matplotlib.pyplot as plt

from gui import trimming as tri


class TrimDialog(QtWidgets.QDialog, tri.Ui_Dialog):
    def __init__(self):
        super(TrimDialog, self).__init__()

        self.setupUi(self)