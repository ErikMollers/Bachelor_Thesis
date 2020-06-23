import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sp

"constants"
L_Debye = math.sqrt((sp.R*300*80*sp.epsilon_0)/(2*(sp.e*sp.Avogadro)**2))
phi_0 = (sp.e*sp.Avogadro*0.025)/(sp.R*300)

"data"
with open("0.1.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_01 = [float(line.split()[1]) for line in lines]
    an_01 = [float(line.split()[2]) for line in lines]
    cat_01 = [float(line.split()[3]) for line in lines]

with open("1.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_1 = [float(line.split()[1]) for line in lines]
    an_1 = [float(line.split()[2]) for line in lines]
    cat_1 = [float(line.split()[3]) for line in lines]
    
with open("10.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_10 = [float(line.split()[1]) for line in lines]
    an_10 = [float(line.split()[2]) for line in lines]
    cat_10 = [float(line.split()[3]) for line in lines]

with open("30.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_30 = [float(line.split()[1]) for line in lines]
    an_30 = [float(line.split()[2]) for line in lines]
    cat_30 = [float(line.split()[3]) for line in lines]

with open("50.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_50 = [float(line.split()[1]) for line in lines]
    an_50 = [float(line.split()[2]) for line in lines]
    cat_50 = [float(line.split()[3]) for line in lines]
    
with open("100.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_100 = [float(line.split()[1]) for line in lines]
    an_100 = [float(line.split()[2]) for line in lines]
    cat_100 = [float(line.split()[3]) for line in lines]    
    
with open("250.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    phi_250 = [float(line.split()[1]) for line in lines]
    an_250 = [float(line.split()[2]) for line in lines]
    cat_250 = [float(line.split()[3]) for line in lines]

"dimensionless x coordinates"
x = [(i+145e-9)/L_Debye for i in q] 

"dimensionless potentials"
phi_01 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_01]
phi_1 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_1]
phi_10 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_10]
phi_30 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_30]
phi_50 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_50]
phi_100 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_100]
phi_250 = [(sp.e*sp.Avogadro*i)/(sp.R*300) for i in phi_250]

x_left = x[:250]
x_right = x[250:]
x_left_reverse = [i for i in x_left]
x_left_reverse.reverse()

"analyticly derived formulas"
phi_theory_left = [2*math.log((math.exp(phi_0/2)+1+(math.exp(phi_0/2)-1)*math.exp(-i))/(math.exp(phi_0/2)+1-(math.exp(phi_0/2)-1)*math.exp(-i))) for i in x_left]
phi_num_left = phi_250[:250]
phi_theory_right = [2*math.log((math.exp(-phi_0/2)+1+(math.exp(-phi_0/2)-1)*math.exp(-i))/(math.exp(-phi_0/2)+1-(math.exp(-phi_0/2)-1)*math.exp(-i))) for i in x_left_reverse]
phi_num_right = phi_250[250:]

an_theory_left = [math.exp((i*sp.e*sp.Avogadro)/(sp.R*300)) for i in phi_theory_left]
cat_theory_left = [math.exp((-i*sp.e*sp.Avogadro)/(sp.R*300)) for i in phi_theory_left]
an_theory_right = [math.exp((i*sp.e*sp.Avogadro)/(sp.R*300)) for i in phi_theory_right]
cat_theory_right = [math.exp((-i*sp.e*sp.Avogadro)/(sp.R*300)) for i in phi_theory_right]
an_num_left = an_250[:250]
cat_num_left = cat_250[:250]
an_num_right = an_250[250:]
cat_num_right = cat_250[250:]


fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

ax1.plot(x, an_01, 'r', label='t = $0.1 \\tau_D$')
ax1.plot(x, an_1, 'b', label='t = $1 \\tau_D$')
ax1.plot(x, an_10, 'g', label='t = 10 $\\tau_D$')
ax1.plot(x, an_30, 'm', label='t = 30 $\\tau_D$')
ax1.plot(x, an_50, 'c', label='t = 50 $\\tau_D$')
ax1.plot(x, an_100, 'y', label='t = 100 $\\tau_D$')
ax1.plot(x, an_250, 'k--', label='t = 250 $\\tau_D$')
ax1.set_xlabel('$\kappa x$')
ax1.set_ylabel('$c_- / c_0$')
ax1.legend()

ax2.plot(x, cat_01, 'r', label='t = $0.1 \\tau_D$')
ax2.plot(x, cat_1, 'b', label='t = $1 \\tau_D$')
ax2.plot(x, cat_10, 'g', label='t = 10 $\\tau_D$')
ax2.plot(x, cat_30, 'm', label='t = 30 $\\tau_D$')
ax2.plot(x, cat_50, 'c', label='t = 50 $\\tau_D$')
ax2.plot(x, cat_100, 'y', label='t = 100 $\\tau_D$')
ax2.plot(x, cat_250, 'k--', label='t = 250 $\\tau_D$')
ax2.set_xlabel('$\kappa x$')
ax2.set_ylabel('$c_+ / c_0$')
ax2.yaxis.tick_right()
ax2.legend()

fig2, ax = plt.subplots(1, 1, figsize=(8, 8))

ax.plot(x, phi_01, 'r', label='t = $0.1 \\tau_D$')
ax.plot(x, phi_1, 'b', label='t = $1 \\tau_D$')
ax.plot(x, phi_10, 'g', label='t = 10 $\\tau_D$')
ax.plot(x, phi_30, 'm', label='t = 30 $\\tau_D$')
ax.plot(x, phi_50, 'c', label='t = 50 $\\tau_D$')
ax.plot(x, phi_100, 'y', label='t = 100 $\\tau_D$')
ax.plot(x, phi_250, 'k--', label='t = 250 $\\tau_D$')
ax.set_xlabel('$\kappa x$')
ax.set_ylabel('$\\varphi^*$')
ax.legend()

fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,10))

ax1.plot(x_left, an_theory_left, 'r--', label ='Anion analytical')
ax1.plot(x_left, an_num_left, 'r', label = 'Anion numerical')
ax1.plot(x_left, cat_theory_left, 'b--', label='Cation analytical')
ax1.plot(x_left, cat_num_left, 'b', label ='Cation analytical')
ax1.set_xlabel('$\kappa x$')
ax1.set_ylabel('$c_+ / c_0$')
ax1.legend()

ax2.plot(x_right, an_theory_right, 'r--', label ='Analytical')
ax2.set_xlabel('$\kappa x$')
ax2.set_ylabel('$c_+ / c_0$')
ax2.legend()

fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,10))

ax1.plot(x_left, phi_theory_left, 'k--', label = 'Analytical')
ax1.plot(x_left, phi_num_left, 'r', label = 'Numerical')
ax1.set_xlabel('$\kappa x$')
ax1.set_ylabel('$\\varphi^*$')
ax1.legend()

ax2.plot(x_right, phi_theory_right, 'k--', label='Analytical')
ax2.plot(x_right, phi_num_right, 'r', label='Numerical')
ax2.set_xlabel('$\kappa x$')
ax2.set_ylabel('$\\varphi^*$')
ax2.yaxis.tick_right()
ax2.legend()


