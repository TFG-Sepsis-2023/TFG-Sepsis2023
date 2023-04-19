import naiveBayes

#Tests con resultados(0:No sobrevive, 1:Si sobrevive)

file = open("./NaiveBayes/resultado_vaso.txt","w")

metodosNB = naiveBayes.NaiveBayes()

datosEntrada = naiveBayes.loadInPuts() #Valores que serán procesados para la ejecución del programa

datosSalida = naiveBayes.loadOutPutsSurvival("./outputs/vasopressorsBinary.txt")  #Resultados de los valores anteriores

for datosEntrenamiento in range(50,len(datosEntrada),50):
    metodosNB.entrena(datosEntrada[:datosEntrenamiento],datosSalida[:datosEntrenamiento])
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(datosEntrada)):
        try:
            resFinal,calculosProb = metodosNB.predicción(datosEntrada[i])


            if datosSalida[i] == 1:

                if resFinal==1:
                    tp += 1
                else:
                    fn += 1
                
            else:
                if resFinal==1:
                    fp += 1
                else:
                    tn += 1
                
        except:
            pass


    acierto = (tp+tn)/(tp+tn+fp+fn)*100
    try:
        precision = tp/(tp+fp)*100
    except ZeroDivisionError:
        precision = 0

    try:
        especificidad = tn / (tn+fp)*100
    except ZeroDivisionError:
        especificidad = 0

    try:
        sensibilidad = tp/(tp+fn)*100
    except ZeroDivisionError:
        sensibilidad = 0  
    acierto = round(acierto,2)
    precision = round(precision,2)
    especificidad = round(especificidad,2)
    sensibilidad = round(sensibilidad,2)

    file.write(str(datosEntrenamiento)+" "+str(acierto)+"% "+str(precision)+"% "+str(especificidad)+"% "+str(sensibilidad)+"%\n")
    

file.close()

    
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