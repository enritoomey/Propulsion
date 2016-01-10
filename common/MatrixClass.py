from PySide.QtCore import *
from PySide.QtGui import *  # importo todas las funciones de pyside


class MatrixDialog(QDialog):
    def __init__(self, ValoresIniciales, parent=None):
        super(MatrixDialog, self).__init__(parent)
        self.setGeometry(QRect(100, 100, 600, 200))
        Matrix = QTableWidget(len(ValoresIniciales[0]), len(ValoresIniciales), self)
        Matrix.setGeometry(QRect(0, 0, 600, 200))
        Matrix.setHorizontalHeaderLabels(['1', '2', '3', '4', '5', '6'])
        Matrix.setVerticalHeaderLabels(['P [Pa]', 'T [K]', 'rho [kg/m3]', 'V [m3/kg]', 'S [J/kgK]'])
        for i in range(len(ValoresIniciales)):
            for j in range(len(ValoresIniciales[i])):
                Matrix.setItem(j, i, QTableWidgetItem(str(ValoresIniciales[i][j])))
