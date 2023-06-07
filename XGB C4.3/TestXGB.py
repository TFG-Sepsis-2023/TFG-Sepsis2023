import xgboost as xgb
import numpy as np
from keras.utils import to_categorical
import Auxiliares
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import random
from sklearn.model_selection import train_test_split


# DATOS

entradas = Auxiliares.loadInputs()
# salidas = Auxiliares.loadOutPutsSurvival2()
salidas = Auxiliares.loadOutPutsVasopressors()
# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train_, X_test_, y_train_, y_test_ = train_test_split(entradas, salidas, test_size=0.2)

# def trainModel(max_depth,num_train,num_test):
def trainModel(max_depth):

    # Definir parámetros del modelo
    param = {'max_depth': max_depth, 'eta': 0.1, 'objective': 'binary:logistic', 'eval_metric': 'error'}

    y_train = np.array(y_train_)
    y_test = np.array(y_test_)
    X_train = np.array(X_train_)
    X_test = np.array(X_test_)

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
    print(preds)
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

print("DATOS DE ENTRENAMIENTO:",len(X_train_))


print("DATOS DE TEST:",len(X_test_))
file.write("NUM TRAIN: "+ str(len(X_train_))+"\n")
file.write("NUM TEST: "+ str(len(X_test_))+"\n\n")
for num_depth in [n for n in range(1,len(entradas[0]))]:


    error_rate,accuracy,precision,recall,f1,succes_rate = trainModel(num_depth)

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

    