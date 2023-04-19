
listas = []
cadena = "[\n"

with open('./NaiveBayes/resultado_vaso.txt','r') as f:

    for line in f:
        line = str(line)[:-1]
        listas.append(line.split(" "))

def add_json(list):
    cad = "{\n"
    cad += '"datosEntrenamiento":"'+str(list[0])+'",\n'
    cad += '"aciertos":"'+str(list[1])+'",\n'
    cad += '"precision":"'+str(list[2])+'",\n'
    cad += '"especificidad":"'+str(list[3])+'",\n'
    cad += '"sensibilidad":"'+str(list[4])+'"\n'
    cad += "},\n"
    return cad

"""
tasas = [0.1,0.3,0.5,0.75,0.9]
types = ['linear','rbf','poly','sigmoid']
tasa_ind = 0
typ_ind = 0
cont = 0
contT = 0
"""
for i in listas:

    cad = add_json(i)
    cadena+=cad
    

cadena = cadena[:-2]+"\n]"


open("./NaiveBayes/res_final_vaso.json","w").write(cadena)