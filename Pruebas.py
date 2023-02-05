import FuncionesRedNeuronal,RedNeuronal,random

### RED NEURONAL

red = RedNeuronal.RedNeuronal()

### ESTADÍSTICAS


initNodes = 4
hiddenNodes = 4
endNodes = 4
hiddenLayers = 1

red.nLayers = 2+hiddenLayers
nLayers = red.nLayers

n = 0.1 # Tasa de aprendizaje


lista_aux = [[1,2,3,2],[3,4,5,2],[1,0,2,3],[4,9,8,1]]
nodos = []



### CREACIÓN CAPAS

def createLayers():

    for layer in range(nLayers):

        if layer == 0:

            ### CAPA INICIAL Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer,[])

            for i in range(1,initNodes+1):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))

            red.layers.append(layerObj)

        elif layer==nLayers-1:
            
            ### CAPA FINAL Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer, [])

            for i in range(initNodes+hiddenNodes+1,initNodes+hiddenNodes+endNodes+1):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))

            red.layers.append(layerObj)

        else:
            ### CAPA OCULTA Tiene 4 NODOS

            layerObj = RedNeuronal.Layer(layer,[])

            for i in range(initNodes+1,initNodes+hiddenNodes+1):
                layerObj.nodes.append(RedNeuronal.Node(i,layer))
            
            red.layers.append(layerObj)



### CREACIÓN DE PESOS INICIALES 

def initialWeights():

    for i in range(nLayers-1,0,-1):
        Nodos0 = red.layers[i-1].nodes
        Nodos1 = red.layers[i].nodes

        for node in Nodos1:
            node.ws = [random.uniform(-1,1) for _ in range(len(Nodos0))]


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
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)

        else:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.relu(node.ini)

#############################################################

### RETRO PROPAGACIÓN

def training(output):

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
                node.w0 = node.w0+n*node.a*node.error

        else:

            Nodos2 = red.layers[layer+1].nodes
            Nodos1 = red.layers[layer].nodes

            for j in range(len(Nodos1)):
                node = Nodos1[j]
                node.error = FuncionesRedNeuronal.DerivadaRelu(node.ini)*sum(node3.ws[j]*node3.a for node3 in Nodos2)
                node.w0 = node.w0+n*node.a*node.error
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
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                print("Sigmoide:",node.ini)
                node.a = FuncionesRedNeuronal.sigmoide(node.ini)
                solve.append(node.ini)

        else:

            Nodos0 = red.layers[layer-1].nodes
            Nodos1 = red.layers[layer].nodes

            for node in Nodos1:
                node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
                node.a = FuncionesRedNeuronal.relu(node.ini)

    print(solve)
    sol = FuncionesRedNeuronal.softmax(solve)
    print(sol)
    return max(enumerate(sol),key=lambda x:x[1])[0]+1

expectedOutputs = FuncionesRedNeuronal.loadOutPuts()
inputs = FuncionesRedNeuronal.loadInPuts()

def main():

    createLayers()
    initialWeights()
    for i in range(1):
        calcAandINi(inputs[i])
        training(expectedOutputs[i])
    """
    for i in range(3):
        calcAandINi(lista_aux[i])
        training(expectedOutputs[i])
    
    """
    print(calcAandINiSOLVE([66,1,1.36,1]))


if __name__ == "__main__":

    main()