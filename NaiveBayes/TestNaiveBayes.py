import naiveBayes

#Tests con resultados(0:No sobrevive, 1:Si sobrevive)

metodosNB = naiveBayes.NaiveBayes()

datosEntrada = naiveBayes.loadInPuts() #Valores que serán procesados para la ejecución del programa

datosSalida = naiveBayes.loadOutPutsSurvival("./outputs/survivalBinary2.txt")  #Resultados de los valores anteriores

metodosNB.entrena(datosEntrada,datosSalida)
contador = 0
contador2 = 0
for i in range(0,50):
    resFinal,calculosProb = metodosNB.predicción(datosEntrada[i])
    contador+=1
    print("Resultado predecido: {} -- Resultado real: {}".format(resFinal,datosSalida[i]))
    if(resFinal == datosSalida[i]):
        contador2+=1
    print("Valores finales de los cálculos realizados para la elección:")

    print(calculosProb)
salida = (contador2 / contador)*100
print("Probabilidad:{}".format(salida))

"""
#Tests con resultados(1:El paciente mejora y es dado de alta, 2:El paciente muere en el piso de la sala
#                     3:El paciente es admitido o transferido a la UCI y muere
#                     4:El paciente es ingresado o trasladado a la UCI, mejora y posteriormente es dado de alta)                    

clasificacionFinal = {1:"El paciente mejora y es dado de alta",
                      2:"El paciente muere en el piso de la sala",
                      3:"El paciente es admitido o transferido a la UCI y muere",
                      4:"El paciente es ingresado o trasladado a la UCI, mejora y posteriormente es dado de alta"
                      }

metodosNB = naiveBayes.NaiveBayes()

datosEntrada = naiveBayes.loadInPuts() #Valores que serán procesados para la ejecución del programa

datosSalida = naiveBayes.loadOutPutsSurvival("./outputs/datosNV.txt")  #Resultados de los valores anteriores


metodosNB.entrena(datosEntrada,datosSalida)

resFinal,calculosProb = metodosNB.predicción([0, 1.0, 0, 1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 2.0, 0, 1, 0, 0, 0, 0, 1, 3.0, 0, 1.0, 1.0, 2.0, 5.0])

print("Resultado final: ", clasificacionFinal[resFinal])

print("Valores finales de los cálculos realizados para la elección:")

print(calculosProb)

"""