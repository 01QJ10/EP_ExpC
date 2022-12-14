# -*- coding: utf-8 -*-
"""Analysis_Magnetic Moment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vtmLZKy0Zy5V0G-2iiUFyRWlE-cReOFQ
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# If you are working on your local editor instead of on Colab, you could skip the below
from google.colab import drive
drive.mount('/content/drive')

# Read the csv into df, if you are working locally, include the local path of your csv file
df = pd.read_csv("/content/drive/MyDrive/Y2S1/PC2193/EP with Zhuming <3/Experiment_C/Magnetic Moment - n=3.csv")
df

I_Loop = df["I_Loop/ A"]
F_avg = df["F_avg/ mN"]
I_HC = df["I_HC/ A"]

T_1 = (0.11) * (F_avg[0:5]/1000)
x_1 = I_Loop[0:5]
T_2 = (0.11) * (F_avg[5:10]/1000)
x_2 = I_Loop[5:10]
T_3 = (0.11) * (F_avg[10:15]/1000)
x_3 = I_Loop[10:15]
T_4 = (0.11) * (F_avg[15:20]/1000)
x_4 = I_Loop[15:20]


# Error
F_1 = df["F_1/ mN"]
F_2 = df["F_2/ mN"]
F_all = np.array([F_1/1000 * 0.11, F_2/1000 * 0.11])
F_std = np.std(F_all, axis=0)
F_std += ((0.05/1000)*0.11)
F_std_1 = F_std[0:5]
F_std_2 = F_std[5:10]
F_std_3 = F_std[10:15]
F_std_4 = F_std[15:20]

# Calculating theoretical values
mu = 1.25663706*10**-6
R = 0.188
N = 154
n = 3
r = ((11.82 + 11.78 + 11.84)/6)/100
A = np.pi*r*r


fig, ax = plt.subplots(figsize = (15, 15), ncols = 2, nrows = 2)

X = np.arange(0.5, 3.0, 0.5)
t_1 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_1*0.5
m_t, c = np.polyfit(X, t_1, 1)
Y = m_t*X + c
ax[0,0].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_1, T_1, 1)
Y = m*x_1 + c
ax[0,0].errorbar(x_1, Y, yerr=F_std_1, fmt = "o-", label = "Experimental value")
ax[0,0].set_title(r"$\vec{T}$ vs $I_{Loop}$ at $I_{HC}$ = 0.5", size = 16)
ax[0,0].set_xlabel(r"$I_{Loop}$/ A", size = 14)
ax[0,0].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[0,0].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


t_2 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_2*1.0
m_t, c = np.polyfit(x_2, t_2, 1)
X = np.arange(0.5, 3.0)
Y = m_t*X + c
ax[0,1].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_2, T_2, 1)
Y = m*x_2 + c
ax[0,1].errorbar(x_2, Y, yerr=F_std_2, fmt = "o-", label = "Experimental value")
ax[0,1].set_title(r"$\vec{T}$ vs $I_{Loop}$ at $I_{HC}$ = 1.0", size = 16)
ax[0,1].set_xlabel(r"$I_{Loop}$/ A", size = 14)
ax[0,1].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[0,1].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)



t_3 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_3*1.5
m_t, c = np.polyfit(x_3, t_3, 1)
X = np.arange(0.5, 3.0)
Y = m_t*X + c
ax[1,0].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_3, T_3, 1)
Y = m*x_3 + c
ax[1,0].errorbar(x_3, Y, yerr=F_std_3, fmt = "o-", label = "Experimental value")
ax[1,0].set_title(r"$\vec{T}$ vs $I_{Loop}$ at $I_{HC}$ = 1.5", size = 16)
ax[1,0].set_xlabel(r"$I_{Loop}$/ A", size = 14)
ax[1,0].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[1,0].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


t_4 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_4*2.0
m_t, c = np.polyfit(x_4, t_4, 1)
X = np.arange(0.5, 3.0)
Y = m_t*X + c
ax[1,1].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_4, T_4, 1)
Y = m*x_4 + c
ax[1,1].errorbar(x_4, Y, yerr=F_std_4, fmt = "o-", label = "Experimental value")
ax[1,1].set_title(r"$\vec{T}$ vs $I_{Loop}$ at $I_{HC}$ = 2.0", size = 16)
ax[1,1].set_xlabel(r"$I_{Loop}$/ A", size = 14)
ax[1,1].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[1,1].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)

plt.style.use("seaborn")
plt.tight_layout()


plt.show()

# Read the csv into df, if you are working locally, include the local path of your csv file
df = pd.read_csv("/content/drive/MyDrive/Y2S1/PC2193/EP with Zhuming <3/Experiment_C/Magnetic Moment - I_HC.csv")
df

I_Loop = df["I_Loop/ A"]
F_avg = df["F_avg/ mN"]
I_HC = df["I_HC/ A"]

T_1 = (0.11) * (F_avg[4:8]/1000)
x_1 = I_HC[4:8]
T_2 = (0.11) * (F_avg[8:12]/1000)
x_2 = I_HC[8:12]
T_3 = (0.11) * (F_avg[12:16]/1000)
x_3 = I_HC[12:16]
T_4 = (0.11) * (F_avg[16:20]/1000)
x_4 = I_HC[16:20]


# Error
F_1 = df["F_1/ mN"]
F_2 = df["F_2/ mN"]
F_all = np.array([F_1/1000 * 0.11, F_2/1000 * 0.11])
F_std = np.std(F_all, axis=0)
F_std += ((0.05/1000)*0.11)
F_std_1 = F_std[4:8]
F_std_2 = F_std[8:12]
F_std_3 = F_std[12:16]
F_std_4 = F_std[16:20]


# Calculating theoretical values
mu = 1.25663706*10**-6
R = 0.188
N = 154
n = 3
r = ((11.82 + 11.78 + 11.84)/6)/100
A = np.pi*r*r


fig, ax = plt.subplots(figsize = (15, 15), ncols = 2, nrows = 2)

X = np.arange(0.5, 2.5, 0.5)
t_1 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_1*1.0
m_t, c = np.polyfit(X, t_1, 1)
Y = m_t*X + c
ax[0,0].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_1, T_1, 1)
Y = m*x_1 + c
ax[0,0].errorbar(x_1, Y, yerr=F_std_1, fmt = "o-", label = "Experimental value")
ax[0,0].set_title(r"$\vec{T}$ vs $I_{HC}$ at $I_{Loop}$ = 1.0", size = 16)
ax[0,0].set_xlabel(r"$I_{Loop}$/ A", size = 14)
ax[0,0].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[0,0].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


t_2 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_2*1.5
m_t, c = np.polyfit(x_2, t_2, 1)
X = np.arange(0.5, 2.5, 0.5)
Y = m_t*X + c
ax[0,1].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_2, T_2, 1)
Y = m*x_2 + c
ax[0,1].errorbar(x_2, Y, yerr=F_std_2, fmt = "o-", label = "Experimental value")
ax[0,1].set_title(r"$\vec{T}$ vs $I_{HC}$ at $I_{Loop}$ = 1.5", size = 16)
ax[0,1].set_xlabel(r"$I_{HC}$/ A", size = 14)
ax[0,1].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[0,1].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)



t_3 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_3*2.0
m_t, c = np.polyfit(x_3, t_3, 1)
X = np.arange(0.5, 2.5, 0.5)
Y = m_t*X + c
ax[1,0].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_3, T_3, 1)
Y = m*x_3 + c
ax[1,0].errorbar(x_3, Y, yerr=F_std_3, fmt = "o-", label = "Experimental value")
ax[1,0].set_title(r"$\vec{T}$ vs $I_{HC}$ at $I_{Loop}$ = 2.0", size = 16)
ax[1,0].set_xlabel(r"$I_{HC}$/ A", size = 14)
ax[1,0].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[1,0].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


t_4 = (8*mu*N/(5*np.sqrt(5)*R))*n*A*x_4*2.5
m_t, c = np.polyfit(x_4, t_4, 1)
X = np.arange(0.5, 2.5, 0.5)
Y = m_t*X + c
ax[1,1].plot(X, Y, label = "Theoretical value")
m, c = np.polyfit(x_4, T_4, 1)
Y = m*x_4 + c
ax[1,1].errorbar(x_4, Y, yerr=F_std_4, fmt = "o-", label = "Experimental value")
ax[1,1].set_title(r"$\vec{T}$ vs $I_{HC}$ at $I_{Loop}$ = 2.5", size = 16)
ax[1,1].set_xlabel(r"$I_{HC}$/ A", size = 14)
ax[1,1].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[1,1].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


plt.show()

# Read the csv into df, if you are working locally, include the local path of your csv file
df = pd.read_csv("/content/drive/MyDrive/Y2S1/PC2193/EP with Zhuming <3/Experiment_C/Magnetic Moment - n.csv")
df

I_Loop = df["I_Loop/ A"]
F_avg = df["F_avg/ mN"]
I_HC = df["I_HC/ A"]

T_1 = (0.11) * (F_avg[0:3]/1000)
T_2 = (0.11) * (F_avg[3:6]/1000)
x = np.array([1, 2, 3])



# Error
F_1 = df["F_1/ mN"]
F_2 = df["F_2/ mN"]
F_all = np.array([F_1/1000 * 0.11, F_2/1000 * 0.11])
F_std = np.std(F_all, axis=0)
F_std += ((0.05/1000)*0.11)
F_std_1 = F_std[0:3]
F_std_2 = F_std[3:6]



# Calculating theoretical values
mu = 1.25663706*10**-6
R = 0.188
N = 154
r_1 = ((11.86 + 11.95 + 11.77)/6)/100
r_2 = ((11.90 + 11.98 + 11.835)/6)/100
r_3 = ((11.82 + 11.78 + 11.84)/6)/100
A_1 = np.pi*r_1*r_1
A_2 = np.pi*r_2*r_2
A_3 = np.pi*r_3*r_3
A = np.array([A_1, A_2, A_3])




fig, ax = plt.subplots(figsize = (18, 10), ncols = 2, nrows = 1)


t_1 = (8*mu*N/(5*np.sqrt(5)*R))*x*A*2.5*1.0
m_t, c = np.polyfit(x, t_1, 1)
Y = m_t*x + c
ax[0].plot(x, Y, label = "Theoretical value")
m, c = np.polyfit(x, T_1, 1)
Y = m*x + c
ax[0].errorbar(x, Y, yerr=F_std_1, fmt = "o-", label = "Experimental value")
ax[0].set_title(r"$\vec{T}$ vs n at $I_{Loop}$ = 2.5 & $I_{HC}$ = 1.0", size = 16)
ax[0].set_xlabel("Number of loop, n", size = 14)
ax[0].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[0].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)


t_2 = (8*mu*N/(5*np.sqrt(5)*R))*x*A*2.5*1.5
m_t, c = np.polyfit(x, t_2, 1)
Y = m_t*x + c
ax[1].plot(x, Y, label = "Theoretical value")
m, c = np.polyfit(x, T_2, 1)
Y = m*x + c
ax[1].errorbar(x, Y, yerr=F_std_2, fmt = "o-", label = "Experimental value")
ax[1].set_title(r"$\vec{T}$ vs n at $I_{Loop}$ = 2.5 & $I_{HC}$ = 1.5", size = 16)
ax[1].set_xlabel("Number of loop, n", size = 14)
ax[1].set_ylabel(r"$\vec{T}$/ Nm", size = 14)
ax[1].legend(loc = "upper left", fontsize = 13)
print((abs(m-m_t)/m_t) * 100)




plt.show()

r_1 = ((11.86 + 11.95 + 11.77)/6)/100
print(r_1)
r_2 = ((11.90 + 11.98 + 11.835)/6)/100
print(r_2)