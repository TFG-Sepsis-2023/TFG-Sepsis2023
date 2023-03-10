
import ID3Utils, random

id3 = ID3Utils.IDE3(dict(),[],None)

n_datos_entrenamiento = [random.randint(50,360) for _ in range(10)]
n_datos_test = [random.randint(100,360) for _ in range(10)]

datas = ID3Utils.loadInputs()
outss = ID3Utils.loadOutPutsSurvival2()
#outss = ID3Utils.loadOutPutsVasopressors()

best = []

for num in n_datos_entrenamiento:
    data = datas[num:]
    outs = outss[num:]

    id3.entrenamiento(data,outs)

    print('----------- Datos de entrenamiento '+str(num)+' -------------\n')

    for test in n_datos_test:

        data_test,outs_test = id3.getConjuntoTest(test,datas,outss)

        porcen = id3.rendimiento(data_test,outs_test)

        print('Para un número de datos de test de',len(data_test),"\n")
        print('El porcentaje de acierto es:',round(porcen,3),"\n")

        best.append([porcen,num,len(data)])


porcen,num_entr,num_test = max(best, key=lambda x:x[0])
print('El mejor porcentaje de aciertos ha sido',porcen,'para un total de',num_entr,'datos de entrenamiento y',num_test,'datos de prueba')

