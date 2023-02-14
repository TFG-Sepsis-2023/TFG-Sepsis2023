
class Name():

    def __init__(self, name, rangeMIN, rangeMAX,values,index):

        self.name = name
        self.rangeMIN = rangeMIN
        self.rangeMAX = rangeMAX
        self.values = values
        self.index = index

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

    columnas = []

    with open('./ID3/Columnas.txt','r') as f:
        for line in f:

            parts = line.split(';')
            name = parts[0]
            min = parts[1]
            if min == 'None':
                min = None
            else:
                min = int(min)
                
            max = parts[2]

            if max == 'None':
                max = None
            else:
                max = int(max)

            values = parts[3]
            for i in range(len(values)):
                value = values[i]
                if value=='SI' or value=='NO':
                    pass
                else:
                    values[i]=int(value)

            index = int(parts[4])

            columnas.append(Name(name,min,max,values,index))

    return columnas


        
        