# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JOULE_BRAYTON/CicloJouleBraytonGUI.ui'
#
# Created: Mon May 14 23:32:46 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 671)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_21 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.DatosEntrada = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DatosEntrada.sizePolicy().hasHeightForWidth())
        self.DatosEntrada.setSizePolicy(sizePolicy)
        self.DatosEntrada.setFrameShape(QtGui.QFrame.StyledPanel)
        self.DatosEntrada.setFrameShadow(QtGui.QFrame.Raised)
        self.DatosEntrada.setObjectName("DatosEntrada")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.DatosEntrada)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtGui.QLabel(self.DatosEntrada)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_2 = QtGui.QLabel(self.DatosEntrada)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_20.addWidget(self.label_2)
        self.formula_comboBox = QtGui.QComboBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formula_comboBox.sizePolicy().hasHeightForWidth())
        self.formula_comboBox.setSizePolicy(sizePolicy)
        self.formula_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formula_comboBox.setObjectName("formula_comboBox")
        self.formula_comboBox.addItem("")
        self.horizontalLayout_20.addWidget(self.formula_comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_20)
        self.formula_frame = QtGui.QFrame(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formula_frame.sizePolicy().hasHeightForWidth())
        self.formula_frame.setSizePolicy(sizePolicy)
        self.formula_frame.setMinimumSize(QtCore.QSize(250, 30))
        self.formula_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.formula_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.formula_frame.setObjectName("formula_frame")
        self.label_3 = QtGui.QLabel(self.formula_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 16, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.formula_frame)
        self.label_4.setGeometry(QtCore.QRect(40, 0, 16, 21))
        self.label_4.setObjectName("label_4")
        self.formulaO = QtGui.QLineEdit(self.formula_frame)
        self.formulaO.setGeometry(QtCore.QRect(80, 10, 16, 20))
        self.formulaO.setObjectName("formulaO")
        self.formulaH = QtGui.QLineEdit(self.formula_frame)
        self.formulaH.setGeometry(QtCore.QRect(50, 10, 16, 20))
        self.formulaH.setObjectName("formulaH")
        self.label_7 = QtGui.QLabel(self.formula_frame)
        self.label_7.setGeometry(QtCore.QRect(100, 0, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtGui.QLabel(self.formula_frame)
        self.label_5.setGeometry(QtCore.QRect(70, 0, 16, 21))
        self.label_5.setObjectName("label_5")
        self.formulaC = QtGui.QLineEdit(self.formula_frame)
        self.formulaC.setGeometry(QtCore.QRect(20, 10, 16, 20))
        self.formulaC.setObjectName("formulaC")
        self.label_15 = QtGui.QLabel(self.formula_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 0, 16, 21))
        self.label_15.setObjectName("label_15")
        self.label_23 = QtGui.QLabel(self.formula_frame)
        self.label_23.setGeometry(QtCore.QRect(70, 0, 16, 21))
        self.label_23.setObjectName("label_23")
        self.layoutWidget = QtGui.QWidget(self.formula_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 0, 91, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.formulaS = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formulaS.sizePolicy().hasHeightForWidth())
        self.formulaS.setSizePolicy(sizePolicy)
        self.formulaS.setObjectName("formulaS")
        self.horizontalLayout_19.addWidget(self.formulaS)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_19.addWidget(self.label_6)
        self.verticalLayout_6.addWidget(self.formula_frame)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_12 = QtGui.QLabel(self.DatosEntrada)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_18.addWidget(self.label_12)
        self.relacionMezcla = QtGui.QDoubleSpinBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relacionMezcla.sizePolicy().hasHeightForWidth())
        self.relacionMezcla.setSizePolicy(sizePolicy)
        self.relacionMezcla.setMaximum(999999999.0)
        self.relacionMezcla.setSingleStep(0.01)
        self.relacionMezcla.setProperty("value", 1.0)
        self.relacionMezcla.setObjectName("relacionMezcla")
        self.horizontalLayout_18.addWidget(self.relacionMezcla)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_HVS = QtGui.QLabel(self.DatosEntrada)
        self.label_HVS.setObjectName("label_HVS")
        self.horizontalLayout_17.addWidget(self.label_HVS)
        self.HVS_lineEdit = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HVS_lineEdit.sizePolicy().hasHeightForWidth())
        self.HVS_lineEdit.setSizePolicy(sizePolicy)
        self.HVS_lineEdit.setObjectName("HVS_lineEdit")
        self.horizontalLayout_17.addWidget(self.HVS_lineEdit)
        self.label_HVI = QtGui.QLabel(self.DatosEntrada)
        self.label_HVI.setObjectName("label_HVI")
        self.horizontalLayout_17.addWidget(self.label_HVI)
        self.HVI_lineEdit = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HVI_lineEdit.sizePolicy().hasHeightForWidth())
        self.HVI_lineEdit.setSizePolicy(sizePolicy)
        self.HVI_lineEdit.setObjectName("HVI_lineEdit")
        self.horizontalLayout_17.addWidget(self.HVI_lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtGui.QLabel(self.DatosEntrada)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.calorQ = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calorQ.sizePolicy().hasHeightForWidth())
        self.calorQ.setSizePolicy(sizePolicy)
        self.calorQ.setObjectName("calorQ")
        self.horizontalLayout_16.addWidget(self.calorQ)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtGui.QLabel(self.DatosEntrada)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtGui.QLabel(self.DatosEntrada)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.presion1 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presion1.sizePolicy().hasHeightForWidth())
        self.presion1.setSizePolicy(sizePolicy)
        self.presion1.setObjectName("presion1")
        self.horizontalLayout_14.addWidget(self.presion1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtGui.QLabel(self.DatosEntrada)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.temperatura1 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatura1.sizePolicy().hasHeightForWidth())
        self.temperatura1.setSizePolicy(sizePolicy)
        self.temperatura1.setObjectName("temperatura1")
        self.horizontalLayout_13.addWidget(self.temperatura1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_temperaturabase = QtGui.QLabel(self.DatosEntrada)
        self.label_temperaturabase.setObjectName("label_temperaturabase")
        self.horizontalLayout_12.addWidget(self.label_temperaturabase)
        self.temperatura_base = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatura_base.sizePolicy().hasHeightForWidth())
        self.temperatura_base.setSizePolicy(sizePolicy)
        self.temperatura_base.setObjectName("temperatura_base")
        self.horizontalLayout_12.addWidget(self.temperatura_base)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        self.Altura_Button = QtGui.QPushButton(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Altura_Button.sizePolicy().hasHeightForWidth())
        self.Altura_Button.setSizePolicy(sizePolicy)
        self.Altura_Button.setObjectName("Altura_Button")
        self.horizontalLayout_15.addWidget(self.Altura_Button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtGui.QLabel(self.DatosEntrada)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.selecDatoExtra_1 = QtGui.QComboBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selecDatoExtra_1.sizePolicy().hasHeightForWidth())
        self.selecDatoExtra_1.setSizePolicy(sizePolicy)
        self.selecDatoExtra_1.setObjectName("selecDatoExtra_1")
        self.selecDatoExtra_1.addItem("")
        self.selecDatoExtra_1.addItem("")
        self.horizontalLayout_11.addWidget(self.selecDatoExtra_1)
        self.datoExtra_1 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datoExtra_1.sizePolicy().hasHeightForWidth())
        self.datoExtra_1.setSizePolicy(sizePolicy)
        self.datoExtra_1.setObjectName("datoExtra_1")
        self.horizontalLayout_11.addWidget(self.datoExtra_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.selecDatoExtra_2 = QtGui.QComboBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selecDatoExtra_2.sizePolicy().hasHeightForWidth())
        self.selecDatoExtra_2.setSizePolicy(sizePolicy)
        self.selecDatoExtra_2.setObjectName("selecDatoExtra_2")
        self.selecDatoExtra_2.addItem("")
        self.selecDatoExtra_2.addItem("")
        self.horizontalLayout_10.addWidget(self.selecDatoExtra_2)
        self.datoExtra_2 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datoExtra_2.sizePolicy().hasHeightForWidth())
        self.datoExtra_2.setSizePolicy(sizePolicy)
        self.datoExtra_2.setObjectName("datoExtra_2")
        self.horizontalLayout_10.addWidget(self.datoExtra_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_22 = QtGui.QLabel(self.DatosEntrada)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_9.addWidget(self.label_22)
        self.PostCombustion = QtGui.QCheckBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PostCombustion.sizePolicy().hasHeightForWidth())
        self.PostCombustion.setSizePolicy(sizePolicy)
        self.PostCombustion.setText("")
        self.PostCombustion.setObjectName("PostCombustion")
        self.horizontalLayout_9.addWidget(self.PostCombustion)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtGui.QLabel(self.DatosEntrada)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.theta1 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theta1.sizePolicy().hasHeightForWidth())
        self.theta1.setSizePolicy(sizePolicy)
        self.theta1.setObjectName("theta1")
        self.horizontalLayout_7.addWidget(self.theta1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.selecDatoExtra_3 = QtGui.QComboBox(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selecDatoExtra_3.sizePolicy().hasHeightForWidth())
        self.selecDatoExtra_3.setSizePolicy(sizePolicy)
        self.selecDatoExtra_3.setObjectName("selecDatoExtra_3")
        self.selecDatoExtra_3.addItem("")
        self.selecDatoExtra_3.addItem("")
        self.horizontalLayout_8.addWidget(self.selecDatoExtra_3)
        self.datoExtra_3 = QtGui.QLineEdit(self.DatosEntrada)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datoExtra_3.sizePolicy().hasHeightForWidth())
        self.datoExtra_3.setSizePolicy(sizePolicy)
        self.datoExtra_3.setObjectName("datoExtra_3")
        self.horizontalLayout_8.addWidget(self.datoExtra_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.calcular = QtGui.QPushButton(self.DatosEntrada)
        self.calcular.setObjectName("calcular")
        self.verticalLayout_7.addWidget(self.calcular)
        self.horizontalLayout_21.addWidget(self.DatosEntrada)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 1, -1, 50)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.PlotArea = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotArea.sizePolicy().hasHeightForWidth())
        self.PlotArea.setSizePolicy(sizePolicy)
        self.PlotArea.setMovable(False)
        self.PlotArea.setObjectName("PlotArea")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.PlotArea.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.PlotArea.addTab(self.tab_2, "")
        self.verticalLayout_8.addWidget(self.PlotArea)
        self.DatosSalida = QtGui.QFrame(Dialog)
        self.DatosSalida.setFrameShape(QtGui.QFrame.StyledPanel)
        self.DatosSalida.setFrameShadow(QtGui.QFrame.Raised)
        self.DatosSalida.setObjectName("DatosSalida")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.DatosSalida)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtGui.QLabel(self.DatosSalida)
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtGui.QLabel(self.DatosSalida)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.calor2 = QtGui.QLineEdit(self.DatosSalida)
        self.calor2.setObjectName("calor2")
        self.horizontalLayout.addWidget(self.calor2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_19 = QtGui.QLabel(self.DatosSalida)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.calorU = QtGui.QLineEdit(self.DatosSalida)
        self.calorU.setObjectName("calorU")
        self.horizontalLayout_2.addWidget(self.calorU)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_20 = QtGui.QLabel(self.DatosSalida)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.trabajoW = QtGui.QLineEdit(self.DatosSalida)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trabajoW.sizePolicy().hasHeightForWidth())
        self.trabajoW.setSizePolicy(sizePolicy)
        self.trabajoW.setObjectName("trabajoW")
        self.horizontalLayout_3.addWidget(self.trabajoW)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.matrixButton = QtGui.QPushButton(self.DatosSalida)
        self.matrixButton.setObjectName("matrixButton")
        self.verticalLayout_2.addWidget(self.matrixButton)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_21 = QtGui.QLabel(self.DatosSalida)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        self.presionMedia = QtGui.QLineEdit(self.DatosSalida)
        self.presionMedia.setObjectName("presionMedia")
        self.horizontalLayout_4.addWidget(self.presionMedia)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtGui.QLabel(self.DatosSalida)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.rendimiento = QtGui.QLineEdit(self.DatosSalida)
        self.rendimiento.setObjectName("rendimiento")
        self.horizontalLayout_5.addWidget(self.rendimiento)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addWidget(self.DatosSalida)
        self.horizontalLayout_21.addLayout(self.verticalLayout_8)

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
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Datos de Entrada</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Formula Química:", None, QtGui.QApplication.UnicodeUTF8))
        self.formula_comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Otra", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">C</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">H</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaO.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaH.setText(QtGui.QApplication.translate("Dialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">+</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">O</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaC.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">C</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">O</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.formulaS.setText(QtGui.QApplication.translate("Dialog", "00.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">% </span><span style=\" font-size:12pt; font-weight:600;\">S</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Relación de mezcla F<span style=\" vertical-align:sub;\">r </span>=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_HVS.setText(QtGui.QApplication.translate("Dialog", "HVS [KJ/kg]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_HVI.setText(QtGui.QApplication.translate("Dialog", "HVI [KJ/kg]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Calor aportado [KJ/kg aire]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Parametros atmosféricos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">1</span>  [Pa] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.presion1.setText(QtGui.QApplication.translate("Dialog", "101325", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">1</span>  [K] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatura1.setText(QtGui.QApplication.translate("Dialog", "293", None, QtGui.QApplication.UnicodeUTF8))
        self.label_temperaturabase.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">b</span> [K] =</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatura_base.setText(QtGui.QApplication.translate("Dialog", "273", None, QtGui.QApplication.UnicodeUTF8))
        self.Altura_Button.setText(QtGui.QApplication.translate("Dialog", "Selecionar Altura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Datos del ciclo:", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_1.setItemText(0, QtGui.QApplication.translate("Dialog", "Theta                         =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_1.setItemText(1, QtGui.QApplication.translate("Dialog", "Relacion de comp.  =", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_1.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_2.setItemText(0, QtGui.QApplication.translate("Dialog", "Temp. max                 =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_2.setItemText(1, QtGui.QApplication.translate("Dialog", "Q                                 =", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_2.setText(QtGui.QApplication.translate("Dialog", "1600", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Post Combustión:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Theta<span style=\" vertical-align:sub;\">1                   </span> = </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.theta1.setText(QtGui.QApplication.translate("Dialog", "1.5", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_3.setItemText(0, QtGui.QApplication.translate("Dialog", "T5                              =", None, QtGui.QApplication.UnicodeUTF8))
        self.selecDatoExtra_3.setItemText(1, QtGui.QApplication.translate("Dialog", "Q 1                            =", None, QtGui.QApplication.UnicodeUTF8))
        self.datoExtra_3.setText(QtGui.QApplication.translate("Dialog", "2500", None, QtGui.QApplication.UnicodeUTF8))
        self.calcular.setText(QtGui.QApplication.translate("Dialog", "Calcular", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotArea.setTabText(self.PlotArea.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Diagrama P-V", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotArea.setTabText(self.PlotArea.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Diagrama T-S (Mollier)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Datos de Salida</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Q<span style=\" vertical-align:sub;\">2 </span>[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Qu<span style=\" vertical-align:sub;\"/>[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>W[KJ/kg aire]=</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matrixButton.setText(QtGui.QApplication.translate("Dialog", "Matriz de Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog", "Presión media [Pa]=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Rendimiento [KJ/kg aire]=", None, QtGui.QApplication.UnicodeUTF8))

