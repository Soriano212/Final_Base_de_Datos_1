import sys
from PyQt6 import QtCore, QtWidgets

from capas.interfaz.InicioSesion import Ui_InicioSesion

class VenInicioSesion(QtWidgets.QTabWidget, Ui_InicioSesion):
    def __init__(self, parent = None) -> None:
        super(VenInicioSesion, self).__init__(parent)
        self.setupUi(self)

    def ingresar(self):
        QtCore.QDateTime()

    def registrarse(self):
        pass

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VenInicioSesion()
        myApp.show()
        app.exec()