import FuncionesRedNeuronal
import random, math
from mpmath import mp

X = FuncionesRedNeuronal.loadInPuts() #Valores que serán procesados para la ejecución del programa
y = FuncionesRedNeuronal.loadOutPutsNB() #Resultados de los valores anteriores

#Porcentajes de que ocurra cada uno de los resultados
def prob_prior(clase,y):
    return sum(x==clase for x in y)/len(y)

print("Porcentaje de que el paciente mejore y le den el alta médica:", prob_prior(1,y))
print("Porcentaje de que el paciente muera al llegar:", prob_prior(2,y))
print("Porcentaje de que el paciente sea trasladado a UCI y muera:", prob_prior(3,y))
print("Porcentaje de que el paciente sea trasladado a UCI, se recupere y le den el alta médica:", prob_prior(4,y))

#Probabilidad condicionada con un atributo
def calcRange(ej,atributo,valor):
    res = 0
    if(atributo == 0):
        if(valor[0] <= ej[atributo] and ej[atributo] <= valor[1]):
            res = 1
    return res

def prob_cond(atributo,valor,clase,X,y):
    cuenta_valor_y_clase = sum(calcRange(ej,atributo,valor) and c==clase for ej,c in zip(X,y))
    cuenta_clase = sum(c == clase for c in y)
    return cuenta_valor_y_clase/cuenta_clase

print("Probabilidad de que se recupere un paciente con edad menor a 40:", prob_cond(0,[0,39],1,X,y)) #Probabilidad de que se recupere un paciente con edad menor a 40
print("Probabilidad de que se recupere un paciente con edad mayor o igual a 40 y menor a 60:", prob_cond(0,[40,59],1,X,y)) #Probabilidad de que se recupere un paciente con edad mayor o igual a 40 y menor a 60