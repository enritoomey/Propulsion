# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 20:09:24 2014

@author: Enriquito
"""
from numpy import log as log
from excepciones import MayorAUnoError,TemperaturaIncompatibleError

r_aire = 287.0 #J/kg/K
gamma_aire = 1.4
cp = gamma_aire*r_aire/(gamma_aire-1)

def CicloJouleBraytonSimple(p1,t1,tb,variable1,dato1,variable2,dato2):
    
    #punto 1
    v1 = r_aire*t1/p1
    rho1=1/v1
    s1 = r_aire/(gamma_aire-1)*log(t1/tb)

    if variable1 == 'Relacion de comp.':
        r_comp = dato1
        if r_comp <= 1:
            raise MayorAUnoError('r_comp')
        theta = r_comp**((gamma_aire-1)/gamma_aire)

    if variable1 == 'Theta':
        theta = dato1
        if theta <= 1:
            raise MayorAUnoError('theta')

    if variable2 == 'Temp. max':
        t3 = dato2
        Q = cp*(t3-theta*t1)
        if Q<0:
            raise TemperaturaIncompatibleError('t3',theta*t1)
        
    if variable2 == 'Q':
        Q = dato2*1000
        t3 = theta*t1+Q/cp
           
    #punto 2
    t2 = theta*t1
    v2 = v1/theta**(1/(gamma_aire-1))
    rho2 = 1/v2
    p2 = r_aire*t2/v2
    s2 = s1 #proceso isoentropico
    
    #punto 3
    p3 = p2
    v3 = t3*r_aire/p3
    rho3 = 1/v3
    s3 = cp*log(t3/t2)+s2
    
    #punto 4
    p4 = p1
    t4 = t3/theta
    v4 = t4*r_aire/p4
    rho4 = 1/v4
    s4 = s3
    
    # Calor util, trabajo, presion media, rendimiento
    Q2 = r_aire/(gamma_aire-1)*(t4-t1) #calor cedido
    Qu = Q-Q2 #calor util
    W = Qu #trabajo
    pmed = W/(v4-v2)
    eta= Qu/Q #rendimiento

    # Datos de salida
    punto1 =(p1,t1,rho1,v1,s1)
    punto2 =(p2,t2,rho2,v2,s2)
    punto3 =(p3,t3,rho3,v3,s3)
    punto4 =(p4,t4,rho4,v4,s4)

    return [punto1,punto2,punto3,punto4], [round(Q,1),round(Q2,1),round(Qu,1),round(W,1),round(pmed,1),round(eta,3)]


def CicloJouleBraytonPostcombustion(p1,t1,tb,theta1,variable1,dato1,variable2,dato2,variable3,dato3):


    if theta1 <= 1:
        raise MayorAUnoError('theta1')
    #punto 1
    v1 = r_aire*t1/p1
    rho1=1/v1
    s1 = r_aire/(gamma_aire-1)*log(t1/tb)

    if variable1 == 'Relacion de comp.':
        r_comp = dato1
        if r_comp <= 1:
            raise MayorAUnoError('r_comp')
        theta = r_comp**((gamma_aire-1)/gamma_aire)



    if variable1 == 'Theta':
        theta = dato1
        if theta <= 1:
            raise MayorAUnoError('theta')

    if variable2 == 'Temp. max':
        t3 = dato2
        Q = cp*(t3-theta*t1)
        if Q<0:
            raise TemperaturaIncompatibleError('t3',theta*t1)

    if variable2 == 'Q':
        Q = dato2*1000
        t3 = theta*t1+Q/cp

    if variable3 == 'T5':
        t5 = dato3
        Q1 = cp*(t5-t3/theta1)
        if Q1<0:
            raise TemperaturaIncompatibleError('t5',t3/theta1)

    if variable3 == 'Q1':
        Q1 = dato3*1000
        t5 = t3/theta1+Q1/cp

    #punto 2
    t2 = theta*t1
    v2 = v1/theta**(1/(gamma_aire-1))
    rho2 = 1/v2
    p2 = r_aire*t2/v2
    s2 = s1 #proceso isoentropico

    #punto 3
    p3 = p2
    v3 = t3*r_aire/p3
    rho3 = 1/v3
    s3 = cp*log(t3/t2)+s2

    #punto 4
    t4 = t3/theta1
    p4 = p3 * theta1**(gamma_aire/(1-gamma_aire))
    v4 = t4*r_aire/p4
    rho4 = 1/v4
    s4 = s3

    # punto 5
    p5 = p4
    v5 = t5*r_aire/p5
    rho5 = 1/v5
    s5 = s4+cp*log(t5/t4)

    # punto 6
    p6 = p1
    t6 = t5*(p5/p6)**((1-gamma_aire)/gamma_aire)
    v6 = t6*r_aire/p6
    rho6 = 1/v6
    s6 = s5

# Correguir esta sección para considerar el trabajo extra realizado en la post-combustión
    # Calor util, trabajo, presion media, rendimiento
    Q2 = cp*(t6-t1); #calor cedido
    Qu = Q+Q1-Q2; #calor util
    W = Qu; #trabajo
    pmed = W/(v6-v2);
    eta= Qu/(Q+Q1) #rendimiento

    # Datos de salida
    punto1 =(p1,t1,rho1,v1,s1)
    punto2 =(p2,t2,rho2,v2,s2)
    punto3 =(p3,t3,rho3,v3,s3)
    punto4 =(p4,t4,rho4,v4,s4)
    punto5 =(p5,t5,rho5,v5,s5)
    punto6 =(p6,t6,rho6,v6,s6)

    return [punto1,punto2,punto3,punto4,punto5,punto6], [round(Q,1),round(Q2,1),round(Qu,1),round(W,1),round(pmed,1),round(eta,3)]
