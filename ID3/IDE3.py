
import ID3Utils

id3 = ID3Utils.IDE3(dict(),[],None)

data = ID3Utils.loadInputs()[:200]
outs = ID3Utils.loadOutPutsSurvival()[:200]

id3.entrenamiento(data,outs)

data_test,outs_test = id3.getConjuntoTest(100,'SURVIVAL')

porcen = id3.rendimiento(data_test,outs_test)

print('El porcentaje de acirto es:',porcen)

