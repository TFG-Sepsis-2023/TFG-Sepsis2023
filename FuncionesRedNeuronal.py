### IMPORTS

import random, math

### CALCULO REDES DE SALIDA

def sigmoide(x):
    return (1/(1+math.exp(-x)))

def relu(x):
    return max(0,x)

def umbral(x):
    return 1 if x>0 else 0

def tanh(x):
    return 2*sigmoide(2*x)-1

### SOFTMAX

def softmax(l):
    lexp=[math.exp(x) for x in l]
    deno=sum(lexp)
    return [e/deno for e in lexp]