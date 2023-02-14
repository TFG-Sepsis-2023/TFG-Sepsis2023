import pandas as pd
import RedNeural.FuncionesRedNeuronal as FuncionesRedNeuronal

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

    outputsList = []

    with open('./datos/data.csv','r') as f:
        next(f)
        for line in f:
            outputsList.append([float(num) for num in str(line)[:-1].split(',')][23:])


    survival = open('./outputs/survivalBinary.txt','w')
    microOrg = open('./outputs/microOrg6OUTS.txt','w')
    extendInf = open('./outputs/extentInfectionBinary.txt','w')
    anatomicalSite = open('./outputs/anatomicalSite7OUTS.txt','w')

    for output in outputsList:

        survival.write(str(output[-1])+"\n")

        extendInf.write(str(output[-3])+"\n")

        MO = [0,0,0,0,0,0]
        AS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        MO[int(output[-2])-1]=1

        microOrg.write(str(MO)[1:-1]+"\n")

        AS[int(output[-4])-1]=1

        anatomicalSite.write(str(AS)[1:-1]+"\n")


    #print(len(FuncionesRedNeuronal.loadInPuts()[0]))
