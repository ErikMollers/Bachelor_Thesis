import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sp

L_Debye = math.sqrt((sp.R*300*80*sp.epsilon_0)/(2*(sp.e*sp.Avogadro)**2))
Kappa = L_Debye**-1 
Length = 290*10**-9
Diff = 10**-9
Phi = 0.025
Omega = [100, 1000, 10000, 100000, 1300000]

E_theory = [(i*Phi*(Length*Kappa + 2*math.sqrt(Length*Kappa)))/(math.sqrt(2)*Length*Kappa*(i*Length + 2*Diff*Kappa)) for i in Omega]

print(E_theory)