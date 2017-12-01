import numpy as np
import matplotlib.pyplot as plt

R = 0.0205
Tc = 653
Pc = 145
Vc = 0.00371
T = 700


#Redlich Isotherm
a = 0.42748 * (R**2) * (Tc**2.5) / Pc
b = 0.08664 * R * Tc / Pc
V = np.linspace(b + 0.001, 0.4, 1000)

for i in range(15):
  T = Tc - 30 + i*5
  P = ((R * T) / (V - b)) - (a / ((T**0.5) * V * (V + b)))
  plt.plot(V,P)

plt.ylim(0,400)
plt.show()


#Redlich Fugacity Coefficient
V = np.linspace(b + 0.001, 0.4, 1000)
A2 = a / ((R**2) * (T**2.5))
B = b / (R * T)
h = b / V

Z = (1 / (1 - h)) - ((A2 / B) * (h / (1 + h)))
lnphi = Z - 1 - np.log(Z - (B * P)) - (((A2) / B) * (np.log(1 + (B * P / Z))))
phi = np.exp(lnphi)

plt.xlim(0, 700)
plt.ylim(0, 1)
plt.plot(P,phi)
plt.show()

#Clausius
a = 27 * (R**2) * (Tc**3) / (64 * Pc)
b = Vc - (R * Tc / (4 * Pc))
c = (3 * R * Tc / (8 * Pc)) - Vc
V = np.linspace(-0.01, 0.4, 1000)

for i in range(15):
  T = Tc - 30  + i*5
  P = ((R * T) / (V - b)) - (a / (T * ((V + c)**2)))
  plt.plot(V,P)

plt.ylim(0,400)
plt.show()


