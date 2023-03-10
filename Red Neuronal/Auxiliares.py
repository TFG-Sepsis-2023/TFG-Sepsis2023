
### LECTURA DE DATOS

def loadInPuts():
    lista = []
    
    with open("./datos/dataParsed.csv",'r') as f:
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')])

    return lista

def loadOutPutsSOFA():

    lista = []
    file = open("./outputs/sofaScore24OUTS.txt",'r')
    
    for line in file:
        lista.append(float(str(line)[:-1]))

    return lista