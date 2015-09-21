# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 19:33:54 2014

@author: Enriquito
"""

R_aire = 287 #J/kg/K
gamma_aire = 1.4

def CicloSabathe(p1,t1,r_comp,Q,alpha=(),pmax=(),beta=()):
    # punto 1
    rho1 =p1/t1/R_aire; 
    v1 = 1/rho1;
    
    #punto 2
    v2 = v1/r_comp;
    rho2 = 1/v2;
    p2 = p1*r_comp**gamma_aire;
    t2 = p2*v2/R_aire;
    
    #Punto 3
    # CASO 1
    if alpha:
        p3 = alpha*p2;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp; 
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire;
        p3a = p3;
        v3a = p3a/R_aire/t3a; rho3a = 1.0/v3a;
    
    # CASO 2    
    if pmax:
        alpha = pmax/p1;
        p3 = pmax;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp; 
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire;
        p3a = p3;
        v3a = p3a/R_aire/t3a; rho3a = 1.0/v3a;
    
    # CASO 3    
    if beta:
        alpha = (Q/t2*(gamma_aire-1)/R_aire+1)/(gamma_aire*(beta-1)+1);
        p3 = alpha*p2;
        v3 = v2; rho3 = rho2;
        t3 = p3*v3/R_aire;
        Qp = R_aire/(gamma_aire-1)*(t3-t2);
        #punto 3a
        Qv  =Q-Qp; 
        t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire+t3;
        p3a = p3;
        v3a = R_aire*t3a/p3a; 
        rho3a = 1.0/v3a;

    # punto 4
    v4 = v1;
    rho4 = 1.0/v4;
    p4 = p3a*(v3a/v1)**gamma_aire;
    t4 = p4*v4/R_aire;

    punto1 =(p1,t1,rho1,v1)
    punto2 =(p2,t2,rho2,v2)
    punto3 =(p3,t3,rho3,v3)
    punto3a =(p3a,t3a,rho3a,v3a)
    punto4 =(p4,t4,rho4,v4)
    
    # Calculo del trabajo util, la presión media, y la eficiencia
    
    
    return [punto1,punto2,punto3,punto3a,punto4]

         
        