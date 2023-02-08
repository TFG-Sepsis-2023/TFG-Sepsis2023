def loadInPuts():
    lista = []
    file = open("./ID3/DatosEntrada.txt",'r')
    
    for line in file:
        line = line[:-1].split(',')
        lista.append(list(float(num) for num in line))

    return lista


lista = [ls[22] for ls in loadInPuts()]

print(lista)
