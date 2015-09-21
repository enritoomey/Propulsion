# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 19:51:24 2014

@author: Enriquito
"""
import numpu as np
R = 287
gamma = 1.4
CP = gamma/(1-gamma)*R
# Datos de entrada
phi = 1.04 # power imput factor
sigma = 0.9 # slip factor
omega = 290 # velocidad de rotación en rev/s
D = 0.5 #m  diametro del rotor
d_e = 0.3 #m diametro externo de entrada
d_i = 0.15 #m diametro interno de entrada
T01 = 295 #K
P01 = 101325 # pa
eta_c = 0.78 # eficiencia isentropica
M = 0.3# Mach a la entrada


#def CompresorCentrifugo():

# flujo masico
T1 = T01/(1+(gamma-1)/2*M**2)
P1 = P01/(1+(gamma-1)/2*M**2)**(gamma/(gamma-1))
rho1 = P1/R/T1;
c1 = M*np.sqrt(R*gamma*T1)
ca = c1 # no hay componente de rotación a la entrada
A = np.pi/4*(d_e**2-d_i**2)
m = rho1*A*ca

# velocidad tangencial de salida U
U = np.pi*D*omega

# T03- Todo el trabajo realizado por el rotor
#       que es igual al cambio de momento angular del
#       fluido, se transforma en aumento de T0.

T03 = T01+sigma*phi*U**2/CP;

#P03 - El aumento de presion total se calcula a partir del aumeto
#      de la temperatura total.

P03 = P01*(1+eta_c*(T03-T01)/T01)**(gamma/(gamma-1))

# Potencia requerida 
Pot = m*(T03-T01)

# calculo de alpha (ángulo alabeo del rotor a la entrada
# para satisfacer incidencia cero del flujo axial)
diametro = np.append(np.arange(d_i,d_e,100),d_e)
alpha = []
for i in diametro:
    alpha = alpha.append(np.arctan(ca/np.pi*i*omega))
    
alpha_i = np.arctan(ca/np.pi*d_i*omega)
alpha_e = np.arctan(ca/np.pi*d_i*omega)

