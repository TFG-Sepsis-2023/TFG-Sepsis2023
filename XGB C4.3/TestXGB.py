import xgboost as xgb
import numpy as np
from keras.utils import to_categorical
import Auxiliares
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import random


# DATOS

entradas = Auxiliares.loadInputs()
salidas = Auxiliares.loadOutPutsSurvival2()
#salidas = Auxiliares.loadOutPutsVasopressors()

def trainModel(max_depth,num_train,num_test):

    # Definir parámetros del modelo
    param = {'max_depth': max_depth, 'eta': 0.1, 'objective': 'binary:logistic', 'eval_metric': 'error'}

    y_train = np.array(salidas[:num_train])
    y_test = np.array(salidas[-num_test:])
    X_train = np.array(entradas[:num_train])
    X_test = np.array(entradas[-num_test:])

    # Cargar datos de entrenamiento y prueba
    dtrain = xgb.DMatrix(data = X_train, label = y_train)
    dtest = xgb.DMatrix(data = X_test, label = y_test)

    # Entrenar modelo
    num_round = 50
    bst = xgb.train(param, dtrain, num_round)

    # Evaluar modelo
    preds = bst.predict(dtest)

    # Imprimir tasa de error
    labels = dtest.get_label()
    error_rate = sum(1 for i in range(len(preds)) if int(preds[i] > 0.5) != labels[i]) / float(len(preds))
    succes_rate = sum(1 for i in range(len(preds)) if int(preds[i] > 0.5) == labels[i]) / float(len(preds))

    accuracy = accuracy_score(y_test, preds.round())
    precision = precision_score(y_test, preds.round())
    recall = recall_score(y_test, preds.round())
    f1 = f1_score(y_test, preds.round())

    return error_rate,accuracy,precision,recall,f1,succes_rate


def print_metrics(max_depth,error_rate,accuracy,precision,recall,f1,succes_rate):

    

    print("MAX_DEPTH: "+str(max_depth)+"\n")
    print('Tasa de error:', error_rate)
    print("Especificidad :", accuracy)
    print("Precisión:", precision)
    print("Sensibilidad:", recall)
    print("F1-score:", f1)
    print("Tasa de aciertos:", succes_rate)
    print("---------------------\n")

    
    file.write("MAX_DEPTH: "+ str(max_depth)+"\n")
    file.write("Tasa de aciertos: "+ str(succes_rate)+"\n")
    file.write("Precisión: "+ str(precision)+"\n")
    file.write("Especificidad: "+ str(accuracy)+"\n")
    file.write("Sensibilidad: "+ str(recall)+"\n\n\n")


file = open("./XGB C4.3/procentajes.txt",'w')

error_rate_old = -1
accuracy_old = -1
precision_old = -1
recall_old = -1
f1_old = -1
succes_rate_old = -1

num_valores = 3

nums_train = [random.randint(50,300) for _ in range(num_valores)]
nums_test = [random.randint(50,300) for _ in range(num_valores)]

nums_train = [50,150,300]
nums_test = [50,150,300]


for num_train in nums_train:

    print("DATOS DE ENTRENAMIENTO:",num_train)

    for num_test in nums_test:

        print("DATOS DE TEST:",num_test)
        file.write("NUM TRAIN: "+ str(num_train)+"\n")
        file.write("NUM TEST: "+ str(num_test)+"\n\n")
        for num_depth in [n for n in range(1,len(entradas[0]))]:
        

            error_rate,accuracy,precision,recall,f1,succes_rate = trainModel(num_depth, num_train, num_test)

            if(error_rate==error_rate_old and accuracy==accuracy_old and precision==precision_old 
            and recall==recall_old and f1==f1_old and succes_rate==succes_rate_old):
                print("MEJOR PROFUNDIDA:",num_depth-1,"\n")
                break
            else:
                print_metrics(num_depth,error_rate,accuracy,precision,recall,f1,succes_rate)
                error_rate_old = error_rate
                accuracy_old = accuracy
                precision_old = precision
                recall_old = recall
                f1_old = f1
                succes_rate_old = succes_rate
                
        error_rate_old = -1
        accuracy_old = -1
        precision_old = -1
        recall_old = -1
        f1_old = -1
        succes_rate_old = -1

file.close()

'''
PARA REALIZAR UNA PREDICCIÓN DE UNA NUEVA ENTRADA HACEMOS LO SIGUIENTE

def getPredict(entry):

    entrada = [float(num) for num in entry.split(", ")]
    entrada = np.array(entrada)

    dtest = xgb.DMatrix(entrada)
    
    return bst.predict(dtest)



'''
    
    