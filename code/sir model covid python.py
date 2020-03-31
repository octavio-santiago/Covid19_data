# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:12:23 2020

@author: BRAEUED1
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 4000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 136, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


res = [136,152,164,240,286,396,459,631,745,810,862,1052]
# A grid of time points (in days)
t = np.linspace(0, 160, 160)
# Initial conditions vector
y0 = S0, I0, R0
erro_min = 1000000
x_min = 0
for x in np.arange(3., 9., 0.1):
    # Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
    beta, gamma = 0.2, 1./10 
    beta, gamma = 1./6.5, 1./14 
    beta, gamma = 1./x, 1./14 
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    erro = np.mean(abs(I[0:len(res)] - res))
    if erro < erro_min:
        erro_min = erro
        x_min = x

beta, gamma = 1./x_min, 1./14
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,N/1000)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

plt.scatter(I[0:len(res)],res)
plt.show()