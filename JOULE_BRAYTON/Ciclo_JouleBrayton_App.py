# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 20:47:21 2014

@author: Enriquito
"""

import matplotlib  # Para los graficos
from PySide.QtCore import *
from PySide.QtGui import *  # importo todas las funciones de pyside

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
# Estas lineas son un poco misteriosas, pero son las que me permite
# vincular los Widget de Qt/Pyside con matplotlib

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from excepciones import NumeroNegativoError,MayorAUnoError,TemperaturaIncompatibleError
import numpy as np # Para las cuentas
import Ciclo_JouleBrayton_V00 as Ciclo_JouleBrayton # contiene la funcion que hace las cuentas
import common.PoderCalorifico as PoderCalorifico# Continene la funcion que calcula el poder calorifico
import layout_cicloJouleBrayton # importo las clases creadas con Qt y pyside
import common.GUI_atmosfera_estandar as GUI_atmosfera_estandar
from common.MatrixClass import MatrixDialog
__appName__ = 'Ciclo Joule-Brayton'

# Creo la clase principal, llamada ""Main Dialog"
class JouleBraytonDialog(QDialog, layout_cicloJouleBrayton.Ui_Dialog):

    # Estas lineas son medias magicas, pero siempre van:
    def __init__(self,parent=None):
        super(JouleBraytonDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appName__)

        # Creo algunas variables que generales que luego voy a usar
        self.Q = []
        self.gamma_aire = 1.4
        self.R_aire = 287
        #Defino las formulas quimicas para selecionar en formulas_comboBox
        self.formulas = {"AvGas":{'c':7,'h':16,'o':0,'s':0.00},"Diesel":{'c':12,'h':21,'o':0,'s':0.00}}
        # Utilizo las 'keys' de self.formulas para cargar los items en la combobox
        for key in self.formulas.keys():
            self.formula_comboBox.addItem(key)

        self.actualizarFormula()

        # Generamos dos figuras, cada una luego asociada a un canvas, que a su vez tiene como padre una de las pestañas
        # self.tab -> contiene la pestaña titulada "Diagrama P-S"
        # self.tab_2 -> contiene la pestaña titulada "Diagrama T-S"
        self.fig1 = Figure(figsize=(4.8,3.4),dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        self.axes1 = self.fig1.add_subplot(111)
        self.axes1.set_ylabel('p')
        self.axes1.set_xlabel('v')
        self.axes1.set_title('Ciclo Joule-Brayton')
        self.axes1.ticklabel_format(style="sci", scilimits=(0, 0), axis="both")  # , useOffset=True,useLocale=True)
        self.axes1.tick_params(axis="both", direction='in', length=6, width=2, labelsize="medium")
        self.fig2 = Figure(figsize=(4.8,3.4),dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        self.axes2 = self.fig2.add_subplot(111)
        self.axes2.set_ylabel('T')
        self.axes2.ticklabel_format(style='sci', scilimits=(0, 0), axis="both")
        self.axes2.set_xlabel('S')
        self.axes2.set_title('Ciclo Joule-Brayton')
        # generate the canvas to display the plot
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas1.setParent(self.tab)
        self.canvas1.show()
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas2.setParent(self.tab_2)
        self.canvas2.show()

#        Cambio los lineInput de HVS y HVI a "ReadOnly"
        self.HVS_lineEdit.setReadOnly(True)
        self.HVI_lineEdit.setReadOnly(True)

        #Inicializo la parte de la postcombustión como no habilitada.
        self.datoExtra_3.setDisabled(True)
        self.selecDatoExtra_3.setDisabled(True)
        self.theta1.setDisabled(True)

        #Seleccion de una formula en formula_comboBox
        self.connect(self.formula_comboBox,SIGNAL("currentIndexChanged(int)"),self.selecionFormula)

        #Acciones de actualización de la formula quimica para el calculo de Q
        # En este punto tengo que agregar la opción de que si Q surge como resultado
        # de otro parametros de entrada, la relación demezcla se tendrá que actualizar
        # para que la formula y la relación sean compatibles con el Q obtenido
        self.connect(self.formulaC,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaH,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaO,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.formulaS,SIGNAL("textEdited(const QString&)"),self.actualizarFormula)
        self.connect(self.relacionMezcla,SIGNAL("valueChanged(double)"),self.actualizarFormula)
        self.connect(self.calcular,SIGNAL("clicked()"),self.Calculos)
        # Configurando el boton de check para la postcombustion
        self.connect(self.PostCombustion,SIGNAL("stateChanged(int)"),self.enable_PostCombustion)
        self.connect(self.selecDatoExtra_2,SIGNAL("currentIndexChanged(int)"),self.actualizarFormula)
        # Boton para mostrar matriz de resultados
        self.connect(self.matrixButton,SIGNAL("clicked()"),self.displayMatrix)
        #Boton para seleccionar P1 y T1 a partir de la altura:
        self.connect(self.Altura_Button,SIGNAL("clicked()"),self.seleccionAltura)

    def enable_PostCombustion(self):
        if self.PostCombustion.checkState():
            self.datoExtra_3.setEnabled(True)
            self.selecDatoExtra_3.setEnabled(True)
            self.theta1.setEnabled(True)
        else:
            self.datoExtra_3.setDisabled(True)
            self.selecDatoExtra_3.setDisabled(True)
            self.theta1.setDisabled(True)


    def selecionFormula(self):
        formula = self.formula_comboBox.currentText()
        if formula != 'Otra':
            self.formulaC.setText(str(self.formulas[formula]['c']))
            self.formulaH.setText(str(self.formulas[formula]['h']))
            self.formulaO.setText(str(self.formulas[formula]['o']))
            self.formulaS.setText(str(self.formulas[formula]['s']))
            self.actualizarFormula()

    def actualizarFormula(self):
        c = self.lecturadatos(self.formulaC,'int')
        h = self.lecturadatos(self.formulaH,'int')
        o = self.lecturadatos(self.formulaO,'int')
        s = self.lecturadatos(self.formulaS,'float')
        # si la formula ingresada coincide con alguna formula del comboBox
        # poner el comboBox en esa formula.
        indexName = 'Otra'
        for key in self.formulas.keys():
            if (self.formulas[key]['c'] == c) &  (self.formulas[key]['h'] == h) & (self.formulas[key]['o'] == o):
                indexName = key
        index = self.formula_comboBox.findText(indexName)
        self.formula_comboBox.setCurrentIndex(index)

        Fr = self.relacionMezcla.value()
        self.HVS, self.HVI, self.Q, self.lambda_s = PoderCalorifico.PoderCalorifico(c,h,o,s,Fr)
        self.HVS_lineEdit.setText('{:.1f}'.format(self.HVS))
        self.HVI_lineEdit.setText('{:.1f}'.format(self.HVI))
        self.calorQ.setText('{:.1f}'.format(self.Q))
        if self.selecDatoExtra_2.currentText().split("  ")[0] == 'Q':
            self.datoExtra_2.setText(str(self.Q))
            self.datoExtra_2.setReadOnly(True)
        else: self.datoExtra_2.setReadOnly(False)

    def seleccionAltura(self):
        p1 = str(self.presion1.text())
        t1 = str(self.temperatura1.text())
        dialogo = GUI_atmosfera_estandar.MainDialog(p1,t1)
        if dialogo.exec_():
            self.presion1.setText('{:.1f}'.format(dialogo.atmosfera['p']))
            self.temperatura1.setText('{:.1f}'.format(dialogo.atmosfera['t']))

    def lecturadatos(self,lineedit,type):
        try:
            aux = 0
            if type == 'int':
                aux = int(lineedit.text())
            if type == 'float':
                aux = float(lineedit.text())
            if aux < 0:
                raise NumeroNegativoError
            return aux
        except (TypeError, ValueError,NumeroNegativoError):
            QMessageBox.warning(self,"Error en los datos de entrada! ","Vuelva a ingresar los datos")
            lineedit.selectAll()
            lineedit.setFocus()
            raise

    # Genero ahora la función que va a realizar los calculos, es decir,
    # que va a llamar la función del ciclo.
    def Calculos(self):
        # Lectura de los datos de entrada con la función verificacion
        p1 = self.lecturadatos(self.presion1,'float')
        t1 = self.lecturadatos(self.temperatura1,'float')
        tb = self.lecturadatos(self.temperatura_base,'float')
        variableExtra1 = self.selecDatoExtra_1.currentText().split("  ")[0]
        datoExtra1 = self.lecturadatos(self.datoExtra_1,'float')
        variableExtra2 = self.selecDatoExtra_2.currentText().split("  ")[0]
        datoExtra2 = self.lecturadatos(self.datoExtra_2,'float')
        theta1 = self.lecturadatos(self.theta1,'float')
        variableExtra3 = self.selecDatoExtra_3.currentText().split()[0]
        datoExtra3 = self.lecturadatos(self.datoExtra_3,'float')
        try:
            #Procedo a calcular los parametros del ciclo, diferenciando entre el problema
            #con y sin post-combustión
            if self.PostCombustion.checkState()== Qt.CheckState.Checked:
                self.puntos, self.resultados = Ciclo_JouleBrayton.CicloJouleBraytonPostcombustion(p1,t1,tb,theta1,variableExtra1,datoExtra1,variableExtra2,datoExtra2,variableExtra3,datoExtra3)
            else:
                self.puntos, self.resultados = Ciclo_JouleBrayton.CicloJouleBraytonSimple(p1,t1,tb,variableExtra1,datoExtra1,variableExtra2,datoExtra2)

        except MayorAUnoError as e:
            QMessageBox.warning(self,"Error en los datos de entrada! ","La variable "+str(e.variableName)+" no puede ser menor a 1")
            if e.variableName == 'theta1':
                self.theta1.selectAll()
                self.theta1.setFocus()
            else:
                self.datoExtra_1.selectAll()
                self.datoExtra_1.setFocus()

        except TemperaturaIncompatibleError as e:
            QMessageBox.warning(self,"Error en los datos de entrada! ","La temperatura "+str(e.variableName)+" no puede ser menor a la "+
                                    "temepratura del estado anterior ("+str(e.value)+" K)")
            if e.variableName == 't3':
                self.datoExtra_2.selectAll()
                self.datoExtra_2.setFocus()
            else:
                self.datoExtra_3.selecAll()
                self.datoExtra_3.setFocus()

        else:
            #Grafico el resultado
            self.plotCiclo(self.puntos)

            # Muestro los resultados
            self.calor2.setText(str(self.resultados[1]))
            self.calorU.setText(str(self.resultados[2]))
            self.trabajoW.setText(str(self.resultados[3]))
            self.presionMedia.setText(str(self.resultados[4]))
            self.rendimiento.setText(str(self.resultados[5]))

            # En caso de que realice un calculo con "Temp. max" como parametro de
            #entrada, Q es resultado del calculo. Como la formula quimica del combustible
            # y por ende, su poder calorifico, no varian, debo cambiar la relación
            # de mezcla de entrada para que sea compatible con el nuevo calor calculado.
            self.Q = self.resultados[0]/1000
            if self.selecDatoExtra_2.currentText().split("  ")[0] == "Temp. max":
                self.calorQ.setText(str(self.Q))
                self.relacionMezcla.setValue(self.Q*self.lambda_s/self.HVI)

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
        v2 = np.append(np.arange(volumen[-2],volumen[-1],(volumen[-1]-volumen[-2])/100),volumen[-1])
        self.axes1.clear()
        self.axes1.plot(v1,presion[1]*volumen[1]**self.gamma_aire*(1/v1**self.gamma_aire),'r')
        self.axes1.plot(volumen[1:3],presion[1:3],'r')
        self.axes1.plot((volumen[0],volumen[-1]),(presion[0],presion[-1]),'r')
        self.axes1.plot(v2,presion[-2]*volumen[-2]**self.gamma_aire*(1/v2**self.gamma_aire),'r')
        if self.PostCombustion.checkState() == Qt.CheckState.Checked:
            self.axes1.plot((volumen[-3],volumen[-2]),(presion[-3],presion[-2]),'r')
            v3 = np.append(np.arange(volumen[2],volumen[3],(volumen[3]-volumen[2])/100),volumen[3])
            self.axes1.plot(v3,presion[2]*volumen[2]**self.gamma_aire*(1/v3**self.gamma_aire),'r')

        self.canvas1.draw()

        S1 = np.append(np.arange(entropia[1],entropia[2],(entropia[2]-entropia[1])/100),entropia[2])
        S2 = np.append(np.arange(entropia[0],entropia[-1],(entropia[-1]-entropia[0])/100),entropia[-1])

        self.axes2.clear()
        self.axes2.plot(entropia[0:2],temperatura[0:2],'r',entropia[-2::],temperatura[-2::],'r')
        self.axes2.plot(S1,temperatura[1]*np.exp((self.gamma_aire-1)*(S1-entropia[1])/(self.R_aire*self.gamma_aire)),'r')
        self.axes2.plot(S2,temperatura[0]*np.exp((self.gamma_aire-1)*(S2-entropia[0])/(self.R_aire*self.gamma_aire)),'r')
        if self.PostCombustion.checkState()==Qt.CheckState.Checked:
            S3 = np.append(np.arange(entropia[3],entropia[4],(entropia[4]-entropia[3])/100),entropia[4])
            self.axes2.plot(entropia[2:4],temperatura[2:4],'r')
            self.axes2.plot(S3,temperatura[3]*np.exp((self.gamma_aire-1)*(S3-entropia[3])/self.R_aire/self.gamma_aire),'r')
        self.canvas2.draw()


    def displayMatrix(self):
        matriz = MatrixDialog(self.puntos)
        matriz.exec_()
