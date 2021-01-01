#!/usr/bin/env python
# coding: utf-8

# # TP 4 : Théorèmes de convergence 3M246 JAFUNO Douba

# # 1 La loi des grands nombres

# In[1]:


from random import random
import matplotlib.pyplot as plt
from math import tan, pi, exp


# In[2]:


# Question 1
N = 10000
 # fonction qui trace les valeurs de Y_n la moyennes des X_n par la LGN
def LGN(X_n):
    somme = 0.
    Y_n = []   
    for i in range(N):
        somme += X_n() 
        Y_n.append( somme/(i+1.) )
    plt.plot(Y_n, 'r')
    


# In[3]:


#Question 2
# Par la loi des grands nombres, on a convergence vers E[U] = 1/2
plt.plot([0,N], [0.5, 0.5], 'r')
for i in range(5):
    LGN(random)
plt.show()


# In[4]:


#Question 3
#fonction de la Loi de Cauchy
def cauchy():
    return tan(pi*random())

for i in range(5):
    LGN(cauchy)
plt.title("LGN Cauchy")
plt.show()
# La suite n'est presque surement pas bornée (car la loi de Cauchy n'est pas intégrable)


# In[5]:


#Question 4
#fonction de la Loi de Pareto de parametre 0.5 
def pareto():
    return random()**-2

for i in range(5):
    LGN(pareto)
plt.show()
# La suite tend vers +oo (car la loi de Pareto de parametre 0.5 est non integrable et positive ) 


# # 2 Le théorème limite central

# In[6]:


#Question5   histogramme de 10000 simulations de S=X1 + . . . + XN, pour N = 1, . . . , 12, o`u les Xi
#sont des variables aléeatoires de loi uniforme sur [2, 3].
#fonction qui renvoie s
def s(N): 
    x = 0.
    for i in range(N):
        x += (2+random())
    return x

for N in range(1,12):
    x = []
    for k in range(10000):
        x.append( s(N) )
    plt.hist(x, bins=5*N, density=True, color=((N-1)/10., 0, (11-N)/10.))
plt.show()


# In[7]:


#Question6
# Histogramme de 10000 simulations de la variable Zn / loi normale 

def Z(N):
    x = 0.
    for i in range(N):
        x += random()
    return (12*N)**0.5 * (x/N - 0.5)


x = [Z(100) for k in range(10000)]
plt.hist(x, density=True, bins=40)
s = [i/100. for i in range(-300, 300)]
plt.plot(s, [exp(-u**2/2)*(2*pi)**-0.5 for u in s], 'r')
plt.show()
       

