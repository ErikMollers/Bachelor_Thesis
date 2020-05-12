import matplotlib.pyplot as plt
import numpy as np

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.txt") as f:
    lines = f.readlines()
    q = [float(line.split()[0]) for line in lines]
    an_000 = [float(line.split()[1]) for line in lines]
    cat_000 = [float(line.split()[2]) for line in lines]

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.03.txt") as f:
    lines = f.readlines()
    an_003 = [float(line.split()[1]) for line in lines]
    cat_003 = [float(line.split()[2]) for line in lines]

with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.06.txt") as f:
    lines = f.readlines()
    an_006 = [float(line.split()[1]) for line in lines]
    cat_006 = [float(line.split()[2]) for line in lines]
    
with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.09.txt") as f:
    lines = f.readlines()
    an_009 = [float(line.split()[1]) for line in lines]
    cat_009 = [float(line.split()[2]) for line in lines]
    
with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.12.txt") as f:
    lines = f.readlines()
    an_012 = [float(line.split()[1]) for line in lines]
    cat_012 = [float(line.split()[2]) for line in lines]
    
with open("C:/Users/5637171/Bachelor_Thesis/Data/saltConcentration/secondRun_12-05-2020/0.15.txt") as f:
    lines = f.readlines()
    an_015 = [float(line.split()[1]) for line in lines]
    cat_015 = [float(line.split()[2]) for line in lines]
    
x = [i+2e-8 for i in q]

fig1, ax = plt.subplots(3, 2, figsize=(15, 15))
ax1, ax2, ax3, ax4, ax5, ax6 = ax.flatten()

ax1.plot(x, an_000, 'r', label='anion')
ax1.plot(x, cat_000, 'b', label='cation')
ax1.set_title('t = 0.00s')
ax1.set_xlabel('Distance from electrode (nm)')
ax1.set_ylabel('concentration')
ax1.legend()

ax2.plot(x, an_003, 'r', label='anion')
ax2.plot(x, cat_003, 'b', label='cation')
ax2.set_title('t = 0.03s')
ax2.set_xlabel('Distance from electrode (nm)')
ax2.set_ylabel('concentration')
ax2.yaxis.tick_right()
ax2.legend()

ax3.plot(x, an_006, 'r', label='anion')
ax3.plot(x, cat_006, 'b', label='cation')
ax3.set_title('t = 0.06s')
ax3.set_xlabel('Distance from electrode (nm)')
ax3.set_ylabel('concentration')
ax3.legend()

ax4.plot(x, an_009, 'r', label='anion')
ax4.plot(x, cat_009, 'b', label='cation')
ax4.set_title('t = 0.09s')
ax4.set_xlabel('Distance from electrode (nm)')
ax4.set_ylabel('concentration')
ax4.yaxis.tick_right()
ax4.legend()

ax5.plot(x, an_012, 'r', label='anion')
ax5.plot(x, cat_012, 'b', label='cation')
ax5.set_title('t = 0.12s')
ax5.set_xlabel('Distance from electrode (nm)')
ax5.set_ylabel('concentration')
ax5.legend()

ax6.plot(x, an_015, 'r', label='anion')
ax6.plot(x, cat_015, 'b', label='cation')
ax6.set_title('t = 0.15s')
ax6.set_xlabel('Distance from electrode (nm)')
ax6.set_ylabel('concentration')
ax6.yaxis.tick_right()
ax6.legend()




