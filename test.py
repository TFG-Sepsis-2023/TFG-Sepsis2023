import pandas as pd

def main():
    file_name = 'C:/Users/aleja/Documents/Universidad/TFG/Dataset.xlsx'

    archivo_excel = pd.read_excel(file_name, skiprows=range(1,2))
    #print(archivo_excel.columns)

    file = open('./DatosEntrada.txt',"w")

    """
    values = archivo_excel['Age'].values
    print(values)

    """
    columnas = ['Age', 'Sex', 'DM']
    df_seleccionados = archivo_excel[columnas]
    
    ### VALOR DE OUTPUT INDEX 24
    # output = lista[24]
    ### RESTO DE VALORES MENOS OUTPUT
    # values = lista[:24]+lista[25:]
    outputs = []
    for i in range(364):
        lista = archivo_excel.loc[i].values.flatten().tolist()
        values = lista[1:24]+lista[25:]
        outputs.append(lista[24])
        file.write(str(values)[1:-1]+"\n")
    
    file.close()

    file = open('./Outputs.txt',"w")
    for out in outputs:
        file.write(str(out)+"\n")
    file.close()


if __name__ == "__main__":

    main()