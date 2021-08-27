# # Imports
# from PyQt5 import QtWidgets
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
# import matplotlib

# # Ensure using PyQt5 backend
# matplotlib.use('QT5Agg')

# # Matplotlib canvas class to create figure
# class MplCanvas(Canvas):
#     def __init__(self):
#         self.fig = Figure()
#         self.ax = self.fig.add_subplot(111)
#         Canvas.__init__(self, self.fig)
#         Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         Canvas.updateGeometry(self)

# # Matplotlib widget
# class MplWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
#         self.canvas = MplCanvas()                  # Create canvas object
#         self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
#         self.vbl.addWidget(self.canvas)
#         self.setLayout(self.vbl)


import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure


class MplCanvas(Canvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.canvas = MplCanvas()
        # self.canvas.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        # self.canvas.figure.clf()
