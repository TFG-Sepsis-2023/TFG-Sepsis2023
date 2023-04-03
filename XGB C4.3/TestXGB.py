import xgboost as xgb
import numpy as np
from keras.utils import to_categorical
import Auxiliares
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# DATOS

entradas = Auxiliares.loadInputs()
#salidas = ID3Utils.loadOutPutsSurvival2()
salidas = Auxiliares.loadOutPutsVasopressors()

# Definir parámetros del modelo
param = {'max_depth': 3, 'eta': 0.1, 'objective': 'binary:logistic', 'eval_metric': 'error'}

y_train = np.array(salidas)
y_test = np.array(salidas[-50:])
X_train = np.array(entradas)
X_test = np.array(entradas[-50:])

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
print('Tasa de error:', error_rate)

accuracy = accuracy_score(y_test, preds.round())
precision = precision_score(y_test, preds.round())
recall = recall_score(y_test, preds.round())
f1 = f1_score(y_test, preds.round())

print("Especificidad :", accuracy)
print("Precisión:", precision)
print("Sensibilidad:", recall)
print("F1-score:", f1)
print("Tasa de aciertos:", succes_rate)

'''
PARA REALIZAR UNA PREDICCIÓN DE UNA NUEVA ENTRADA HACEMOS LO SIGUIENTE

def getPredict(entry):

    entrada = [float(num) for num in entry.split(", ")]
    entrada = np.array(entrada)

    dtest = xgb.DMatrix(entrada)
    
    return bst.predict(dtest)



'''
    
    