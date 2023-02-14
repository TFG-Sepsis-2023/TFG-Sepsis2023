import Perceptron


ejemplos = Perceptron.loadInPuts()
votos = Perceptron.loadOutPutsSurvival()

cpuv=Perceptron.Clasificador_Perceptron_Umbral()
cpuv.entrena(ejemplos,votos,tasa=0.3,n_epochs=50)

print(Perceptron.rendimiento(cpuv,ejemplos,votos))