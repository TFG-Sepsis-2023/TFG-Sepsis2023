import Perceptron,random


datos = Perceptron.loadInPuts()
#salidas = Perceptron.loadOutPutsSurvival()
salidas = Perceptron.loadOutPutsVasopressors()

epochs = [5,10,20,30,40,50,60]
tasas = [random.uniform(0.001,0.1) for _ in range(5)]

succesPercent = []

for epoch in epochs:
    print('---------------------------------------------------------')
    print('---------------------- Epochs: '+str(epoch)+' ------------------------')
    print('---------------------------------------------------------\n')
    for tasa in tasas:
        cpuv=Perceptron.Clasificador_Perceptron_Umbral()
        cpuv.entrena(datos,salidas,tasa=tasa,n_epochs=epoch)

        percent = Perceptron.rendimiento(cpuv,datos,salidas)*100
        print('Tasa=',tasa)
        print('El porcentaje de aciertos del perceptrón regla umbral es:',str(round(percent,4))+'%\n')

        succesPercent.append([percent,epoch,tasa])

print('---------------------------------------------------------\n')

succesPercent.reverse()
best = max(succesPercent, key=lambda x:x[0])
print('El mejor porcentaje de acierto es:',best[0],'con un número de epochs:',best[1],' y una tasa de aprendizaje de:',best[2])
