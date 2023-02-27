
import math

class Nodo():

    def __init__(self,atribute,data,outs,padre,hijos,entropia=0):

       self.padre = padre
       self.hijos = hijos
       self.atribute = atribute
       self.entropia = entropia
       self.data = data
       self.outs = outs


class IDE3():

    def __init__(self,dict,nodes, mainNode):

        self.dict = dict
        self.nodes = nodes
        self.mainNode = mainNode
 
    def calcValues(self,data):

        dictionary = dict()


        for i in range(len(data[0])):

            dictionary[i] = set(num[i] for num in data)

        self.dict = dictionary

    def bestEnthropy(self,data,outs):

        ent = self.enthropy(data,outs)

        ganancies = []

        for key in self.dict:

            ganacy = ent

            for value in self.dict[key]:

                newData = []
                newOuts = []

                for entry,out in zip(data,outs):

                    if entry[key]==value: 
                        newData.append(entry)
                        newOuts.append(out)

                ganacy = ganacy - len(newData)/len(data) * self.enthropy(newData,newOuts)

                ganancies.append([key,ganacy, newData, newOuts])
        
        return max(ganancies, key= lambda x:x[1])

    def enthropy(self,data,outs):


        possitive = sum(sol==1 for _,sol in zip(data,outs))
        negative = sum(sol==0 for _,sol in zip(data,outs))
        total = len(data)

        if possitive==0 or negative==0: return 0
        elif possitive==negative: return 1

        return -possitive/total * math.log(possitive/total,2) - negative/total * math.log(negative/total)

    def entrenamiento(self,data,outs):

        self.calcValues(data)

        best_initial = self.bestEnthropy(data,outs)

        mainNode = Nodo(best_initial[0],best_initial[2],best_initial[3],None,[])

        for key in self.dict[best_initial[0]]:

            self.calcNode(mainNode,mainNode.data,mainNode.outs, key)


        self.mainNode = mainNode

        return None

    def calcNode(self,padre,data,outs,value):

        newData = []
        newOuts = []

        for i in range(len(data)):
            if data[i][padre.atribute] == value:
                newData.append(data[i])
                newOuts.append(outs[i])


        ent = self.enthropy(newData,newOuts)

        if ent == 0: 
            padre.hijos.append(Nodo(None,newData,newOuts,padre,[],ent))
            return None
        
        else:

            bestAtribute,bestGanancy,bestData,bestOuts = self.bestEnthropy(data,outs)

            newNode = Nodo(bestAtribute,bestData,bestOuts,padre,[],ent)

            for key in self.dict[bestAtribute]:
                self.calcNode(newNode,bestData,bestOuts,key)

            padre.hijos.append(newNode)

            return None


    def clasifica(self,entry):

        # 1, 2.0, 0, 2.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 1, 1, 1, 0, 1, 1, 0, 1.0, 0, 1.0, 8.0, 2.0, 6.0

        node = self.mainNode
        res = None

        while(True):
            
            atribute = node.atribute
            hijos = node.hijos

            if atribute == None:
                res = node.outs[0]
                break

            option = list(enumerate(self.dict[atribute]))



            if len(hijos)==0:
                res = node.outs[0]
                break

            for i,value in option:
                entrada = entry[atribute] 
                if entry[atribute]==value: 
                    node = hijos[i]
                    break


        return res




def loadOutPutsVasopressors():

    lista = []
    file = open("./outputs/vasopressorsBinary.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def loadOutPutsSurvival():

    lista = []
    file = open("./outputs/survivalBinary.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def createDataID3():
    
    file = open('./ID3/datosID3.csv','w')

    with open('./datos/dataParsed.csv','r') as f:

        for line in f:

            lineWtirte = [float(num) for num in str(line).split(',')]

            # AGE

            lineWtirte[0] = int(lineWtirte[0]>61.31593)

            # Initial procalcitonin (PCT) value

            lineWtirte[2] = int(lineWtirte[2]>13.87909)

            # respiration (PaO2)

            lineWtirte[13] = int(lineWtirte[13]>93.85742)
            
            # respiration (FiO2)

            lineWtirte[14] = int(lineWtirte[14]>45.78571)
            
            # palets

            lineWtirte[15] = int(lineWtirte[15]>213.1566)
            
            # bilirubin

            lineWtirte[16] = int(lineWtirte[16]>0.8697802)
            
            # Glasgow Coma Scale

            lineWtirte[17] = int(lineWtirte[17]>13.4478)
            
            # Mean arterial preasure

            lineWtirte[18] = int(lineWtirte[18]>79.67308)
            
            # Creatine

            lineWtirte[19] = int(lineWtirte[19]>1.959423)
            
            # Length of stay (LOS)

            lineWtirte[21] = int(lineWtirte[21]>61.31593)   

            # ESCRIBIMOS LA LINEA

            file.write(str(lineWtirte)[1:-1]+"\n")
            
def loadInputs():

    data = []

    with open('./ID3/datosID3.csv','r') as f:
        for line in f:
            data.append([float(num) for num in str(line).split(',')])

    return data        