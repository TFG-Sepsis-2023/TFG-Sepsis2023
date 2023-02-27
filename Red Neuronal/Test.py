import NuevaRed

red = NuevaRed.RedNeuronal([])

datos = NuevaRed.loadInPuts()
salidas = NuevaRed.loadOutPutsSOFA()

red.crea(len(datos[0]),6,len(salidas[0]))

red.entrena(datos,salidas,5,0.1)

res1,res2 = red.rendimiento(datos,salidas)

print(res1*100, res2*100)