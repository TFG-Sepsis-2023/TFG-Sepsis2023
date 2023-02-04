import FuncionesRedNeuronal,RedNeuronal,random

red = RedNeuronal.RedNeuronal()
red.nLayers = 3

nodos = []

### CREACIÓN CAPAS

### CAPA 0 Tiene 4 NODOS

leyerNumber = 0
red.layers.append(RedNeuronal.Layer(leyerNumber))
layer = red.layers[leyerNumber]

for i in range(1,5):
    layer.nodes.append(RedNeuronal.Node(i,leyerNumber))

### CAPA 1 Tiene 2 NODOS

leyerNumber = 1
red.layers.append(RedNeuronal.Layer(leyerNumber))
layer = red.layers[leyerNumber]

for i in range(5,7):
    layer.nodes.append(RedNeuronal.Node(i,leyerNumber))

### CAPA 2 Tiene 2 NODOS

leyerNumber = 2
red.layers.append(RedNeuronal.Layer(leyerNumber))
layer = red.layers[leyerNumber]

for i in range(7,9):
    layer.nodes.append(RedNeuronal.Node(i,leyerNumber))

### PESOS

Nodos0 = red.layers[0].nodes
Nodos1 = red.layers[1].nodes
Nodos2 = red.layers[2].nodes

for node in Nodos1:
    node.ws = [random.uniform(-1,1) for _ in range(len(Nodos0))]

for node in Nodos2:
    node.ws = [random.uniform(-1,1) for _ in range(len(Nodos1))]


### CALCULOS DE INi

for node in Nodos1:
    node.ini = sum(node.ws[i]*Nodos0[i].a for i in range(len(Nodos0))) + 1
    node.a = FuncionesRedNeuronal.relu(node.ini)

for node in Nodos2:
    node.ini = sum(node.ws[i]*Nodos1[i].a for i in range(len(Nodos1))) + 1
    node.a = FuncionesRedNeuronal.sigmoide(node.ini)
    
#############################################################

expectedOutputs = []

### RETRO PROPAGACIÓN


## FALTA FOR PARA TODOS LOS OUTPUTS
for node in Nodos2:
    node.error = FuncionesRedNeuronal.Derivadasigmoide(node.ini)*(expectedOutputs[])
