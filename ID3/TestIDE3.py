
import ID3Utils, random
from sklearn.model_selection import train_test_split
id3 = ID3Utils.IDE3(dict(),[],None)

n_datos_entrenamiento = [random.randint(50,360) for _ in range(10)]
n_datos_test = [random.randint(100,360) for _ in range(10)]

datas = ID3Utils.loadInputs()
#outss = ID3Utils.loadOutPutsSurvival2()
outss = ID3Utils.loadOutPutsVasopressors()
X_train, X_test, y_train, y_test = train_test_split(datas, outss, test_size=0.2)
best = []
file = open("./ID3/salidas.txt","w")

id3.entrenamiento(X_train,y_train)

print('----------- Datos de entrenamiento '+str(len(X_train))+' -------------\n')

X_test,y_test = id3.getConjuntoTest(72,datas,outss)

tp,tn,fp,fn  = id3.rendimiento(X_test,y_test)
porcen = (tp+tn)/(tp+tn+fp+fn)
try:
    precision = tp/(tp+fp)
except ZeroDivisionError:
    precision = 0

try:
    especificidad = tn / (tn+fp)
except ZeroDivisionError:
    especificidad = 0

try:
    sensibilidad = tp/(tp+fn)
except ZeroDivisionError:
    sensibilidad = 0

print('Para un número de datos de test de',len(X_test),"\n")
print('El porcentaje de acierto es:',porcen,"\n")
print("\tPrecision:",precision)
print("\tEspecificidad:",especificidad)
print("\tSensibilidad:",sensibilidad,"\n")
file.write(str(len(X_train))+"\n")
file.write(str(len(X_test))+"\n")
file.write(str(porcen)+"\n")
file.write(str(precision)+"\n")
file.write(str(especificidad)+"\n")
file.write(str(sensibilidad)+"\n")
file.write("\n")

best.append([porcen,len(X_train),len(X_train)])


file.close()