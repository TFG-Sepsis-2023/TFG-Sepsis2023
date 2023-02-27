
import ID3Utils, math

id3 = ID3Utils.IDE3(dict(),[],None)

data = ID3Utils.loadInputs()[:200]
outs = ID3Utils.loadOutPutsSurvival()[:200]

data_test = ID3Utils.loadInputs()[200:]
outs_test = ID3Utils.loadOutPutsSurvival()[200:]

print(len(data_test))

id3.entrenamiento(data,outs)

print('FIN DE ENTRENAMIENTO')

ls = id3.rendimiento(data_test,outs_test)

for entry in ls:
    index = data_test.index(entry)
    data_test.remove(entry)
    outs_test.remove(index)



print(len(data_test))
