# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 20:47:21 2014

@author: Enriquito
"""
import matplotlib
from PySide.QtCore import *
from PySide.QtGui import *

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'
# Hay que agregarle la siguiente linea para que matplotlib use pyside. De esta forma los objetos FigureCanvas y Figure
# compatibles con los Qwidget creados por Pyside! Ademas, hay que agregarla antes de importar FigureCanvasQTAgg

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from excepciones import NumeroNegativoError, MayorAUnoError, TemperaturaIncompatibleError, Var2IncompatibleError
import SABATHE.layout_CicloSabathe as CicloSabatheGUI
import common.PoderCalorifico as PoderCalorifico
import SABATHE.ciclo_sabathe_calculos as ciclo_sabathe
import common.GUI_atmosfera_estandar as GUI_atmosfera_estandar
from common.MatrixClass import MatrixDialog

__appName__ = 'Ciclo Sabathe'


class SabatheDialog(QDialog, CicloSabatheGUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(SabatheDialog, self).__init__(parent)
        self.setWindowTitle(__appName__)
        self.setupUi(self)
        self.Q = []
        self.formulas = {"AvGas": {'c': 7, 'h': 16, 'o': 0, 's': 0.00},
                         "Diesel": {'c': 12, 'h': 21, 'o': 0, 's': 0.00}}
        # Utilizo las 'keys' de self.formulas para cargar los items en la combobox
        for key in self.formulas.keys():
            self.formula_comboBox.addItem(key)

        # Generamos dos figuras, cada una luego asociada a un canvas, que a su vez tiene como padre una de las pestañas
        # self.tab -> contiene la pestaña titulada "Diagrama P-S"
        # self.tab_2 -> contiene la pestaña titulada "Diagrama T-S"
        self.fig1 = Figure(figsize=(4.8, 3.4), dpi=72, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.axes1 = self.fig1.add_subplot(111)
        self.axes1.set_ylabel('p')
        self.axes1.set_xlabel('v')
        self.axes1.set_title('Ciclo Sabathe')
        self.fig2 = Figure(figsize=(4.8, 3.4), dpi=72, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.axes2 = self.fig2.add_subplot(111)
        self.axes2.set_ylabel('T')
        self.axes2.set_xlabel('S')
        self.axes2.set_title('Ciclo Sabathe')
        # generate the canvas to display the plot
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas1.setParent(self.tab)
        self.canvas1.show()
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas2.setParent(self.tab_2)
        self.canvas2.show()
        self.gamma_aire = 1.4
        self.R_aire = 287
        self.actualizarFormula()

        # Cambio los lineInput de HVS y HVI a "ReadOnly"
        self.HVS_lineEdit.setReadOnly(True)
        self.HVI_lineEdit.setReadOnly(True)

        # Seleccion de una formula en formula_comboBox
        self.connect(self.formula_comboBox, SIGNAL("currentIndexChanged(int)"), self.selecionFormula)

        # Acciones de actualización de la formula quimica para el calculo de Q
        self.connect(self.formulaC, SIGNAL("textEdited(const QString&)"), self.actualizarFormula)
        self.connect(self.formulaH, SIGNAL("textEdited(const QString&)"), self.actualizarFormula)
        self.connect(self.formulaO, SIGNAL("textEdited(const QString&)"), self.actualizarFormula)
        self.connect(self.formulaS, SIGNAL("textEdited(const QString&)"), self.actualizarFormula)
        self.connect(self.relacionMezcla, SIGNAL("valueChanged(double)"), self.actualizarFormula)
        self.connect(self.calcular, SIGNAL("clicked()"), self.Calculos)
        # Boton para mostrar matriz de resultados
        self.connect(self.matrixButton, SIGNAL("clicked()"), self.displayMatrix)
        # Boton para seleccionar P1 y T1 a partir de la altura:
        self.connect(self.Altura_Button, SIGNAL("clicked()"), self.seleccionAltura)

        self.atmosfera_estandar_dialog = AtmosferaEstandarDialog()

    def selecionFormula(self):
        formula = self.formula_comboBox.currentText()
        if formula != 'Otra':
            self.formulaC.setText(str(self.formulas[formula]['c']))
            self.formulaH.setText(str(self.formulas[formula]['h']))
            self.formulaO.setText(str(self.formulas[formula]['o']))
            self.formulaS.setText(str(self.formulas[formula]['s']))
            self.actualizarFormula()

    def actualizarFormula(self):
        c = self.lecturadatos(self.formulaC, 'int')
        h = self.lecturadatos(self.formulaH, 'int')
        o = self.lecturadatos(self.formulaO, 'int')
        s = self.lecturadatos(self.formulaS, 'float')
        # si la formula ingresada coincide con alguna formula del comboBox
        # poner el comboBox en esa formula.
        indexName = 'Otra'
        for key in self.formulas.keys():
            if (self.formulas[key]['c'] == c) & (self.formulas[key]['h'] == h) & (self.formulas[key]['o'] == o):
                indexName = key
        index = self.formula_comboBox.findText(indexName)
        self.formula_comboBox.setCurrentIndex(index)

        Fr = self.relacionMezcla.value()
        HVS, HVI, self.Q, self.lambda_s = PoderCalorifico.PoderCalorifico(c, h, o, s, Fr)
        self.HVS_lineEdit.setText('{:.1f}'.format(HVS))
        self.HVI_lineEdit.setText('{:.1f}'.format(HVS))
        self.calorQ.setText('{:.1f}'.format(self.Q))

    def seleccionAltura(self):
        p1 = str(self.presion1.text())
        t1 = str(self.temperatura1.text())
        dialogo = GUI_atmosfera_estandar.MainDialog(p1,t1)
        if dialogo.exec_():
            self.presion1.setText('{:.1f}'.format(dialogo.atmosfera['p']))
            self.temperatura1.setText('{:.1f}'.format(dialogo.atmosfera['t']))

# Genero ahora la función que va a realizar los calculos, es decir,
    # que va a llamar la función del ciclo. A esta le agrego una subclase de
    # Exception para capturar los valores de entrada negativos.
    class NumeroNegativo(Exception): pass

    def lecturadatos(self, lineedit, type):
        try:
            aux = 0
            if type == 'int':
                aux = int(lineedit.text())
            if type == 'float':
                aux = float(lineedit.text())
            if aux < 0:
                raise NumeroNegativoError
            return aux
        except (TypeError, ValueError, NumeroNegativoError):
            QMessageBox.warning(self, "Error en los datos de entrada! ", "Vuelva a ingresar los datos")
            lineedit.selezctAll()
            lineedit.setFocus()
            raise

    def Calculos(self):
        Q = self.Q
        # Lectura de los datos de entrada con la función verificacion
        try:
            p1 = self.lecturadatos(self.presion1, 'float')
            t1 = self.lecturadatos(self.temperatura1, 'float')
            variableExtra1 = self.selecDatoExtra1.currentText().split("  ")[0]
            datoExtra1 = self.lecturadatos(self.datoExtra1, 'float')
            variableExtra2 = self.selecDatoExtra2.currentText().split("  ")[0]
            datoExtra2 = self.lecturadatos(self.datoExtra2, 'float')
            self.puntos, resultados = ciclo_sabathe.CicloSabathe(p1, t1, Q * 1000, variableExtra1, datoExtra1,
                                                                 variableExtra2, datoExtra2)

        except MayorAUnoError as e:
            QMessageBox.warning(self, "Error en los datos de entrada! ",
                                "La variable " + str(e.variableName) + " no puede ser menor a 1")
            if e.variableName == 'r_comp':
                self.datoExtra1.selectAll()
                self.datoExtra1.setFocus()
            elif e.variableName == 'Alpha':
                self.datoExtra2.selectAll()
                self.datoExtra2.setFocus()
            else:
                pass

        except TemperaturaIncompatibleError as e:
            QMessageBox.warning(self, "Error en los datos de entrada! ",
                                "La temperatura " + str(e.variableName) + " no puede ser menor a la " + \
                                "temepratura del estado anterior (" + str(e.value) + " K)")
            self.datoExtra1.selectAll()
            self.datoExtra1.setFocus()

        except Var2IncompatibleError as e:
            QMessageBox.warning(self, "Error en los datos de entrada!",
                                e.varname + " no puede ser mayor a " + str(e.value1) + \
                                ", ni menor a = " + str(e.value2))
            self.datoExtra2.selectAll()
            self.datoExtra2.setFocus()

        else:
            self.plotCiclo(self.puntos)

            self.calor2.setText(str(resultados[0]))
            self.calorU.setText(str(resultados[1]))
            self.trabajoW.setText(str(resultados[2]))
            self.presionMedia.setText(str(resultados[3]))
            self.rendimiento.setText(str(resultados[4]))

    def plotCiclo(self, puntos):
        presion = []
        temperatura = []
        densidad = []
        volumen = []
        entropia = []
        for punto in puntos:
            presion.append(punto[0])
            temperatura.append(punto[1])
            densidad.append(punto[2])
            volumen.append(punto[3])
            entropia.append(punto[4])

        v1 = np.append(np.arange(volumen[1], volumen[0], (volumen[0]-volumen[1])/100), volumen[0])
        v2 = np.append(np.arange(volumen[3], volumen[4], (volumen[4]-volumen[3])/100), volumen[4])
        self.axes1.clear()
        self.axes1.plot(v1, presion[1]*volumen[1]**self.gamma_aire*(1/v1**self.gamma_aire), 'r')
        self.axes1.plot(volumen[1:4], presion[1:4], 'r', (volumen[4], volumen[0]), (presion[4], presion[0]), 'r')
        self.axes1.plot(v2, presion[3]*volumen[3]**self.gamma_aire*(1/v2**self.gamma_aire), 'r')
        self.canvas1.draw()

        S1 = np.append(np.arange(entropia[1], entropia[2], (entropia[2]-entropia[1])/100), entropia[2])
        S2 = np.append(np.arange(entropia[2], entropia[3], (entropia[3]-entropia[2])/100), entropia[3])
        S3 = np.append(np.arange(entropia[4], entropia[0], (entropia[0]-entropia[4])/100), entropia[0])

        self.axes2.clear()
        self.axes2.plot(S1, temperatura[1]*np.exp((self.gamma_aire-1)*(S1-entropia[1])/self.R_aire), 'r')
        self.axes2.plot(S2, temperatura[2]*np.exp((self.gamma_aire-1)*(S2-entropia[2])/self.R_aire/self.gamma_aire), 'r')
        self.axes2.plot(entropia[0:2], temperatura[0:2], 'r', entropia[3::], temperatura[3::], 'r')
        self.axes2.plot(S3, temperatura[4]*np.exp((self.gamma_aire-1)*(S3-entropia[4])/self.R_aire), 'r')
        self.canvas2.draw()

    def displayMatrix(self):
        matriz = MatrixDialog(self.puntos)
        matriz.exec_()
