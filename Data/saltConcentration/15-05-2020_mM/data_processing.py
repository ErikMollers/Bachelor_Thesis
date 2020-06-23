import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sp

with open("0.03.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_003 = [float(line.split()[1]) for line in lines]
    an_003 = [float(line.split()[2]) for line in lines]
    cat_003 = [float(line.split()[3]) for line in lines]

    
x = [(i+145e-9)/9.74e-9 for i in q]
phi_0 = (sp.e*sp.Avogadro*0.025)/(sp.R*300)


phi_theory = [(sp.R*300*2)*math.log((math.exp(phi_0/2)+1+(math.exp(phi_0/2)-1)*math.exp(-i))/(math.exp(phi_0/2)+1-(math.exp(phi_0/2)-1)*math.exp(-i)))/(sp.e*sp.Avogadro) for i in x]


fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

ax1.plot(x, an_003, 'r', label='anion')
ax1.plot(x, cat_003, 'b', label='cation')
ax1.set_title('Ion concentrations at t = $350*L^2/D$')
ax1.set_xlabel('Distance from electrode in Debye lengths')
ax1.set_ylabel('concentration in mol$/m^3$')
ax1.legend()

ax2.plot(x, phi_theory, 'bo', label='theorethical')
ax2.plot(x, phi_003, 'r', label='simulated')
ax2.set_title('Electric potential at t = $350*L^2/D$')
ax2.set_xlabel('Distance from electrode in Debye lengths')
ax2.set_ylabel('$\phi$')
ax2.yaxis.tick_right()
ax2.legend()


