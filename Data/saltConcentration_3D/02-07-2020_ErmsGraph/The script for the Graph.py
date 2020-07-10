import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sp

L_Debye = math.sqrt((sp.R*300*80*sp.epsilon_0)/(2*(sp.e*sp.Avogadro)**2))
Kappa = L_Debye**-1 
Length = 290*10**-9
Diff = 10**-9
Phi = 0.025
Omega = [100, 500, 400*math.pi, 5000]

E_theory = [(i*Phi*(Length*Kappa + 2*math.sqrt(Length*Kappa)))/(math.sqrt(2)*Length*Kappa*(i*Length + 2*Diff*Kappa)) for i in Omega]
E_Numerical = [7.810283419189252, 38.98532325540228, 97.96320586366866, 389.7965881467761]
print(E_theory)

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(Omega, E_theory, 'k--', label=('Theoretical'))
ax.plot(Omega, E_Numerical, 'r', label=('Numerical'))
ax.legend()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel('$\omega$')
ax.set_ylabel('$E_{rms}$ $(V/m)$')