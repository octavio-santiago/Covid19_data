# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:12:23 2020

@author: BRAEUED1
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 32700000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 100, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


res = [100,124,158,221,319,435,541,704,994,1301,1697,2247,2943,3680,4663,6411,9259,13789,19383,
       24207,33546,42751,54881,64775,82179,103729,119682]
# A grid of time points (in days)
t = np.linspace(0, 160, 160)
# Initial conditions vector
y0 = S0, I0, R0

def calculate(res,t,y0):
    erro_min = 100000000
    x_min = 2.
    for x in np.arange(2., 6., 0.1):
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
    return S,I,R,x_min,erro_min

S,I,R,x_min,erro_min = calculate(res,t,y0)
spike = list(I).index(max(I))
spike_val = max(I)
print('O pico será em: ', spike - len(res), " dias")
print('Com aproximadamene ', round(spike_val,0), " infectados notificados")
print('E aproximadamene ', 0.02 * round(spike_val,0), " mortos")

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
plt.plot(res,res,'r')
plt.show()

plt.plot(range(0, len(res)), [x/1000 for x in res], 'b',alpha=0.5, lw=2, label='Real cases')
plt.plot(t[0:len(res)], I[0:len(res)]/1000, 'r',alpha=0.5, lw=2, label='Predicted cases')

plt.show()

# plot prediction with real cases
extend = len(t[len(res):])
import random
t_list = random.sample(range(10, 300), extend)
t_list = [np.nan for x in t_list]
res_new = res.copy()
res_new.extend(t_list)
plt.plot(t, I, 'r',alpha=0.5, lw=2, label='Predicted cases')
plt.plot(t, res_new, 'b',alpha=0.5, lw=2, label='Real cases')

plt.show()

# plot prediction with real cases
extend = len(t[len(res):])
import random
t_list = random.sample(range(10, 300), extend)
t_list = [np.nan for x in t_list]
res_new = res.copy()
res_new.extend(t_list)
plt.plot(t, I, 'r',alpha=0.5, lw=2, label='Predicted cases')
plt.plot(t, res_new, 'b',alpha=0.5, lw=2, label='Real cases')

plt.show()

#evolution of infection rate
cases = []
errors = []
x_mins = []
res_y = res.copy()
for i in range(5,len(res),5):
    print(res_y[0:i])
    S,I,R,x_min,erro_min = calculate(res_y[0:i],t,y0)
    cases.append(I)
    errors.append(erro_min)
    x_mins.append(x_min)
    if i >= (len(res)-5):
        plt.plot(t, I,'b', alpha=1, lw=2, label='Predicted cases')
    else:
        plt.plot(t, I,'r',alpha=0.5, lw=2, label='Predicted cases')

plt.show()
'''
#plot curves for multiple scenarios
beta, gamma = 1./x_min, 1./g
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
#fig = plt.figure(facecolor='w')
#ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
#ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, alpha=0.5, lw=2, label='Infected')
#ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,N/1000)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
    

plt.show()'''
