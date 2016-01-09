# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 19:33:54 2014

@author: Enriquito
"""
import numpy as np

from excepciones import MayorAUnoError, TemperaturaIncompatibleError, Var2IncompatibleError
R_aire = 287 #J/kg/K
gamma_aire = 1.4
S_ref = 1
Cp = gamma_aire * R_aire / (gamma_aire - 1)
Cv = Cp - R_aire

def CicloSabathe(p1,t1,Q,variableExtra1,valor1,variableExtra2,valor2):
    # punto 1
    rho1 =p1/t1/R_aire
    v1 = 1/rho1
    S1 = S_ref

    #punto 2
    if variableExtra1=='Relacion de comp.':
        r_comp=valor1
        if r_comp <= 1:
            raise MayorAUnoError('r_comp')
        v2 = v1/float(r_comp)
        p2 = p1*r_comp**gamma_aire
        t2 = p2*v2/R_aire

    if variableExtra1 == 'T2':
        t2 = valor1
        if t1 >= t2:
            raise TemperaturaIncompatibleError('T2', t1)
        p2 = p1*(t1/t2)**(gamma_aire/(1-gamma_aire))
        v2 = t2*R_aire/p2
        r_comp = v1/v2

    rho2 = 1/v2
    S2 = S1

    #Punto 3
    # CASO 1
    if variableExtra2=='Alpha':
        alpha = valor2
        if alpha <= 1:
            raise MayorAUnoError('Alpha')
        p3 = alpha*p2
        v3 = v2; rho3 = rho2
        t3 = p3*v3/R_aire
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire / (gamma_aire - 1) * (t3 - t2)
        if Qp>Q:
            alpha_max = ((gamma_aire-1)*Q+t2*R_aire)/p2/v2
            alpha_min = (t3 * R_aire + (Q - Qp) * (gamma_aire - 1) / gamma_aire) / p2 / v1
            if alpha_min < 1:
                alpha_min = 1
            raise Var2IncompatibleError(variableExtra2, alpha_max, alpha_min)
        #punto 3a
        Qv  =Q-Qp
        t3a =t3+Qv/R_aire*(gamma_aire-1)/gamma_aire
        p3a = p3
        v3a =R_aire*t3a/p3a
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)
        # Esta condicion no se deberia cumplir si alpha no supera alpha_max
        if v3a>v1:
            alpha_max = ((gamma_aire - 1) * Q + t2 * R_aire) / p2 / v2
            alpha_min = (t3 * R_aire + (Q - Qp) * (gamma_aire - 1) / gamma_aire) / p2 / v1
            if alpha_min < 1:
                alpha_min = 1
            raise Var2IncompatibleError(variableExtra2, alpha_max, alpha_min)
        rho3a = 1.0/v3a

    # CASO 2
    if variableExtra2 == 'Presion max':
        p3 = valor2
        if p3 <= p2:
            p3_max = ((gamma_aire - 1) * Q + t2 * R_aire) / v2
            p3_min = (t3 * R_aire + Qv * (gamma_aire - 1) / gamma_aire) / v1
            if p3_min < p2:
                p3_min = p2
            raise Var2IncompatibleError(variableExtra2, p3_max, p3_min)
        v3 = v2
        rho3 = rho2
        t3 = p3*v3/R_aire
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2)
        #punto 3a
        Qv  =Q-Qp
        if Qv < 0:
            p3_max = ((gamma_aire - 1) * Q + t2 * R_aire) / v2
            p3_min = (t3 * R_aire + Qv * (gamma_aire - 1) / gamma_aire) / v1
            if p3_min < p2:
                p3_min = p2
            raise Var2IncompatibleError(variableExtra2, p3_max, p3_min)
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire+t3
        p3a = p3
        v3a =R_aire*t3a/p3a; rho3a = 1.0/v3a
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)

    # CASO 3
    if variableExtra2=='Beta':
        beta = valor2
        if beta <= 1:
            beta_min = 1
            beta_max = np.minimum(v1 / v2, Q / (Cp * t2) + 1)
            raise Var2IncompatibleError(variableExtra2, beta_max, beta_min)
        alpha = (Q/t2*(gamma_aire-1)/R_aire+1)/(gamma_aire*(beta-1)+1)
        p3 = alpha*p2
        if p3 <= p2:
            beta_min = 1
            beta_max = np.minimum(v1 / v2, Q / (Cp * t2) + 1)
            raise Var2IncompatibleError(variableExtra2, beta_max, beta_min)
        v3 = v2; rho3 = rho2
        t3 = p3*v3/R_aire
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2)
        #punto 3a
        Qv  =Q-Qp
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire+t3
        p3a = p3
        v3a = R_aire*t3a/p3a
        if v3a >= v1:
            beta_min = 1
            beta_max = np.minimum(v1 / v2, Q / (Cp * t2) + 1)
            raise Var2IncompatibleError(variableExtra2, beta_max, beta_min)
        rho3a = 1.0/v3a
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)

    # CASO 4
    if variableExtra2=='Temp. max':
        t3a = valor2
        t3 = (Cp * t3a - Q - Cv * t2) / R_aire
        if t3 <= t2:  # Tmin
            t3a_max = Q / Cv + t2
            t3a_min = np.maximum(t2 + Q / Cp, (Q + Cv * t2) / (Cp - R_aire * v2 / v1))
            raise Var2IncompatibleError(variableExtra2, t3a_max, t3a_min)
        p3 = p2/t2*t3
        v3 = v2; rho3 = rho2
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2)
        #punto 3a
        Qv = Q - Qp
        if Qv <= 0:  # Tmax
            t3a_max = Q / Cv + t2
            t3a_min = np.minimum(t2 + Q / Cp, (Q + Cv * t2) / (Cp - R_aire * v2 / v1))
            raise Var2IncompatibleError(variableExtra2, t3a_max, t3a_min)
        p3a = p3
        v3a = R_aire * t3a / p3a
        if v3a >= v1:
            t3a_max = Q / Cv + t2
            t3a_min = np.maximum(t2 + Q / Cp, (Q + Cv * t2) / (Cp - R_aire * v2 / v1))
            raise Var2IncompatibleError(variableExtra2, t3a_max, t3a_min)
        rho3a = 1.0/v3a
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)


    # punto 4
    v4 = v1
    rho4 = 1.0/v4
    p4 = p3a*(v3a/v1)**gamma_aire
    t4 = p4*v4/R_aire
    S4 = S3a+gamma_aire*R_aire/(gamma_aire-1)*np.log(t4/t3a)-R_aire*np.log(p4/p3a)

    punto1 =(p1,t1,rho1,v1,S1)
    punto2 =(p2,t2,rho2,v2,S2)
    punto3 =(p3,t3,rho3,v3,S3)
    punto3a =(p3a,t3a,rho3a,v3a,S3a)
    punto4 =(p4,t4,rho4,v4,S4)

    # Calculo del trabajo util, la presión media, y la eficiencia
    Q2 = R_aire/(gamma_aire-1)*(t4-t1) #calor cedido
    Qu = Q-Q2 #calor util
    W = Qu #trabajo
    pmed = W/(v4-v2)
    eta= Qu/Q #rendimiento térmico



    return [punto1,punto2,punto3,punto3a,punto4], [round(Q2/1000,1),round(Qu/1000,1),round(W/1000,1),round(pmed,1),round(eta,3)]
