import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


dataframe = pd.read_csv('./datos/data.csv')

X = np.array(dataframe.drop(['Vasopressors','SOFA score','Outcome'],1))

for value in ['Survival','Vasopressors','SOFA score']:
    print("\n\n---------------------------")
    print(value)
    print("---------------------------")
    y = np.array(dataframe[value])

    model = linear_model.LogisticRegression()
    model.fit(X,y)

    print(dataframe.groupby('Survival').size())
    print(dataframe.groupby('Vasopressors').size())
    print(dataframe.groupby('SOFA score').size())

    predictions = model.predict(X)

    print('PORCENTAJE ACIERTOS MODELO COMPLETO:',model.score(X,y)*100)


    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)

    name='Logistic Regression'
    kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())

    predictions = model.predict(X_validation)

    print("PORCENTAJE ACIERTOS MODELO SECCIONADO=",accuracy_score(Y_validation,predictions)*100)

    print(classification_report(Y_validation, predictions))
