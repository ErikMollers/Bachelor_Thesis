import matplotlib.pyplot as plt
import numpy as np
import math

"Importing the data"
E1 = np.loadtxt('1.txt', skiprows=250, usecols=3, max_rows=1)
E2 = np.loadtxt('2.txt', skiprows=250, usecols=3, max_rows=1)
E3 = np.loadtxt('3.txt', skiprows=250, usecols=3, max_rows=1)
E4 = np.loadtxt('4.txt', skiprows=250, usecols=3, max_rows=1)
E5 = np.loadtxt('5.txt', skiprows=250, usecols=3, max_rows=1)
E6 = np.loadtxt('6.txt', skiprows=250, usecols=3, max_rows=1)
E7 = np.loadtxt('7.txt', skiprows=250, usecols=3, max_rows=1)
E8 = np.loadtxt('8.txt', skiprows=250, usecols=3, max_rows=1)
E9 = np.loadtxt('9.txt', skiprows=250, usecols=3, max_rows=1)
E10 = np.loadtxt('10.txt', skiprows=250, usecols=3, max_rows=1)

"calculating the rms of different amount of discrete timesteps"
E_rms = math.sqrt((E1**2 + E2**2 + E3**2 + E4**2 + E5**2 + E6**2 + E7**2 + E8**2 + E9**2 + E10**2)/10)

print("the root mean square =", E_rms)


