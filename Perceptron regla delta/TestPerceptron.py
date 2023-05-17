import Perceptron, random
from sklearn.model_selection import train_test_split

datos = Perceptron.loadInPuts()
salidas = Perceptron.loadOutPutsSurvival()
#salidas = Perceptron.loadOutPutsVasopressors()

# dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(datos, salidas, test_size=0.2)
epochs = [5,10,20,30,40,50,60]
tasas = [random.uniform(0.001,0.1) for _ in range(5)]

succesPercent = []

file = open("./Perceptron regla delta/salidas.txt","w")

for epoch in epochs:
    print('---------------------------------------------------------')
    print('---------------------- Epochs: '+str(epoch)+' ------------------------')
    print('---------------------------------------------------------\n')
    for tasa in tasas:
        cpuv=Perceptron.Clasificador_Perceptron_Regla_Delta()
        cpuv.entrena(X_train,y_train,tasa=tasa,n_epochs=epoch)

        tp,tn,fp,fn = Perceptron.rendimiento(cpuv,X_test,y_test)
        percent = (tp+tn)/(tp+tn+fp+fn)*100
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

        print('Tasa=',tasa)
        print('\n\tEl porcentaje de aciertos del perceptrón regla delta es:',str(round(percent,4))+'%')
        print("\tPrecision:",precision)
        print("\tEspecificidad:",especificidad)
        print("\tSensibilidad:",sensibilidad,"\n")
        file.write(str(tasa)+"\n")
        file.write(str(percent)+"\n")
        file.write(str(precision)+"\n")
        file.write(str(especificidad)+"\n")
        file.write(str(sensibilidad)+"\n")
        file.write("\n")

        succesPercent.append([percent,epoch,tasa])

print('---------------------------------------------------------\n')

succesPercent.reverse()
best = max(succesPercent, key=lambda x:x[0])
print('El mejor porcentaje de acierto es:',best[0],'con un número de epochs:',best[1],' y una tasa de aprendizaje de:',best[2])
