from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.utils import to_categorical
import Auxiliares
import numpy as np

# DATOS
salidas = Auxiliares.loadOutPutsSOFA()
entradas = Auxiliares.loadInPuts()

# Crear el modelo de la red neuronal
model = Sequential()
model.add(Dense(25, activation='relu', input_shape=(26,)))
model.add(Dense(24, activation='sigmoid'))

# Normalizar la salida con la función softmax
model.add(Dense(24, activation='softmax'))

def trainModel():
    # Compilar el modelo
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Codificar los datos de salida en una representación de un solo vector

    y_train = to_categorical(salidas, 24)
    y_test = to_categorical(salidas[-50:], 24)
    X_train = np.array(entradas)
    X_test = np.array(entradas[-50:])

    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=30000,batch_size=len(entradas), validation_data=(X_test, y_test))

def predict(entry):

    prediction = model.predict([entry])
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

    
    

#trainModel()
#save_model()
model = load_model()

print("El porcentaje de aciertos es",sum(predict(entry)==out for entry,out in zip(entradas,salidas))/len(entradas)*100)
