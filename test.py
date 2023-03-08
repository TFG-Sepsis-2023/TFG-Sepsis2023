import pandas as pd

def main():
    

    """
    values = archivo_excel['Age'].values
    print(values)

    columnas = ['Age', 'Sex', 'DM']
    df_seleccionados = archivo_excel[columnas]
    
    ### VALOR DE OUTPUT INDEX 24
    # output = lista[24]
    ### RESTO DE VALORES MENOS OUTPUT
    # values = lista[:24]+lista[25:]
    outputs = []
    for i in range(364):
        lista = archivo_excel.loc[i].values.flatten().tolist()
        values = lista[1:24]
        outputs.append(lista[24])
        file.write(str(values)[1:-1]+"\n")
    
    file.close()

    """
'''

    '''


if __name__ == "__main__":

    ls = [71,2,0.07,2,1,1,1,2,2,2,1,2,1,236,100,224,0.3,15,110,0,0.7,1,2,5,1,8,2,6,1]

    print(ls[22])
    # SOFA score 22
    # VASOPRESSOR 19
    # SURVIVAL 28

    vasopresosrs = []
    sofas = []

    file = open('./outputs/sofaScore24OUTS.txt','w')
    with open('./datos/data.csv','r') as f:

        next(f)
        for line in f:

            line = [float(num) for num in line.split(',')]
            file.write(str(line[22])+"\n")





    
