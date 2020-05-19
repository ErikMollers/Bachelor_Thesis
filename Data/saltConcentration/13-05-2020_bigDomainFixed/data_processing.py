import matplotlib.pyplot as plt
import numpy as np

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/13-05-2020_bigDomainFixed/0.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    an_000 = [float(line.split()[1]) for line in lines]
    cat_000 = [float(line.split()[2]) for line in lines]

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/13-05-2020_bigDomainFixed/0.03.txt") as f:
    lines = f.readlines()
    an_003 = [float(line.split()[1]) for line in lines]
    cat_003 = [float(line.split()[2]) for line in lines]

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/13-05-2020_bigDomainFixed/0.06.txt") as f:
    lines = f.readlines()
    an_006 = [float(line.split()[1]) for line in lines]
    cat_006 = [float(line.split()[2]) for line in lines]
    
with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/13-05-2020_bigDomainFixed/0.09.txt") as f:
    lines = f.readlines()
    an_009 = [float(line.split()[1]) for line in lines]
    cat_009 = [float(line.split()[2]) for line in lines]
    
    
x = [(i+2e-6)/9.905e-7 for i in q]

fig1, ax = plt.subplots(2, 2, figsize=(10, 10))
ax1, ax2, ax3, ax4 = ax.flatten()

ax1.plot(x, an_000, 'r', label='anion')
ax1.plot(x, cat_000, 'b', label='cation')
ax1.set_title('t = 0')
ax1.set_xlabel('Distance from electrode in Debye lengths')
ax1.set_ylabel('concentration')
ax1.legend()

ax2.plot(x, an_003, 'r', label='anion')
ax2.plot(x, cat_003, 'b', label='cation')
ax2.set_title('t = $1.875*L^2/D$')
ax2.set_xlabel('Distance from electrode in Debye lengths')
ax2.set_ylabel('concentration')
ax2.yaxis.tick_right()
ax2.legend()

ax3.plot(x, an_006, 'r', label='anion')
ax3.plot(x, cat_006, 'b', label='cation')
ax3.set_title('t = $3.75*L^2/D$')
ax3.set_xlabel('Distance from electrode in Debye lengths')
ax3.set_ylabel('concentration')
ax3.legend()

ax4.plot(x, an_009, 'r', label='anion')
ax4.plot(x, cat_009, 'b', label='cation')
ax4.set_title('t = $5.625*L^2/D$')
ax4.set_xlabel('Distance from electrode in Debye lengths')
ax4.set_ylabel('concentration')
ax4.yaxis.tick_right()
ax4.legend()


