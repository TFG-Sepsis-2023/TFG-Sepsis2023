### IMPORTS

import random, math
from mpmath import mp


### CALCULO REDES DE SALIDA

def sigmoide(x):
    
    return (1/(1+mp.exp(-x)))

def relu(x):
    return max(0,x)

def umbral(x):
    return 1 if x>0 else 0

def tanh(x):
    return 2*sigmoide(2*x)-1

### SOFTMAX

def softmax(l):
    
    lexp=[mp.exp(x) for x in l]
    deno=sum(lexp)
    return [e/deno for e in lexp]

### DERIVADAS

def DerivadaSigmoide(x):
    return x*(1-x)

def DerivadaRelu(x):
    return 1 if x>0 else 0

### AUXILIAR 

def loadOutPuts():

    lista = []
    file = open("./outputs/outcome4OUTPUTS.txt",'r')
    
    for line in file:
        line = line[:-1].split(',')
        lista.append(list(int(num) for num in line))

    return lista

def loadInPuts():
    lista = []
    
    with open("./datos/data.csv",'r') as f:
        next(f)
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')][:23])

    return lista