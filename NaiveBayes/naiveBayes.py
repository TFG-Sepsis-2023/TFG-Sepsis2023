from mpmath import mp
from collections import defaultdict
import random

def loadInPuts():
    data = []
    with open('./datos/dataNV.csv','r') as f:
        for line in f:
            data.append([float(num) for num in str(line).split(',')])

    return data

def loadOutPutsSurvival(fichero):

    lista = []
    file = open(fichero,'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

#Clase para implementar el método Naive Bayes

class NaiveBayes():
    
    def __init__(self, k=1):
        self.k = k
    
    def entrena(self,X,y):

        # Número de ejemplos y de atributos (o características)       
        n_ejemplos=len(X)
        self.n_atributos=len(X[0])

       # Conteos (los atributos los representamos por su índice)

        self.cuenta_prior=defaultdict(int)
        self.cuenta_cond=defaultdict(int)
        for (ej,clase) in zip(X,y):
            self.cuenta_prior[clase]+=1
            for i,v in enumerate(ej):
                self.cuenta_cond[(i,v,clase)]+=1

       # Lista de clases

        self.clases=list(self.cuenta_prior.keys())

       # Valores distintos en cada atributo (necesario para suavizar)

        self.valores_atributo={c:set() for c in range(self.n_atributos)}
        for i,v,_ in self.cuenta_cond:
            self.valores_atributo[i].add(v)

       # Probabilidades a priori P(clase)

        self.probprior=dict()
        for clase in self.cuenta_prior:
            self.probprior[clase]=self.cuenta_prior[clase]/n_ejemplos
        
        print("Probabilidades que una persona sobreviva o no:", self.probprior)

       # Probabilidades condicionadas P(i=v|clase) [Con suavizado]

        self.probcond=dict()
        for i in range(self.n_atributos):
            for v in self.valores_atributo[i]:
                for clase in self.clases:
                    self.probcond[(i,v,clase)]=((self.cuenta_cond[(i,v,clase)]+self.k)/
                        (self.cuenta_prior[clase]+self.k*len(self.valores_atributo[i])))
    
    def predicción(self,ejemplo):

        if self.probcond is None:
            print("El clasificador debe ser entrenado previamente")

        else:
            res_clases = {}
            max_prob=float("-inf")       
            for clase in self.clases:
                acum_prod=self.probprior[clase]
                for i in range(self.n_atributos):
                    # Multiplicaciones de las probabilidades a priori y condicionadas P(clase)*P(i=v|clase)
                    acum_prod*=self.probcond[(i,ejemplo[i],clase)]
                res_clases[clase] = acum_prod
                if acum_prod>max_prob:
                    max_prob=acum_prod
                    max_clase=clase
            return max_clase,res_clases
