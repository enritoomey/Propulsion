import sys

from PySide.QtCore import *
from PySide.QtGui import *  # importo todas las funciones de pyside

import CiclosApp_Layout
from Ciclo_JouleBrayton_App import JouleBraytonDialog
from Ciclo_Sabathe_App import SabatheDialog

__appName__ = 'Ciclos App'


class CiclosAppDialog(QDialog, CiclosApp_Layout.Ui_Dialog):
    def __init__(self, parent=None):
        super(CiclosAppDialog, self).__init__(parent)
        self.setWindowTitle(__appName__)
        self.setupUi(self)

        self.connect(self.SabatheButton, SIGNAL("clicked()"), self.displaySabathe)
        self.connect(self.JouleBraytonButton, SIGNAL("clicked()"), self.displayJouleBrayton)

    def displaySabathe(self):
        sabathe = SabatheDialog(self)
        sabathe.exec_()

    def displayJouleBrayton(self):
        sabathe = JouleBraytonDialog(self)
        sabathe.exec_()


app = QApplication(sys.argv)
form = CiclosAppDialog()
form.show()
app.exec_()
