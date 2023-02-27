'''
import ID3Utils

id3 = ID3Utils.IDE3(dict(),[],None)

data = ID3Utils.loadInputs()
outs = ID3Utils.loadOutPutsSurvival()

id3.entrenamiento(data,outs)

print(id3.clasifica(data[0]))'''

from sklearn.datasets import load_diabetes
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
X, y = load_diabetes(return_X_y=True)
regressor = DecisionTreeRegressor(random_state=0)
cross_val_score(regressor, X, y, cv=10)
print(regressor.get_params())