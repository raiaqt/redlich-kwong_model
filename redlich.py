
import numpy as np
import matplotlib.pyplot as plt

R = 0.08205

#ammonia
#Tc = 405.5
#Pc = 111.3

#ethanol
#Tc = 514 
#Pc = 62.18

#ethanol
Tc = 647.1
Pc = 217.7

a = 0.42748 * (R**2) * (Tc**2.5) / Pc
b = 0.08664 * R * Tc / Pc

V = np.arange(b + 0.001, 0.1, 0.00001)

for i in range(20):
  T = Tc - 400 + i*40
  P = ((R * T) / (V - b)) - (a / ((T**0.5) * V * (V + b))) 
  plt.plot(V,P)

#plt.ylim(-500, 4000)
plt.show()

