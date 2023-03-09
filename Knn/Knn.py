from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import numpy as np

### LECTURA DE DATOS

def loadInPuts():
    lista = []
    
    with open("./datos/dataParsed.csv",'r') as f:
        for line in f:
            lista.append([float(num) for num in str(line)[:-1].split(',')])

    return lista

def loadOutPutsSOFA():

    lista = []
    file = open("./outputs/sofaScore24OUTS.txt",'r')
    
    for line in file:
        lista.append(float(str(line)[:-1]))

    return lista

def loadOutPutsOutcome():

    lista = []
    file = open("./outputs/outcome.txt",'r')
    
    for line in file:
        lista.append(float(str(line)[:-1]))

    return lista

### Knn

datos = loadInPuts()
salidas = loadOutPutsOutcome()
scaler = StandardScaler()


datos = np.array(datos)
salidas = np.array(salidas)


X_train_normalized = scaler.fit_transform(datos)
selector = SelectKBest(score_func=f_classif, k=10)
X_train_selected = selector.fit_transform(X_train_normalized, salidas)
selected_indices = selector.get_support(indices=True)

# Seleccionar solo las características relevantes en X_train y X_test
X_train_selected = datos[:, selected_indices]

# Dividir los datos en entrenamiento y prueba
X_train_selected, X_test_selected, y_train, y_test = train_test_split(X_train_selected, salidas, test_size=0.2, random_state=42)

best = []

def KNeighbors(n=5):


    neigh = KNeighborsClassifier(n_neighbors=n,metric='minkowski')
    neigh.fit(X_train_selected, y_train)
    accuracy = neigh.score(X_test_selected, y_test)

    print('Accuracy=',accuracy)

    #prob = sum(neigh.predict(np.array(dato).reshape(1,-1))[0]==salida for dato,salida in zip(datos,salidas))/len(datos)*100
    prob = 0
    num = 300
    for dato,salida in zip(X_train_selected[:num],y_train[:num]):
        predict = neigh.predict(np.array(dato).reshape(1,-1))[0]
        
        prob += predict==salida


    prob = prob / num * 100

    best.append([prob,n])

    print("La tasa de acciertos del algoritmo Knn es",round(prob,3),"%")


for i in range(3,50,2):
    print("K=",i)
    KNeighbors(i)

maximo = max(best, key=lambda x:x[0])

print("La mejor tasa de aciertos es de "+str(maximo[0])+"% para k="+str(maximo[1]))