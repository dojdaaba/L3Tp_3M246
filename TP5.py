#!/usr/bin/env python
# coding: utf-8

# # TP 5 : Estimation et méthode de Monte Carlo 3M246 JAFUNO Douba

# In[1]:


from random import random, gauss
from math import sin, pi, cos


# # 1 Estimation de la moyenne d’une variable

# In[2]:


#écrire un programme qui calcule un intervalle de confiance pour
#la moyenne de la variable considérée. Pour écrire le programme, on donnera une valeur arbitraire à la
#moyenne, et on calculera l’intervalle de confiance comme si la moyenne ´etait inconnue.
#Pour chaque exemple, on calculera 1000 intervalles de confiance, et on comptera parmi ces derniers
#combien contenaient effectivement la valeur théorique.


# In[3]:


# cas d’une variable X de loi N (m, 1) o`u m est inconnu.

m = 1.5 #  valeur de m pour l'ic 

def IC_N_m_1(N):
    moy = sum([gauss(m,1) for i in range(N)]) / N 
    largeur = 1.96 * N**-0.5
    return moy-largeur , moy+largeur



print("Valeur theorique :", m)

a,b = IC_N_m_1(1000)
print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (1000,a,b))

N_IC = 1000 # Nb d'intervalles de confiance calcules
N = 100 # Nb de variables pour calculer un ic
nb_succes = 0
for i in range(N_IC):
    a,b = IC_N_m_1(N)
    if a<m<b:
        nb_succes += 1
        
#compter parmi ces derniers combien contenaient effectivement la valeur théorique.
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))


# In[4]:


#cas variables de loi B(p), avec p fixe, mais inconnu.

p = 0.23 #  valeur de p pour l'ic

def bernoulli():
    if random()<p:
        return 1
    else:
        return 0

def IC_b(N):
    moy = sum([bernoulli() for i in range(N)]) / float(N) 
    largeur = 1.96 * N**-0.5 / 2
    return moy-largeur , moy+largeur

print("Valeur theorique : ", p)
for N in [100, 1000, 10000]:
    a,b = IC_b(N)
    print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (N,a,b))


nb_succes = 0
for i in range(N_IC):
    a,b = IC_b(N)
    if a<p<b:
        nb_succes += 1
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))


# In[5]:


#variables de loi N(m,sigma^2), avec m et sigma fixes, mais inconnus On cherche m.

m = -2.9
sigma2 = 3.7

def IC_N_m_s(N):
    X = [gauss(m,sigma2) for i in range(N)]
    moy = sum(X) / N 
    moy_carres = sum([x**2 for x in X])/N 
    s2_n = moy_carres - moy**2
    largeur = 1.96 * (s2_n/N)**0.5 
    return moy-largeur , moy+largeur


print("Valeur theorique : ", m)
for N in [100, 1000, 10000]:
    a,b = IC_N_m_s(N)
    print("Intervalle de confiance pour %d simulations : [ %f , %f ]" % (N,a,b))


nb_succes = 0
for i in range(N_IC):
    a,b = IC_N_m_s(N)
    if a<m<b:
        nb_succes += 1
print("Sur %d intervalles de confiance calcules avec %d variables, %f%% contenaient la valeur theorique." % (N_IC, N, nb_succes*N/float(N_IC)))


# # 2 Influence de la variance

# In[6]:



## MC integrale de I=cos(x)/x^1/3 sur [0,1]

N = 1000 # Nombre de simulation


## Fct qui calcule I 
def f(x):
    return cos(x) * x**-(1.0/3)

simus = [f(random()) for i in range(N)] # Les sim des f(U).

moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2
print("Intervalle de confiance 1 [ %f , %f ]" % (moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5)) 


# In[7]:


## Deuxieme methode 

def g(x):
    return 1.5*cos(x)

simus = [g(random()**1.5) for i in range(N)] 

moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2 
print("Intervalle de confiance 2 :[ %f , %f ]" % (moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5))


# # 3 Robustesse de la méthode

# In[8]:


#Estimation du volume de la boule unite en dimension 10
from math import gamma

d = 10 # La dimension

# fct qui renvoie une loi uniforme sur [-1,1]^d.
def X():
    return [2*random()-1 for i in range(d)]

def bd(x):
    if sum([t**2 for t in x])<1:
        return 2.**d # Volume de [-1,1]^d
    else:
        return 0

N= 1000000 # Nb de simulations

simus = [bd(X()) for i in range(N)]

moy = sum(simus)/N
var = sum(s**2 for s in simus)/N - moy**2

print("Valeur theorique : ", (pi**(0.5*d)/gamma(0.5*d+1)))


print("Intervalle de confiance construit a partir de %d simulations." % N)
print([moy - 1.96*(var/N)**0.5 , moy + 1.96*(var/N)**0.5])

