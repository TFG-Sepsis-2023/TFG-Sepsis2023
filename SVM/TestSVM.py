from sklearn import svm
import numpy as np
import Auxiliares
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score

def print_metrics(accuracy,precision,recall,succes_rate):

    print("Especificidad :", accuracy)
    print("Precisión:", precision)
    print("Sensibilidad:", recall)
    print("Tasa de aciertos:", succes_rate)

    file.write("Tasa de aciertos: "+ str(succes_rate)+"\n")
    file.write("Precisión: "+ str(precision)+"\n")
    file.write("Especificidad: "+ str(accuracy)+"\n")
    file.write("Sensibilidad: "+ str(recall)+"\n\n\n")



def train(entradas,salidas,kernel_type,test_value):

    X = np.array(entradas)
    y = np.array(salidas)

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_value, random_state=42)

    # Crear un clasificador SVM
    clf = svm.SVC(kernel=kernel_type)

    # Entrenar el clasificador SVM
    clf.fit(X_train, y_train)

    # Predecir las etiquetas de la prueba
    y_pred = clf.predict(X_test)

    # Evaluar la precisión del clasificador SVM
    accuracy = clf.score(X_test, y_test)
    succes_rate = sum(1 for x_in,y_in in zip(X_test,y_test) if clf.predict(np.array(x_in).reshape(1,-1))==y_in) / float(len(y_test))
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print_metrics(accuracy,precision,recall,succes_rate)


file = open("./SVM/procentajes.txt",'w')

# Generar un conjunto de datos de ejemplo

entradas = Auxiliares.loadInputs()
salidas_survival = Auxiliares.loadOutPutsSurvival2()
salidas_vasopressors = Auxiliares.loadOutPutsVasopressors()


kernel_types = ['linear','rbf','poly','sigmoid']
test_values = [0.1,0.3,0.5,0.75,0.9]

file.write("--------------- SURVIVAL ---------------\n")
for k_type in kernel_types:

    print("----------------------------")
    print("[+] Kernel Type:",k_type)
    file.write("[+] Kernel Type:"+str(k_type)+"\n")
    for test_value in test_values:

        print("[+] Porcentaje de test:",test_value)
        file.write("[+] Porcentaje de test:"+str(test_value)+"\n")
        train(entradas,salidas_survival,k_type,test_value)
        print("\n")

file.write("--------------- VASOPRESSORS ---------------\n")
for k_type in kernel_types:

    print("----------------------------")
    print("[+] Kernel Type:",k_type)
    file.write("[+] Kernel Type:"+str(k_type)+"\n")
    for test_value in test_values:

        print("[+] Porcentaje de test:",test_value)
        file.write("[+] Porcentaje de test:"+str(test_value)+"\n")
        train(entradas,salidas_vasopressors,k_type,test_value)
        print("\n")