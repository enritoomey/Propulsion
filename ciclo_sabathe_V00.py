# -*- coding: utf-8 -*-
"""
Programación Ciclo Sabathe
Created on Wed Aug 20 19:52:23 2014

@author: Enriquito

"""
from PoderCalorifico import PoderCalorifico

# Constantes
R_aire = 287 #J/kg/K
gamma_aire = 1.4

# Variables de Entrada Fijas
p1 = 64341.3;
t1 = 318.15;
r_comp = 9.5;
# Definir 2 de las siguientes 3 variables. La otra se define a partir de las
# otras 2.

# El calor se calcula con la función poder calorifico, ingresando como dato de 
# entrada la formula quimica del combustible (C,H,O,S), y la relación de mezcla
# relativa Fr (pobre<Fr=1<rica).
c = 7;
h = 15;
o = 0;
s = 0;
Fr = 1;
HVS,HVS,Q=PoderCalorifico(c,h,o,s,Fr)


# Falta un dato de entrada mas que puede ser alpha, beta o pmax.

alpha =6.34;#Relación de presión
pmax = p1*6.34;
beta =1;#

def Ciclo_Sabathe(p1,t1,r_comp,Q,alpha=(),beta=(),pmax=()):
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
p3 = alpha*p2;
v3 = v2; rho3 = rho2;
t3 = p3*v3/R_aire;
Qp = R_aire/(gamma_aire-1)*(t3-t2);
#punto 3a
Qv  =Q-Qp; 
t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire;
p3 = p3a;
v3a = p3a/R_aire/t3a; rho3a = 1/v3a;

# CASO 2
p3 = alpha*p2;
v3 = v2; rho3 = rho2;
t3 = p3*v3/R_aire;
Qp = R_aire/(gamma_aire-1)*(t3-t2);
Qv = R_aire*gamma_aire/(gamma_aire-1)*t3*(beta-1);
Q = Qv+Qp;
##punto 3a
t3a = Qv/R_aire*(gamma_aire-1)/gamma_aire;
p3 = p3a;
v3a = p3a/R_aire/t3a; rho3a = 1/v3a;

# CASO 3
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
rho3a = 1/v3a;

# punto 4
v4 = v1;
p4 = p3a*(v3a/v1)**gamma_aire;
t4 = p4*v4/R_aire;














