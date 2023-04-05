from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import Auxiliares
import numpy as np

# DATOS

entradas = Auxiliares.loadInputs()
#salidas = Auxiliares.loadOutPutsSurvival2()
#salidas = Auxiliares.loadOutPutsVasopressors()

def train(size_test=0.2, prio=0.2):

    X = np.array(entradas)
    y = np.array(salidas)

    # dividir los datos en conjunto de entrenamiento y conjunto de prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=size_test)

    # crear el clasificador de máxima verosimilitud
    clf = GaussianNB(priors=[prio, 1-prio], var_smoothing=0.01)

    # entrenar el clasificador utilizando el conjunto de entrenamiento
    clf.fit(X_train, y_train)

    # hacer predicciones utilizando el conjunto de prueba
    y_pred = clf.predict(X_test)

    # calcular metricas del clasificador
    succes_rate = sum(1 for x_in,y_in in zip(X_test,y_test) if clf.predict(np.array(x_in).reshape(1,-1))==y_in) / float(len(y_test))
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    return accuracy,precision,recall,succes_rate


def print_metrics(accuracy,precision,recall,succes_rate):

    print("Especificidad :", accuracy)
    print("Precisión:", precision)
    print("Sensibilidad:", recall)
    print("Tasa de aciertos:", succes_rate)

    file.write("Tasa de aciertos: "+ str(succes_rate)+"\n")
    file.write("Precisión: "+ str(precision)+"\n")
    file.write("Especificidad: "+ str(accuracy)+"\n")
    file.write("Sensibilidad: "+ str(recall)+"\n\n\n")

# Escribir fihero

file = open("./ML/procentajes.txt",'w')

salidas = Auxiliares.loadOutPutsSurvival2()

print("SURVIVIAL\n --------------")

file.write("SURVIVIAL\n--------------\n")

for prob in [0.2, 0.3, 0.5, 0.75, 0.9]:


    print("CONJUNTO DE TEST:",prob,"\n")
    file.write("CONJUNTO DE TEST:"+str(prob)+"\n")
    for prio in [0.2, 0.3, 0.5, 0.75, 0.9]:
        print("PRIO:"+str(prio)+"\n")
        file.write("PRIO:"+str(prio)+"\n")
        accuracy,precision,recall,succes_rate = train(prob,prio)
        print_metrics(accuracy,precision,recall,succes_rate)
        print("--------------------------------\n\n")

print("VASOPRESORES\n --------------")
file.write("VASOPRESORES\n--------------\n")

salidas = Auxiliares.loadOutPutsVasopressors()

for prob in [0.2, 0.3, 0.5, 0.75, 0.9]:

    print("CONJUNTO DE TEST:",prob,"\n")
    file.write("CONJUNTO DE TEST:"+str(prob)+"\n")
    for prio in [0.2, 0.3, 0.5, 0.75, 0.9]:
        print("PRIO:"+str(prio)+"\n")
        file.write("PRIO:"+str(prio)+"\n")
        accuracy,precision,recall,succes_rate = train(prob,prio)
        print_metrics(accuracy,precision,recall,succes_rate)
        print("--------------------------------\n\n")