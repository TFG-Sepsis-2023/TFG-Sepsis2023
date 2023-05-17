from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from keras import metrics
import Auxiliares
import numpy as np

# DATOS
#salidas = Auxiliares.loadOutPutsSOFA()
salidas = Auxiliares.loadOutPutsOUTCOME()
#entradas = Auxiliares.loadInPuts()
entradas = Auxiliares.loadInPuts2()

# dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train_, X_test_, y_train_, y_test_ = train_test_split(entradas, salidas, test_size=0.2)

# Crear el modelo de la red neuronal
model = Sequential()
model.add(Dense(25, activation='relu', input_shape=(len(entradas[0]),)))
model.add(Dense(24, activation='sigmoid'))

# Normalizar la salida con la función softmax
model.add(Dense(5, activation='softmax'))

def trainModel(n_epochs):
    # Compilar el modelo
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=[metrics.Accuracy(),metrics.Precision(),metrics.SpecificityAtSensitivity(0.5)])

    # Codificar los datos de salida en una representación de un solo vector

    y_train = to_categorical(y_train_, 5) # 5 para OUTCOME y 24 para SOFA   
    y_test = to_categorical(y_test_, 5) # 5 para OUTCOME y 24 para SOFA   
    X_train = np.array(X_train_)
    X_test = np.array(X_test_)

    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=n_epochs,batch_size=len(entradas), validation_data=(X_test, y_test),verbose=False)

def predict(entry):

    prediction = model.predict([entry],verbose=False)
    predicted_category = np.argmax(prediction)

    #print(prediction)

    return predicted_category

def save_model():

    # serializar el modelo a JSON
    model_json = model.to_json()
    with open("./Red Neuronal/model.json", "w") as json_file:
        json_file.write(model_json)
    # serializar los pesos a HDF5
    model.save_weights("./Red Neuronal/model.h5")
    print("Modelo Guardado!")

def load_model():
    json_file = open('./Red Neuronal/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # cargar pesos al nuevo modelo
    loaded_model.load_weights("./Red Neuronal/model.h5")
    print("Cargado modelo desde disco.")

    return loaded_model

    
    

#trainModel(30000)
#save_model()
#model = load_model()

guardar = []

for num in [1,20,50,100,500,1000,2000,5000,10000,20000,30000]:
    trainModel(num)
    porc = sum(predict(entry)==out for entry,out in zip(entradas,salidas))/len(entradas)*100
    print("El porcentaje de aciertos es",porc)
    guardar.append([num,porc])
    print(model.get_metrics_result())

print(guardar)
