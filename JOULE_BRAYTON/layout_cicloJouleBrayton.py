# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CicloJouleBraytonGUI_V01.ui'
#
# Created: Sun Apr 05 23:12:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 486)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.DatosEntrada = QtGui.QFrame(Dialog)
        self.DatosEntrada.setGeometry(QtCore.QRect(10, 10, 291, 461))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DatosEntrada.sizePolicy().hasHeightForWidth())
        self.DatosEntrada.setSizePolicy(sizePolicy)
        self.DatosEntrada.setFrameShape(QtGui.QFrame.StyledPanel)
        self.DatosEntrada.setFrameShadow(QtGui.QFrame.Raised)
        self.DatosEntrada.setObjectName("DatosEntrada")
        self.label_8 = QtGui.QLabel(self.DatosEntrada)
        self.label_8.setGeometry(QtCore.QRect(26, 185, 131, 21))
        self.label_8.setObjectName("label_8")
        self.label_2 = QtGui.QLabel(self.DatosEntrada)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(self.DatosEntrada)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_6 = QtGui.QLabel(self.DatosEntrada)
        self.label_6.setGeometry(QtCore.QRect(200, 70, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtGui.QLabel(self.DatosEntrada)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(self.DatosEntrada)
        self.label_5.setGeometry(QtCore.QRect(100, 70, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtGui.QLabel(self.DatosEntrada)
        self.label_7.setGeometry(QtCore.QRect(130, 70, 16, 16))
        self.label_7.setObjectName("label_7")
        self.formulaC = QtGui.QLineEdit(self.DatosEntrada)
        self.formulaC.setGeometry(QtCore.QRect(50, 80, 16, 20))
        self.formulaC.setObjectName("formulaC")
        self.formulaS = QtGui.QLineEdit(self.DatosEntrada)
        self.formulaS.setGeometry(QtCore.QRect(150, 70, 41, 20))
        self.formulaS.setObjectName("formulaS")
        self.formulaH = QtGui.QLineEdit(self.DatosEntrada)
        self.formulaH.setGeometry(QtCore.QRect(80, 80, 16, 20))
        self.formulaH.setObjectName("formulaH")
        self.label_4 = QtGui.QLabel(self.DatosEntrada)
        self.label_4.setGeometry(QtCore.QRect(70, 70, 16, 16))
        self.label_4.setObjectName("label_4")
        self.formulaO = QtGui.QLineEdit(self.DatosEntrada)
        self.formulaO.setGeometry(QtCore.QRect(110, 80, 16, 20))
        self.formulaO.setObjectName("formulaO")
        self.label_16 = QtGui.QLabel(self.DatosEntrada)
        self.label_16.setGeometry(QtCore.QRect(27, 161, 141, 21))
        self.label_16.setObjectName("label_16")
        self.theta1 = QtGui.QLineEdit(self.DatosEntrada)
        self.theta1.setGeometry(QtCore.QRect(170, 381, 91, 20))
        self.theta1.setObjectName("theta1")

        self.label_10 = QtGui.QLabel(self.DatosEntrada)
        self.label_10.setGeometry(QtCore.QRect(26, 225, 41, 21))
        self.label_10.setObjectName("label_10")

        self.presion1 = QtGui.QLineEdit(self.DatosEntrada)
        self.presion1.setGeometry(QtCore.QRect(96, 205, 61, 20))
        self.presion1.setObjectName("presion1")

        self.selecDatoExtra_1 = QtGui.QComboBox(self.DatosEntrada)
        self.selecDatoExtra_1.setGeometry(QtCore.QRect(20, 291, 141, 22))
        self.selecDatoExtra_1.setObjectName("selecDatoExtra_1")
        self.selecDatoExtra_1.addItem("")
        self.selecDatoExtra_1.addItem("")

        self.label_11 = QtGui.QLabel(self.DatosEntrada)
        self.label_11.setGeometry(QtCore.QRect(20, 271, 131, 21))
        self.label_11.setObjectName("label_11")

        self.datoExtra_1 = QtGui.QLineEdit(self.DatosEntrada)
        self.datoExtra_1.setGeometry(QtCore.QRect(170, 291, 91, 20))
        self.datoExtra_1.setObjectName("datoExtra_1")

        self.temperatura1 = QtGui.QLineEdit(self.DatosEntrada)
        self.temperatura1.setGeometry(QtCore.QRect(96, 225, 61, 20))
        self.temperatura1.setObjectName("temperatura1")

        self.label_13 = QtGui.QLabel(self.DatosEntrada)
        self.label_13.setGeometry(QtCore.QRect(20, 381, 141, 16))
        self.label_13.setObjectName("label_13")

        self.label_9 = QtGui.QLabel(self.DatosEntrada)
        self.label_9.setGeometry(QtCore.QRect(26, 205, 51, 21))
        self.label_9.setObjectName("label_9")

        self.relacionMezcla = QtGui.QDoubleSpinBox(self.DatosEntrada)
        self.relacionMezcla.setGeometry(QtCore.QRect(146, 107, 62, 22))
        self.relacionMezcla.setDecimals(3)
        self.relacionMezcla.setMinimum(0.001)
        self.relacionMezcla.setMaximum(999999999.0)
        self.relacionMezcla.setSingleStep(0.05)
        self.relacionMezcla.setProperty("value", 1.0)
        self.relacionMezcla.setObjectName("relacionMezcla")

        self.label_12 = QtGui.QLabel(self.DatosEntrada)
        self.label_12.setGeometry(QtCore.QRect(26, 107, 131, 21))
        self.label_12.setObjectName("label_12")

        self.calorQ = QtGui.QLineEdit(self.DatosEntrada)
        self.calorQ.setGeometry(QtCore.QRect(177, 161, 91, 20))
        self.calorQ.setObjectName("calorQ")

        self.calcular = QtGui.QPushButton(self.DatosEntrada)
        self.calcular.setGeometry(QtCore.QRect(90, 431, 101, 23))
        self.calcular.setObjectName("calcular")

        self.temperatura_base = QtGui.QLineEdit(self.DatosEntrada)
        self.temperatura_base.setGeometry(QtCore.QRect(96, 245, 61, 20))
        self.temperatura_base.setObjectName("temperatura_base")

        self.label_temperaturabase = QtGui.QLabel(self.DatosEntrada)
        self.label_temperaturabase.setGeometry(QtCore.QRect(26, 245, 51, 21))
        self.label_temperaturabase.setObjectName("label_temperaturabase")

        self.selecDatoExtra_2 = QtGui.QComboBox(self.DatosEntrada)
        self.selecDatoExtra_2.setGeometry(QtCore.QRect(20, 321, 141, 22))
        self.selecDatoExtra_2.setObjectName("selecDatoExtra_2")
        self.selecDatoExtra_2.addItem("")
        self.selecDatoExtra_2.addItem("")

        self.datoExtra_2 = QtGui.QLineEdit(self.DatosEntrada)
        self.datoExtra_2.setGeometry(QtCore.QRect(170, 321, 91, 20))
        self.datoExtra_2.setObjectName("datoExtra_2")

        self.label_22 = QtGui.QLabel(self.DatosEntrada)
        self.label_22.setGeometry(QtCore.QRect(20, 354, 131, 21))
        self.label_22.setObjectName("label_22")

        self.PostCombustion = QtGui.QCheckBox(self.DatosEntrada)
        self.PostCombustion.setGeometry(QtCore.QRect(114, 357, 70, 17))
        self.PostCombustion.setText("")
        self.PostCombustion.setObjectName("PostCombustion")

        self.datoExtra_3 = QtGui.QLineEdit(self.DatosEntrada)
        self.datoExtra_3.setGeometry(QtCore.QRect(170, 401, 91, 20))
        self.datoExtra_3.setObjectName("datoExtra_3")

        self.selecDatoExtra_3 = QtGui.QComboBox(self.DatosEntrada)
        self.selecDatoExtra_3.setGeometry(QtCore.QRect(20, 401, 141, 22))
        self.selecDatoExtra_3.setObjectName("selecDatoExtra_3")
        self.selecDatoExtra_3.addItem("")
        self.selecDatoExtra_3.addItem("")

        self.formula_comboBox = QtGui.QComboBox(self.DatosEntrada)
        self.formula_comboBox.setGeometry(QtCore.QRect(120, 40, 151, 22))
        self.formula_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formula_comboBox.setObjectName("formula_comboBox")
        self.formula_comboBox.addItem("")

        self.Altura_Button = QtGui.QPushButton(self.DatosEntrada)
        self.Altura_Button.setGeometry(QtCore.QRect(176, 215, 91, 41))
        self.Altura_Button.setObjectName("Altura_Button")

        self.HVS_lineEdit = QtGui.QLineEdit(self.DatosEntrada)
        self.HVS_lineEdit.setGeometry(QtCore.QRect(96, 135, 51, 20))
        self.HVS_lineEdit.setObjectName("HVS_lineEdit")

        self.HVI_lineEdit = QtGui.QLineEdit(self.DatosEntrada)
        self.HVI_lineEdit.setGeometry(QtCore.QRect(223, 134, 51, 20))
        self.HVI_lineEdit.setObjectName("HVI_lineEdit")

        self.label_HVI = QtGui.QLabel(self.DatosEntrada)
        self.label_HVI.setGeometry(QtCore.QRect(160, 134, 71, 21))
        self.label_HVI.setObjectName("label_HVI")
        self.label_HVS = QtGui.QLabel(self.DatosEntrada)
        self.label_HVS.setGeometry(QtCore.QRect(28, 133, 71, 21))
        self.label_HVS.setObjectName("label_HVS")

        self.DatosSalida = QtGui.QFrame(Dialog)
        self.DatosSalida.setGeometry(QtCore.QRect(320, 340, 361, 111))
        self.DatosSalida.setFrameShape(QtGui.QFrame.StyledPanel)
        self.DatosSalida.setFrameShadow(QtGui.QFrame.Raised)
        self.DatosSalida.setObjectName("DatosSalida")

        self.label_17 = QtGui.QLabel(self.DatosSalida)
        self.label_17.setGeometry(QtCore.QRect(30, 40, 141, 21))
        self.label_17.setObjectName("label_17")

        self.label_18 = QtGui.QLabel(self.DatosSalida)
        self.label_18.setGeometry(QtCore.QRect(180, 77, 141, 21))
        self.label_18.setObjectName("label_18")

        self.label_19 = QtGui.QLabel(self.DatosSalida)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 141, 21))
        self.label_19.setObjectName("label_19")

        self.label_20 = QtGui.QLabel(self.DatosSalida)
        self.label_20.setGeometry(QtCore.QRect(30, 80, 141, 21))
        self.label_20.setObjectName("label_20")

        self.label_21 = QtGui.QLabel(self.DatosSalida)
        self.label_21.setGeometry(QtCore.QRect(180, 57, 141, 21))
        self.label_21.setObjectName("label_21")

        self.calor2 = QtGui.QLineEdit(self.DatosSalida)
        self.calor2.setGeometry(QtCore.QRect(110, 40, 61, 20))
        self.calor2.setObjectName("calor2")

        self.label_14 = QtGui.QLabel(self.DatosSalida)
        self.label_14.setGeometry(QtCore.QRect(20, 10, 151, 21))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")

        self.calorU = QtGui.QLineEdit(self.DatosSalida)
        self.calorU.setGeometry(QtCore.QRect(110, 60, 61, 20))
        self.calorU.setObjectName("calorU")

        self.trabajoW = QtGui.QLineEdit(self.DatosSalida)
        self.trabajoW.setGeometry(QtCore.QRect(110, 80, 61, 20))
        self.trabajoW.setObjectName("trabajoW")

        self.presionMedia = QtGui.QLineEdit(self.DatosSalida)
        self.presionMedia.setGeometry(QtCore.QRect(280, 57, 71, 20))
        self.presionMedia.setObjectName("presionMedia")

        self.rendimiento = QtGui.QLineEdit(self.DatosSalida)
        self.rendimiento.setGeometry(QtCore.QRect(310, 77, 41, 20))
        self.rendimiento.setObjectName("rendimiento")

        self.matrixButton = QtGui.QPushButton(self.DatosSalida)
        self.matrixButton.setGeometry(QtCore.QRect(200, 10, 131, 31))
        self.matrixButton.setObjectName("matrixButton")

        self.PlotArea = QtGui.QTabWidget(Dialog)
        self.PlotArea.setGeometry(QtCore.QRect(310, 10, 381, 311))
        self.PlotArea.setMovable(False)
        self.PlotArea.setObjectName("PlotArea")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.PlotArea.addTab(self.tab, "")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.PlotArea.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.PlotArea.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.formulaC, self.formulaH)
        Dialog.setTabOrder(self.formulaH, self.formulaO)
        Dialog.setTabOrder(self.formulaO, self.formulaS)
        Dialog.setTabOrder(self.formulaS, self.relacionMezcla)
        Dialog.setTabOrder(self.relacionMezcla, self.calorQ)
        Dialog.setTabOrder(self.calorQ, self.presion1)
        Dialog.setTabOrder(self.presion1, self.temperatura1)
        Dialog.setTabOrder(self.temperatura1, self.temperatura_base)
        Dialog.setTabOrder(self.temperatura_base, self.selecDatoExtra_1)
        Dialog.setTabOrder(self.selecDatoExtra_1, self.datoExtra_1)
        Dialog.setTabOrder(self.datoExtra_1, self.selecDatoExtra_2)
        Dialog.setTabOrder(self.selecDatoExtra_2, self.datoExtra_2)
        Dialog.setTabOrder(self.datoExtra_2, self.PostCombustion)
        Dialog.setTabOrder(self.PostCombustion, self.theta1)
        Dialog.setTabOrder(self.theta1, self.selecDatoExtra_3)
        Dialog.setTabOrder(self.selecDatoExtra_3, self.datoExtra_3)
        Dialog.setTabOrder(self.datoExtra_3, self.calcular)
        Dialog.setTabOrder(self.calcular, self.PlotArea)
        Dialog.setTabOrder(self.PlotArea, self.calor2)
        Dialog.setTabOrder(self.calor2, self.calorU)
        Dialog.setTabOrder(self.calorU, self.trabajoW)
        Dialog.setTabOrder(self.trabajoW, self.presionMedia)
        Dialog.setTabOrder(self.presionMedia, self.rendimiento)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ciclo Joule-Brayton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Parametros atmosféricos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Formula Química:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Datos de Entrada</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">% </span><span style=\" font-size:12pt; font-weight:600;\">S</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">C</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">O</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">+</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaC.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaS.setText(QtGui.QApplication.translate("Dialog", "00.00", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaH.setText(QtGui.QApplication.translate("Dialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">H</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaO.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Calor aportado [KJ/kg aire]=", None, QtGui.QApplication.UnicodeUTF8))
        self.theta1.setText(QtGui.QApplication.translate("Dialog", "1.5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">1</span>  [K] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.presion1.setText(QtGui.QApplication.translate("Dialog", "101325", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_1.setItemText(0, QtGui.QApplication.translate("Dialog", "Theta                         =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_1.setItemText(1, QtGui.QApplication.translate("Dialog", "Relacion de comp.  =", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Datos del ciclo:", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_1.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatura1.setText(QtGui.QApplication.translate("Dialog", "293", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Theta<span style=\" vertical-align:sub;\">1                   </span> = </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">1</span>  [Pa] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Relación de mezcla F<span style=\" vertical-align:sub;\">r </span>=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.calcular.setText(QtGui.QApplication.translate("Dialog", "Calcular", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatura_base.setText(QtGui.QApplication.translate("Dialog", "273", None, QtGui.QApplication.UnicodeUTF8))
        self.label_temperaturabase.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">b</span> [K] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_2.setItemText(0, QtGui.QApplication.translate("Dialog", "Temp. max                 =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_2.setItemText(1, QtGui.QApplication.translate("Dialog", "Q                                 =", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_2.setText(QtGui.QApplication.translate("Dialog", "1600", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Post Combustión:", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_3.setText(QtGui.QApplication.translate("Dialog", "2500", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_3.setItemText(0, QtGui.QApplication.translate("Dialog", "T5                              =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_3.setItemText(1, QtGui.QApplication.translate("Dialog", "Q1 [KJ/kg]                            =", None, QtGui.QApplication.UnicodeUTF8))
        self.formula_comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Otra", None, QtGui.QApplication.UnicodeUTF8))
        self.Altura_Button.setText(QtGui.QApplication.translate("Dialog", "Selecionar Altura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_HVI.setText(QtGui.QApplication.translate("Dialog", "HVI [KJ/kg]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_HVS.setText(QtGui.QApplication.translate("Dialog", "HVS [KJ/kg]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Q<span style=\" vertical-align:sub;\">2 </span>[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Rendimiento [KJ/kg aire]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Qu<span style=\" vertical-align:sub;\"/>[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>W[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog", "Presión media [Pa]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Datos de Salida</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixButton.setText(QtGui.QApplication.translate("Dialog", "Matriz de Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotArea.setTabText(self.PlotArea.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Diagrama P-V", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotArea.setTabText(self.PlotArea.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Diagrama T-S (Mollier)", None, QtGui.QApplication.UnicodeUTF8))

