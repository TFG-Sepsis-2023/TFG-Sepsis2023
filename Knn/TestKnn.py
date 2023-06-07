from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.metrics import classification_report
import numpy as np
import Auxiliar

def KNeighbors(n=5):


    neigh = KNeighborsClassifier(n_neighbors=n,metric='minkowski')
    neigh.fit(X_train_selected, y_train)
    accuracy = neigh.score(X_test_selected, y_test)

    y_predict = neigh.predict(X_test_selected)
    print('Accuracy=',accuracy*100)
    print(classification_report(y_test,y_predict))


### Knn

#datos = Auxiliar.loadInPuts()
datos = Auxiliar.loadInPuts2()
#salidas = Auxiliar.loadOutPutsSOFA()
salidas = Auxiliar.loadOutPutsOUTCOME()
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

for i in range(3,50,2):
    print("K=",i)
    KNeighbors(i)
