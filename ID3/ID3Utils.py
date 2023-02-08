
class Name():

    def __init__(self, name, rangeMIN, rangeMAX, set):

        self.name = name
        self.rangeMIN = rangeMIN
        self.rangeMAX = rangeMAX
        self.set = set

    def __str__(self):

        return "Columna=>(Nombre: "+self.Name+", MIN: "+self.rangeMIN+", MAX: "+self.rangeMAX+") "


def loadInPuts():
    lista = []
    file = open("./ID3/DatosEntrada.txt",'r')
    
    for line in file:
        line = line[:-1].split(',')
        lista.append(list(float(num) for num in line))

    return lista

def createColumns():

    pass


        
        