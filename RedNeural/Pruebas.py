import FuncionesRedNeuronal,RedNeuronal,random

### RED NEURONAL

red = RedNeuronal.RedNeuronal()

### DATOS

expectedOutputs = FuncionesRedNeuronal.loadOutPuts()
inputs = FuncionesRedNeuronal.loadInPuts()

### ESTADÍSTICAS

initNodes = len(inputs[0])
hiddenNodes = 4
endNodes = 4
hiddenLayers = 1

red.nLayers = 2+hiddenLayers
nLayers = red.nLayers

n = 0.1 # Tasa de aprendizaje

### CREACIÓN CAPAS

def createLayers():

    for layer in range(nLayers):

        if layer == 0:

            ### CAPA INICIAL Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer,[])

            for i in range(0,initNodes):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))

            red.layers.append(layerObj)

        elif layer==nLayers-1:
            
            ### CAPA FINAL Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer, [])

            for i in range(0,endNodes):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))

            red.layers.append(layerObj)

        else:
            ### CAPA OCULTA Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer,[])

            for i in range(0,hiddenNodes):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))
            
            red.layers.append(layerObj)



### CREACIÓN DE PESOS INICIALES 

def initialWeights():

    for i in range(nLayers-1,0,-1):
        Nodos0 = red.layers[i-1].nodes
        Nodos1 = red.layers[i].nodes


        for node in Nodos1:
            node.ws = [random.uniform(-1,1) for _ in range(len(Nodos0))]

    for layer in red.layers:
        for node in layer.nodes:
            node.w0 = random.uniform(-1,1)


### CALCULOS DE a Y INi

def calcAandINi(entry):

    for layer in range(nLayers):

        if layer == 0:
            
            Nodos0 = red.layers[layer].nodes

            for i in range(len(Nodos0)):
                Nodos0[i].a= entry[i]

        elif layer == nLayers-1:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + node.w0
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)

        else:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + node.w0
                node.a = FuncionesRedNeuronal.relu(node.ini)

#############################################################

### RETRO PROPAGACIÓN

def retroprop(output):

    for layer in range(nLayers-1,-1,-1):

        if layer == 0:
            
            Nodos0 = red.layers[layer].nodes
            Nodos1 = red.layers[layer+1].nodes
            for j in range(len(Nodos0)):
                node = Nodos0[j]
                for index in range(len(Nodos1)):
                    node2 = Nodos1[index]
                    node2.ws[j]= node2.ws[j] + n*node.a*node2.error

        elif layer == nLayers-1:

            Nodos2 = red.layers[layer].nodes

            for j in range(len(Nodos2)):
                node = Nodos2[j]
                node.error = FuncionesRedNeuronal.DerivadaSigmoide(node.ini)*(output[j]-node.a)
                node.w0 = node.w0+n*node.error

        else:

            Nodos2 = red.layers[layer+1].nodes
            Nodos1 = red.layers[layer].nodes

            for j in range(len(Nodos1)):
                node = Nodos1[j]
                node.error = FuncionesRedNeuronal.DerivadaRelu(node.ini)*sum(node3.ws[j]*node3.error for node3 in Nodos2)
                node.w0 = node.w0+n*node.error
                for index in range(len(Nodos2)):
                    node2 = Nodos2[index]
                    node2.ws[j]= node2.ws[j] + n*node.a*node2.error


### SOLVE

def calcAandINiSOLVE(entry):

    solve = []

    for layer in range(nLayers):

        if layer == 0:
            
            Nodos0 = red.layers[layer].nodes

            for i in range(len(Nodos0)):
                Nodos0[i].a= entry[i]

        elif layer == nLayers-1:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + node.w0
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)
                solve.append(node.ini)

        else:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + node.w0
                node.a = FuncionesRedNeuronal.relu(node.ini)

    print(solve)
    sol = FuncionesRedNeuronal.softmax(solve)
    print(sol)
    return max(enumerate(sol),key=lambda x:x[1])[0]+1



def saveWeights():

    file = open("./Pesos.txt","w")

    for layer in red.layers:
        for nodo in layer.nodes:
            file.write(str(nodo.name)+" => "+str(nodo.ws)+"\n")

    file.close()

def training(inputs, outputs, tasa, n_epochs=50):

    for _ in range(n_epochs):

        conjunto = list(zip(inputs,outputs))
        random.shuffle(conjunto)

        entries = []
        outs = []
        for i,j in conjunto:
            entries.append(i)
            outs.append(j)

        for i in range(20):
            calcAandINi(entries[i])
            retroprop(outs[i])


    return None

def rendimiento(inputs,outputs):

    total = 0
    aciertos = 0

    conjunto = list(zip(inputs,outputs))
    random.shuffle(conjunto)

    entries = []
    outs = []
    for i,j in conjunto:
        entries.append(i)
        outs.append(j)

    for i in range(10):

        total += 1

        res = calcAandINiSOLVE(entries[i])

        expect = outs[i].index(1)+1       

        print(res,expect)

        if res == expect: aciertos+=1

    return print('Porcentaje de aciertos:',aciertos*100/total,'%')


def main():

    createLayers()
    initialWeights()


    #training(inputs,expectedOutputs,0,1)

    print('Fin del entrenamiento')

    rendimiento(inputs,expectedOutputs)



if __name__ == "__main__":

    main()