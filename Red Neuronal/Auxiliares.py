
### LECTURA DE DATOS

def loadInPuts():
    lista = []
    
    with open("./datos/dataParsed.csv",'r') as f:
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')])

    return lista

def loadInPuts2():
    lista = []
    
    with open("./datos/data2.csv",'r') as f:
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')])

    return lista

def loadOutPutsSOFA():

    lista = []
    file = open("./outputs/sofaScore24OUTS.txt",'r')
    
    for line in file:
        lista.append(float(str(line)[:-1]))

    return lista

def loadOutPutsOUTCOME():

    lista = []
    file = open("./outputs/4OUTPUTS1.txt",'r')
    
    for line in file:
        lista.append(float(str(line)[:-1]))

    return lista