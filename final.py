import numpy as np
import matplotlib.pyplot as plt

R = 0.0205
Tc = 653
Pc = 145
Vc = 0.00371


#REDLICH-KWONG
a = 0.42748 * (R**2) * (Tc**2.5) / Pc
b = 0.08664 * R * Tc / Pc

#Isotherm
V = np.linspace(b + 0.001, 0.5, 1000)

for i in range(15):
  T = Tc - 30 + i*5
  P = ((R * T) / (V - b)) - (a / ((T**0.5) * V * (V + b)))
  plt.plot(V,P)

plt.ylim(0,400)
plt.show()

#Compressibility Factor
Vz = np.linspace(0.025, 1, 1000)
Tz = Tc
Pz = ((R * Tz) / (Vz - b)) - (a / ((Tz**0.5) * Vz * (Vz + b)))
Z = Pz * Vz / (R * Tz)

#Fugacity Coefficient
A2 = a / ((R**2) * (Tz**2.5))
B = b / (R * Tz)

lnphi = Z - 1 - np.log(Z - (B * Pz)) - (((A2) / B) * (np.log(1 + (B * Pz / Z))))
phi = np.exp(lnphi)

plt.plot(Pz, phi)
plt.show()


#CLAUSIUS
c = 27 * (R**2) * (Tc**3) / (64 * Pc)
d = Vc - (R * Tc / (4 * Pc))
e = (3 * R * Tc / (8 * Pc)) - Vc

#Isotherm
V = np.linspace(-0.01, 0.5, 1000)

for i in range(15):
  T = Tc - 30  + i*5
  P = ((R * T) / (V - d)) - (c / (T * ((V + e)**2)))
  plt.plot(V,P)

plt.show()

#Compressibility Factor
Vz = np.linspace(0.032, 1, 1000)
Tz = Tc
Pz = ((R * T) / (V - d)) - (c / (T * ((V + e)**2)))
Z = Pz * Vz / (R * Tz)

#Fugacity Coefficient

A1 = d * Pz / (R * Tz)
B1 = e * Pz / (R * Tz)
C1 = c * Pz / ((R**2) * (Tz**2.7))

lnphi = (np.log(1 / (Z - A1)) - (C1 / (Z - B1)) + (Z - 1)) 
phi = np.exp(lnphi)

plt.plot(Pz, phi)
plt.show()
