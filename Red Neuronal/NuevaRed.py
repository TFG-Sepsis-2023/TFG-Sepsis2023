import random
from mpmath import mp

class RedNeuronal():

    def __init__(self,capas=[]):

        self.capas = capas

        

    def crea(self,initial,hidden,final):

        # Creación de nodos

        initial_nodes = [Nodo(w0=random.uniform(-1,1),w=[],ini=0,a=0,error=0)]
        
        hiden_nodes = [Nodo(w0=random.uniform(-1,1),w=[random.uniform(-1,1) for _ in range(initial)],ini=0,a=0,error=0) for _ in range(hidden)]

        final_nodes = [Nodo(w0=random.uniform(-1,1),w=[random.uniform(-1,1) for _ in range(hidden)],ini=0,a=0,error=0) for _ in range(final)]

        # Creación de capas

        capa0 = Capa(0,initial_nodes)
        capa1 = Capa(1,hiden_nodes)
        capa2 = Capa(2,final_nodes)

        # Añadimos capas a la red

        self.capas.append(capa0)
        self.capas.append(capa1)
        self.capas.append(capa2)

    def entrena(self,datos,salidas,n_epochs,tasa):

        Ejs_clas = list(zip(datos,salidas))
        
        for _ in range(n_epochs):
            random.shuffle(Ejs_clas)
            for x,y in Ejs_clas:
                self.calculaA_Ini(x)
                self.retroprop(y,tasa)
        
    def calculaA_Ini(self,entry):

        for i in range(3):

            capa = self.capas[i]      
            nodos = capa.nodes

            if i == 0:
                
                # Las entradas son las "a" para la capa inicial

                for index in range(len(nodos)):
                    nodos[index].a = entry[index]

            elif i==1:

                # Calculamos Ini

                nodos_initial = self.capas[0].nodes

                for nodo in nodos:

                    nodo.ini = nodo.w0 + sum(nodo.w[index]*nodos_initial[index].a for index in range(len(nodos_initial)))
                    nodo.a = relu(nodo.ini)


            elif i ==2:

                nodos_hidden = self.capas[1].nodes

                for nodo in nodos:

                    nodo.ini = nodo.w0 + sum(nodo.w[index]*nodos_hidden[index].a for index in range(len(nodos_hidden)))
                    nodo.a = sigmoide(nodo.ini)

    def retroprop(self,out,tasa):

        for i in range(2,-1,-1):

            capa = self.capas[i]      
            nodos = capa.nodes

            if i == 2:
                
                for index in range(len(nodos)):
                    nodo = nodos[index]
                    nodo.error = DerivadaSigmoide(nodo.ini)*(out[index]-nodo.a)
                    nodo.w0 += tasa*nodo.error

            elif i == 1:

                nodos_final = self.capas[2].nodes

                for hidden in range(len(nodos)):
                    nodo = nodos[hidden]
                    nodo.error = DerivadaSigmoide(nodo.ini)*sum(nodof.w[hidden]*nodof.error for nodof in nodos_final)
                    nodo.w0 += tasa*nodo.error 
                    
                    for nodof in nodos_final:
                        nodof.w[hidden] += tasa*nodof.a*nodo.error

            elif i == 0:

                nodos_hidden = self.capas[1].nodes

                for initial in range(len(nodos)):

                    nodo = nodos[initial]
                    
                    for nodoh in nodos_hidden:
                        nodoh.w[initial] += tasa*nodoh.a*nodo.error

    def solve(self,entry):

        solve_ini = []
        solve_a = []

        for i in range(3):

            capa = self.capas[i]      
            nodos = capa.nodes

            if i == 0:
                
                # Las entradas son las "a" para la capa inicial

                for index in range(len(nodos)):
                    nodos[index].a = entry[index]

            elif i==1:

                # Calculamos Ini

                nodos_initial = self.capas[0].nodes

                for nodo in nodos:

                    nodo.ini = nodo.w0 + sum(nodo.w[index]*nodos_initial[index].a for index in range(len(nodos_initial)))
                    nodo.a = relu(nodo.ini)


            elif i ==2:

                nodos_hidden = self.capas[1].nodes

                for nodo in nodos:

                    nodo.ini = nodo.w0 + sum(nodo.w[index]*nodos_hidden[index].a for index in range(len(nodos_hidden)))
                    nodo.a = sigmoide(nodo.ini)

                    solve_ini.append(nodo.ini)
                    solve_a.append(nodo.a)

        return solve_ini,solve_a

    def clasifica(self,ej):

        solve_ini,solve_a = self.solve(ej)

        return max(enumerate(softmax(solve_ini)),key=lambda x:x[1])[0]+1,max(enumerate(softmax(solve_a)),key=lambda x:x[1])[0]+1
    
    def rendimiento(self,datos,salidas):

        sum = 0
        sum2 = 0

        for xi,yi in zip(datos,salidas):

            res_ini,res_a = self.clasifica(xi)
            res = yi.index(1)+1
            if res==res_ini:
                sum += 1
            if res==res_a:
                sum2+=1

        return sum/len(salidas), sum2/len(salidas)


class Nodo():

    def __init__(self,w0=0,w=[],ini=0,a=0,error=0):

        self.w0 = w0
        self.w = w
        self.a = a
        self.ini = ini
        self.error = error


class Capa():

    def __init__(self,number=0,nodes=[]):

        self.number = number
        self.nodes = nodes


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
    return sigmoide(x)*(1-sigmoide(x))

def DerivadaRelu(x):
    return 1 if x>0 else 0

### LECTURA DE DATOS

def loadInPuts():
    lista = []
    
    with open("./datos/dataParsed.csv",'r') as f:
        next(f)
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')])

    return lista

def loadOutPutsSOFA():

    lista = []
    file = open("./outputs/sofaScore24OUTS.txt",'r')
    
    for line in file:
        lista.append([int(num) for num in str(line)[:-1].split(',')])

    return lista