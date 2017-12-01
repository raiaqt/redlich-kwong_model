import numpy as np
import matplotlib.pyplot as plt

R = 0.0205
Tc = 653
Pc = 145
Vc = 0.00371
T = 700

a = 27 * (R**2) * (Tc**3) / (64 * Pc)
b = Vc - (R * Tc / (4 * Pc))
c = (3 * R * Tc / (8 * Pc)) - Vc

V = np.linspace(-0.01, 0.4, 1000)

for i in range(15):
  T = Tc - 30  + i*5
  P = ((R * T) / (V - b)) - (a / (T * ((V + c)**2)))
  plt.plot(V,P)

plt.show()
