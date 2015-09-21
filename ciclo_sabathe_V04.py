# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 19:33:54 2014

@author: Enriquito
"""
import numpy as np
R_aire = 287 #J/kg/K
gamma_aire = 1.4
S_ref = 1;

def CicloSabathe(p1,t1,Q,variableExtra1,valor1,variableExtra2,valor2):
    # punto 1
    rho1 =p1/t1/R_aire;
    v1 = 1/rho1;
    S1 = S_ref;

    #punto 2
    if variableExtra1=='Relacion de comp.':
        r_comp=valor1
        v2 = v1/float(r_comp);
        p2 = p1*r_comp**gamma_aire;
        t2 = p2*v2/R_aire;
        print("t2 = ",t2)

    if variableExtra1 == 'T2':
        t2 = valor1
        p2 = p1*(t1/t2)**(gamma_aire/(1-gamma_aire))
        v2 = t2*R_aire/p2
        r_comp = v1/v2
        print("r_comp = ",r_comp)

    rho2 = 1/v2;
    S2 = S1

    #Punto 3
    # CASO 1
if variableExtra2=='Alpha':
        alpha = valor2
        p3 = alpha*p2;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        if Qp>Q:
            alpha_max = ((gamma_aire-1)*Q+t2*R_aire)/p2/v2
            print("Error, alpha no puede ser mayor a: "+str(alpha_max))
            raise
        #punto 3a
        Qv  =Q-Qp;
        t3a =t3+Qv/R_aire*(gamma_aire-1)/gamma_aire;
        p3a = p3;
        v3a =R_aire*t3a/p3a;
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)
        if v3a>v1:
            print("Error, la combinación de relación de compresion"+\
            "calor aportado y alpha es incompatible: v3a="+str(v3a)+" > "+str(v1))
        rho3a = 1.0/v3a;

    # CASO 2
    if variableExtra2=='Presion':
        pmax = valor2
        alpha = pmax/p2;
        print("alpha = ",alpha)
        p3 = pmax;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp;
        if Qv<0:
            print("Los parametros ingresados no son compatibles con el calor aportado por el combustible")
            print("Disminuir Pmax o aumentar T2")
            raise
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire+t3;
        p3a = p3;
        v3a =R_aire*t3a/p3a; rho3a = 1.0/v3a;
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)

    # CASO 3
    if variableExtra2=='Beta':
        beta = valor2
        alpha = (Q/t2*(gamma_aire-1)/R_aire+1)/(gamma_aire*(beta-1)+1);
        print("alpha = ",alpha)
        p3 = alpha*p2;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp;
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire+t3;
        p3a = p3;
        v3a = R_aire*t3a/p3a;
        rho3a = 1.0/v3a;
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)
        if v3a>v1 or v3a<v3:
            print("datos incompatibles")
            raise

    if variableExtra2=='Temp. max':
        tmax = valor2
        t3 = tmax
        p3 = p2/t2*t3;
        if p3 < p2:
            print("datos incompatibles")
            raise
        alpha = p3/p2;
        print("alpha = ",alpha)
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        S3 = S2+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3/t2)-R_aire*np.log(p3/p2)
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp;
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire;
        p3a = p3;
        v3a = p3a/R_aire/t3a;
        rho3a = 1.0/v3a;
        S3a = S3+gamma_aire*R_aire/(gamma_aire-1)*np.log(t3a/t3)-R_aire*np.log(p3a/p3)


    # punto 4
    v4 = v1;
    rho4 = 1.0/v4;
    p4 = p3a*(v3a/v1)**gamma_aire;
    t4 = p4*v4/R_aire;
    S4 = S3a+gamma_aire*R_aire/(gamma_aire-1)*np.log(t4/t3a)-R_aire*np.log(p4/p3a)

    punto1 =(p1,t1,rho1,v1,S1)
    punto2 =(p2,t2,rho2,v2,S2)
    punto3 =(p3,t3,rho3,v3,S3)
    punto3a =(p3a,t3a,rho3a,v3a,S3a)
    punto4 =(p4,t4,rho4,v4,S4)

    # Calculo del trabajo util, la presión media, y la eficiencia
    Q2 = R_aire/(gamma_aire-1)*(t4-t1) #calor cedido
    Qu = Q-Q2; #calor util
    W = Qu; #trabajo
    pmed = W/(v4-v2);
    eta= Qu/Q #rendimiento térmico



    return [punto1,punto2,punto3,punto3a,punto4], [round(Q2/1000,1),round(Qu/1000,1),round(W/1000,1),round(pmed,1),round(eta,3)]
