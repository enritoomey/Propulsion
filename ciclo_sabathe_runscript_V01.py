# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 20:47:21 2014

@author: Enriquito
"""
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import matplotlib
matplotlib.use('Qt4Agg')
# Hay que agregarle la siguiente linea para que matplotlib use pyside. De esta forma los objetos FigureCanvas y Figure
# compatibles con los Qwidget creados por Pyside!
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
# En el metodo "CicloSabatheGUI" es el obtenido por pyside al procesar el archivo ".ui"
import CicloSabatheGUI_V01 as CicloSabatheGUI
# Importamos los modulos que tienen las funciones para el cálculo de los ciclos. La primera tiene la funció para el
# cálculo de calor especifico asociado a la formula quimica del combustible, y el segundo el programa que resuelve el
# ciclo.
import PoderCalorifico
import ciclo_sabathe_V03 as ciclo_sabathe


class MainDialog(QDialog, CicloSabatheGUI.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.Q = []
        # Generamos dos figuras, cada una luego asociada a un canvas, que a su vez tiene como padre una de las pestañas
        # self.tab -> contiene la pestaña titulada "Diagrama P-S"
        # self.tab_2 -> contiene la pestaña titulada "Diagrama T-S"
        self.fig1 = Figure(figsize=(4.8,3.4),dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        self.axes1 = self.fig1.add_subplot(111)
        self.axes1.set_ylabel('p')
        self.axes1.set_xlabel('v')
        self.axes1.set_title('Ciclo Sabathe')
        self.fig2 = Figure(figsize=(4.8,3.4),dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
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

        # Acciones de actualización de la formula quimica para el calculo de Q
        self.connect(self.formulaC,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaH,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaO,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaS,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.relacionMezcla,SIGNAL("valueChanged(double)"),self.actualizarFormula)
        self.connect(self.calcular,SIGNAL("clicked()"),self.Calculos)

    def actualizarFormula(self):
        c = int(self.formulaC.text())
        h = int(self.formulaH.text())
        o = int(self.formulaO.text())
        s = float(self.formulaS.text())
        Fr = self.relacionMezcla.value()
        HVS, HVI, self.Q, self.lambda_s = PoderCalorifico.PoderCalorifico(c,h,o,s,Fr)
        self.calorQ.setText(str(self.Q))

    def Calculos(self):
        Q = self.Q
        p1 = float(self.presion1.text())
        t1 = float(self.temperatura1.text())
        r_comp = float(self.r_comp.text())
        variableExtra = self.selecDatoExtra.currentText().split()[0]
        datoExtra = float(self.datoExtra.text())

        puntos, resultados = ciclo_sabathe.CicloSabathe(p1,t1,Q*1000,r_comp,variableExtra,datoExtra)
        self.plotCiclo(puntos)

        print(puntos)
        print(resultados)

        self.calor2.setText(str(resultados[0]))
        self.calorU.setText(str(resultados[1]))
        self.trabajoW.setText(str(resultados[2]))
        self.presionMedia.setText(str(resultados[3]))
        self.rendimiento.setText(str(resultados[4]))

    def plotCiclo(self,puntos):
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

        v1 = np.append(np.arange(volumen[1],volumen[0],(volumen[0]-volumen[1])/100),volumen[0])
        v2 = np.append(np.arange(volumen[3],volumen[4],(volumen[4]-volumen[3])/100),volumen[4])
        self.axes1.clear()
        self.axes1.plot(v1,presion[1]*volumen[1]**self.gamma_aire*(1/v1**self.gamma_aire),'r')
        self.axes1.plot(volumen[1:4],presion[1:4],'r',(volumen[4],volumen[0]),(presion[4],presion[0]),'r')
        self.axes1.plot(v2,presion[3]*volumen[3]**self.gamma_aire*(1/v2**self.gamma_aire),'r')
        self.canvas1.draw()

        S1 = np.append(np.arange(entropia[1],entropia[2],(entropia[2]-entropia[1])/100),entropia[2])
        S2 = np.append(np.arange(entropia[2],entropia[3],(entropia[3]-entropia[2])/100),entropia[3])
        S3 = np.append(np.arange(entropia[4],entropia[0],(entropia[0]-entropia[4])/100),entropia[0])

        self.axes2.clear()
        self.axes2.plot(S1,temperatura[1]*np.exp((self.gamma_aire-1)*(S1-entropia[1])/self.R_aire),'r')
        self.axes2.plot(S2,temperatura[2]*np.exp((self.gamma_aire-1)*(S2-entropia[2])/self.R_aire/self.gamma_aire),'r')
        self.axes2.plot(entropia[0:2],temperatura[0:2],'r',entropia[3::],temperatura[3::],'r')
        self.axes2.plot(S3,temperatura[4]*np.exp((self.gamma_aire-1)*(S3-entropia[4])/self.R_aire),'r')
        self.canvas2.draw()

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()




