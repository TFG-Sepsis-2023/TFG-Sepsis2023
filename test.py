import pandas as pd

def main():
    file_name = 'C:/Users/aleja/Documents/Universidad/TFG/Dataset.xlsx'

    archivo_excel = pd.read_excel(file_name, skiprows=range(1,2))
    #print(archivo_excel.columns)

    """
    values = archivo_excel['Age'].values
    print(values)

    columnas = ['Age', 'Sex', 'DM']
    df_seleccionados = archivo_excel[columnas]
    print(df_seleccionados)
    """

if __name__ == "__main__":

    b=3
    a = 1 if b<2 else 2

    print(a)