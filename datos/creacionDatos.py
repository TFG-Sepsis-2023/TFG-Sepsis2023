
#Con esta funcion podremos obtener los datos parseados para poder ser usados para ID3 y Naive Bayes
def createDataID3():
    
    file = open('./ID3/datosID3.csv','w')

    with open('./datos/dataParsed.csv','r') as f:

        for line in f:

            lineWtirte = [float(num) for num in str(line).split(',')]

            # AGE

            lineWtirte[0] = int(lineWtirte[0]>61.31593)

            # Initial procalcitonin (PCT) value

            lineWtirte[2] = int(lineWtirte[2]>13.87909)

            # respiration (PaO2)

            lineWtirte[13] = int(lineWtirte[13]>93.85742)
            
            # respiration (FiO2)

            lineWtirte[14] = int(lineWtirte[14]>45.78571)
            
            # palets

            lineWtirte[15] = int(lineWtirte[15]>213.1566)
            
            # bilirubin

            lineWtirte[16] = int(lineWtirte[16]>0.8697802)
            
            # Glasgow Coma Scale

            lineWtirte[17] = int(lineWtirte[17]>13.4478)
            
            # Mean arterial preasure

            lineWtirte[18] = int(lineWtirte[18]>79.67308)
            
            # Creatine

            lineWtirte[19] = int(lineWtirte[19]>1.959423)
            
            # Length of stay (LOS)

            lineWtirte[21] = int(lineWtirte[21]>61.31593)   

            # ESCRIBIMOS LA LINEA

            file.write(str(lineWtirte)[1:-1]+"\n")

#Con esta función podemos crear el resultado final de cada dato parseado del 1 al 4

def createDataNV():
    
    file = open('./outputs/datosNV.txt','w')

    with open('./outputs/outcome4OUTPUTS.txt','r') as f:

        for line in f:

            lineWtirte = [float(num) for num in str(line).split(',')]
            cont = 1
            for num in lineWtirte:
                if(num !=1):
                    cont+=1
                else:
                    file.write(str(cont)+"\n")
                    break

def createDataNV2():
    
    file = open('./outputs/datosNVBinary.txt','w')
    contador3=0
    with open('./outputs/datosNV.txt','r') as f:

        for line in f:
            if(int(line) == 2 or int(line) == 3):
                file.write(str(0)+"\n")
            else:
                file.write(str(1)+"\n")
                       

createDataNV2()