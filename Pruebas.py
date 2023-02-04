import FuncionesRedNeuronal,RedNeuronal,random

### RED NEURONAL

red = RedNeuronal.RedNeuronal()

### ESTADÍSTICAS

red.nLayers = 3
nLayers = red.nLayers

initNodes = 4
endNodes = 4
hiddenNodes = 4
hiddenLayers = 1

n = 0,1 # Tasa de aprendizaje


lista_aux = [[1,2,3,2],[3,4,5,2],[1,0,2,3],[4,9,8,1]]
nodos = []



### CREACIÓN CAPAS

def createLayers():

    for layer in range(nLayers):

        if layer == 0:

            ### CAPA INICIAL Tiene 4 NODOS

            red.layers.append(RedNeuronal.Layer(layer))
            layer = red.layers[layer]

            for i in range(1,5):
                layer.nodes.append(RedNeuronal.Node(i,layer))

        elif layer==nLayers-1:
            
            ### CAPA FINAL Tiene 4 NODOS

            red.layers.append(RedNeuronal.Layer(layer))
            layer = red.layers[layer]

            for i in range(9,13):
                layer.nodes.append(RedNeuronal.Node(i,layer))

        else:
            ### CAPA OCULTA Tiene 4 NODOS

            red.layers.append(RedNeuronal.Layer(layer))
            layer = red.layers[layer]

            for i in range(5,9):
                layer.nodes.append(RedNeuronal.Node(i,layer))


### CREACIÓN DE PESOS INICIALES 

def initialWeights():

    for i in range(nLayers,0,-1):
        Nodos0 = red.layers[i-1].nodes
        Nodos1 = red.layers[i].nodes

        for node in Nodos1:
            node.ws = [random.uniform(-1,1) for _ in range(len(Nodos0))]


### CALCULOS DE a Y INi

def calcAandINi(entry):

    for layer in nLayers:

        if layer == 0:

            for i in range(len(red.layers[layer])):
                node.a = entry[i]

        elif layer == nLayers-1:

            Nodos0 = red.layers[layer-1]
            Nodos1 = red.layers[layer]

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)

        else:

            Nodos0 = red.layers[layer-1]
            Nodos1 = red.layers[layer]

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.relu(node.ini)

#############################################################

### RETRO PROPAGACIÓN

def training(output):

    for layer in range(nLayers-1,-1,-1):

        if layer == 0:
            
            Nodos0 = red.layers[layer]
            for j in range(len(Nodos0)):
                node = Nodos0[j]
                for index in range(len(Nodos1)):
                    node2 = Nodos2[index]
                    node2.ws[j]= node2.ws[j] + n*node.a*node2.error

        elif layer == nLayers-1:

            Nodos2 = red.layers[layer]

            for j in range(len(Nodos2)):
                node = Nodos2[j]
                node.error = FuncionesRedNeuronal.DerivadaSigmoide(node.ini)*(output[j]-node.a)
                node.w0 = node.w0+n*node.a*node.error

        else:

            Nodos2 = red.layers[layer+1]
            Nodos1 = red.layers[layer]

            for j in range(len(Nodos1)):
                node = Nodos1[j]
                node.error = FuncionesRedNeuronal.DerivadaRelu(node.ini)*(output[j]-node.a)
                node.w0 = node.w0+n*node.a*node.error
                for index in range(len(Nodos2)):
                    node2 = Nodos2[index]
                    node2.ws[j]= node2.ws[j] + n*node.a*node2.error


### SOLVE

def calcAandINiSOLVE(entry):

    solve = []

    for layer in nLayers:

        if layer == 0:

            for i in range(len(red.layers[layer])):
                node.a = entry[i]

        elif layer == nLayers-1:

            Nodos0 = red.layers[layer-1]
            Nodos1 = red.layers[layer]

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)
                solve.append(node.ini)


        else:

            Nodos0 = red.layers[layer-1]
            Nodos1 = red.layers[layer]

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.relu(node.ini)

    print(FuncionesRedNeuronal.softmax(solve))

expectedOutputs = FuncionesRedNeuronal.loadOutPuts()

def main():

    createLayers()
    initialWeights()
    """
    for i in range(364):
        calcAandINi(lista_aux[i])
        training(expectedOutputs[i])
    for i in range(3):
        calcAandINi(lista_aux[i])
        training(expectedOutputs[i])
    
    calcAandINiSOLVE([0,0,0,1])
    """


if __name__ == "__main__":

    main()