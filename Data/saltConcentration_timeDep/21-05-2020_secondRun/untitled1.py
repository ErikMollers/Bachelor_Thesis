import matplotlib.pyplot as plt
import numpy as np

with open("0.0025.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    psi_0025 = [float(line.split()[1]) for line in lines]
    an_0025 = [float(line.split()[2]) for line in lines]
    cat_0025 = [float(line.split()[3]) for line in lines]

with open("0.005.txt") as f:
    lines = f.readlines()
    psi_005 = [float(line.split()[1]) for line in lines]
    an_005 = [float(line.split()[2]) for line in lines]
    cat_005 = [float(line.split()[3]) for line in lines]

with open("0.0075.txt") as f:
    lines = f.readlines()
    psi_0075 = [float(line.split()[1]) for line in lines]
    an_0075 = [float(line.split()[2]) for line in lines]
    cat_0075 = [float(line.split()[3]) for line in lines]

with open("0.01.txt") as f:
    lines = f.readlines()
    psi_01 = [float(line.split()[1]) for line in lines]
    an_01 = [float(line.split()[2]) for line in lines]
    cat_01 = [float(line.split()[3]) for line in lines]


    
x = [(i+145e-9)/9.65e-9 for i in q]

fig1, ax = plt.subplots(4, 2, figsize=(15, 25))
ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = ax.flatten()


ax1.plot(x, an_0025, 'r', label='anion')
ax1.plot(x, cat_0025, 'b', label='cation')
ax1.set_title('Ion concentrations at t = $29*L^2/D$ ($sin0.5\pi$)')
ax1.set_xlabel('Distance from electrode in Debye lengths')
ax1.set_ylabel('concentration in mol$/m^3$')
ax1.legend()

ax2.plot(x, psi_0025, 'r')
ax2.set_title('Electric potential at t = $29*L^2/D$ ($sin0.5\pi$)')
ax2.set_xlabel('Distance from electrode in Debye lengths')
ax2.set_ylabel('$\phi$')
ax2.yaxis.tick_right()

ax3.plot(x, an_005, 'r', label='anion')
ax3.plot(x, cat_005, 'b', label='cation')
ax3.set_title('Ion concentrations at t = $58*L^2/D$ ($sin\pi$)')
ax3.set_xlabel('Distance from electrode in Debye lengths')
ax3.set_ylabel('concentration in mol$/m^3$')
ax3.legend()

ax4.plot(x, psi_005, 'r')
ax4.set_title('Electric potential at t = $58*L^2/D$ ($sin\pi$)')
ax4.set_xlabel('Distance from electrode in Debye lengths')
ax4.set_ylabel('$\phi$')
ax4.yaxis.tick_right()

ax5.plot(x, an_0075, 'r', label='anion')
ax5.plot(x, cat_0075, 'b', label='cation')
ax5.set_title('Ion concentrations at t = $87*L^2/D$ ($sin1.5\pi$)')
ax5.set_xlabel('Distance from electrode in Debye lengths')
ax5.set_ylabel('concentration in mol$/m^3$')
ax5.legend()

ax6.plot(x, psi_0075, 'r')
ax6.set_title('Electric potential at t = $87*L^2/D$ ($sin1.5\pi$)')
ax6.set_xlabel('Distance from electrode in Debye lengths')
ax6.set_ylabel('$\phi$')
ax6.yaxis.tick_right()

ax7.plot(x, an_01, 'r', label='anion')
ax7.plot(x, cat_01, 'b', label='cation')
ax7.set_title('Ion concentrations at t = $116*L^2/D$ ($sin2\pi$)')
ax7.set_xlabel('Distance from electrode in Debye lengths')
ax7.set_ylabel('concentration in mol$/m^3$')
ax7.legend()

ax8.plot(x, psi_01, 'r')
ax8.set_title('Electric potential at t = $116*L^2/D$ ($sin2\pi$)')
ax8.set_xlabel('Distance from electrode in Debye lengths')
ax8.set_ylabel('$\phi$')
ax8.yaxis.tick_right()
