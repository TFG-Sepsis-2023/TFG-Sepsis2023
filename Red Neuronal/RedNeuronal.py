### CLASES

class RedNeuronal():

    def __init__(self,nLayers=None,layers=[]):

        self.nLayers = nLayers
        self.layers = layers
        
    def __str__(self):
        return "Red Neuronal (Número de capas = "+str(self.nLayers)+", Capas = "+str(self.layers)+")"
        
    

class Layer():

    def __init__(self,number,nodes=[]):

        self.number = number
        self.nodes = nodes

    def __str__(self):

        return "Capa (Numero = "+str(self.number)+", Nodos = "+str(len(self.nodes))+")"
        

class Node():

    def __init__(self,name,layer=0,a=0,ini=None,ws=[],w0=1,error=0):

        self.name = name
        self.layer = layer
        self.a = a
        self.ini = ini
        self.ws = ws
        self.w0 = w0
        self.error = error
        
    def __str__(self):

        return "Nodo (Nombre = "+str(self.name)+", Capa = "+str(self.layer)+", Ini = "+str(self.ini)+", Pesos = "+str(self.ws)+", Error = "+str(self.error)+")"
        
