
### LECTURA DE DATOS
def loadOutPutsVasopressors():

    lista = []
    file = open("./outputs/vasopressorsBinary.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def loadOutPutsSurvival():

    lista = []
    file = open("./outputs/survivalBinary.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def loadOutPutsSurvival2():

    lista = []
    file = open("./outputs/survivalBinary2.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def loadInputs():

    data = []

    with open('./datos/dataNV.csv','r') as f:
        for line in f:
            data.append([float(num) for num in str(line).split(',')])

    return data        
