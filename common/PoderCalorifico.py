# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 10:57:30 2014

@author: Enriquito
"""

def PoderCalorifico(c, h, o, Ps_aux, Fr):
    Ps = Ps_aux/100
    s = (c*12.0107+h*1.008+o*15.9994)/32.065*(Ps/(1-Ps))
    Ptotal = c*12.0107+h*1.008+o*15.9994+s*32.065
    Pc = c*12.0107/Ptotal
    Ph = h*1.008/Ptotal
    Po = o*15.9994/Ptotal
    
    #Calor especifico superior (por kg de Combustible)
    HVS = 8080*Pc+29000*(Ph-Po/8)+2500*Ps
    
    mH2O = 9*1.008*h/Ptotal
    Qlat = 2696.0/5.0
    
    #Calor especifico inferior (por kg de Combustible)
    HVI = HVS - mH2O*Qlat

    lambda_s = 2*15.9994*(c+float(h)/4)/Ptotal/0.236
    Q = Fr*HVI/lambda_s
    
    return 4.184*HVS, 4.184*HVI, 4.184*Q, lambda_s
    
    
    
    
    
    