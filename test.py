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

    file = open("./outputs/outcome.txt","w")

    with open("./outputs/outcome4OUTPUTS.txt") as f:

        for line in f:

            line = [int(num) for num in str(line)[:-1].split(',')]
            index = line.index(1)

            file.write(str(index+1)+"\n")

            





    
