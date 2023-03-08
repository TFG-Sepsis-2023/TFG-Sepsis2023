import Perceptron, random


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

    outs = []

    for tasa in tasas:
        cpuv=Perceptron.Clasificador_Perceptron_Regla_Delta()
        cpuv.entrena(datos,salidas,tasa=tasa,n_epochs=epoch)

        '''while(True):
            cons = input('Datos:')
            cons = [float(i) for i in cons.split(',')]
            print('Resultado:',cpuv.clasifica(cons))'''

        percent = Perceptron.rendimiento(cpuv,datos,salidas)*100
        print('Tasa=',tasa)
        print('El porcentaje de aciertos del perceptrón regla delta es:',str(round(percent,4))+'%\n')

        outs.append([percent,epoch,tasa])

    succesPercent.append(max(outs,key=lambda x:x[0]))



print('---------------------------------------------------------\n')

succesPercent.reverse()
best = max(succesPercent, key=lambda x:x[0])
print('El mejor porcentaje de acierto es:',best[0],'con un número de epochs:',best[1],' y una tasa de aprendizaje de:',best[2])
