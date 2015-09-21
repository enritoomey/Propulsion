# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 12:08:19 2014

@author: Enriquito
"""

from matplotlib import pyplot as plt
import numpy as np
gamma_aire = 1.4

def adiabatica(v):
    return 1/v**gamma_aire
    
def plotCiclo(puntos):
    presion = []
    temperatura = []
    densidad = []
    volumen = []
    for punto in puntos:
        presion.append(punto[0])
        temperatura.append(punto[1])
        densidad.append(punto[2])
        volumen.append(punto[3])

    v1 = np.append(np.arange(volumen[1],volumen[0],(volumen[0]-volumen[1])/100),volumen[0])
    v2 = np.append(np.arange(volumen[3],volumen[4],(volumen[4]-volumen[3])/100),volumen[4])    
    l1, = plt.plot(v1,presion[1]*volumen[1]**gamma_aire*adiabatica(v1),'r')
    l2, l3, =plt.plot(volumen[1:4],presion[1:4],'r',(volumen[4],volumen[0]),(presion[4],presion[0]),'r')
    l4, =plt.plot(v2,presion[3]*volumen[3]**gamma_aire*adiabatica(v2),'r')
    
    #plt.legend( (l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)
    plt.xlabel('volumen especifico')
    plt.ylabel('ciclo sabathe')
    plt.show()