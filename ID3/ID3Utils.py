
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

            ganancies.append([key,ganacy])
        

        return max(ganancies, key= lambda x:x[1])

    def enthropy(self,data,outs):


        possitive = sum(sol==1 for _,sol in zip(data,outs))
        negative = sum(sol==0 for _,sol in zip(data,outs))
        total = len(data)

        if possitive==0 or negative==0: return 0
        elif possitive==negative: return 1

        return -possitive/total * math.log(possitive/total,2) - negative/total * math.log(negative/total,2)

    def entrenamiento(self,data,outs):

        self.calcValues(data)

        best_initial = self.bestEnthropy(data,outs)

        mainNode = Nodo(best_initial[0],data,outs,None,[])

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

            bestAtribute,bestGanancy = self.bestEnthropy(data,outs)

            newNode = Nodo(bestAtribute,newData,newOuts,padre,[],ent)

            for key in self.dict[bestAtribute]:
                self.calcNode(newNode,newData,newOuts,key)

            padre.hijos.append(newNode)

            return None


    def clasifica(self,entry):

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
                if entry[atribute]==value: 
                    node = hijos[i]
                    break


        return res

    def rendimiento(self,data,outs):

        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for xi,yi in zip(data,outs):
            
            predict = self.clasifica(xi)
            if yi == 1:

                if predict==1:
                    tp += 1
                else:
                    fn += 1
                
            else:
                if predict==1:
                    fp += 1
                else:
                    tn += 1

        return tp,tn,fp,fn

    def getConjuntoTest(self,num,data,outs):

        data = data[-num:]
        outs = outs[:-num]

        ls = self.rendimientoTest(data,outs)

        for entry in ls:
            index = data.index(entry)
            data.remove(entry)
            del outs[index]

        return data,outs

    def clasificaTest(self,entry):

        node = self.mainNode
        res = None

        cont = 0

        while(True):
            
            cont += 1

            if cont==100:
                raise ValueError(entry)

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
                if entry[atribute]==value: 
                    node = hijos[i]
                    break


        return res

    def rendimientoTest(self,data,outs):

        ls = []
        cont = 0
        for dato,out in zip(data,outs):
            try:
                cont += self.clasificaTest(dato)==out
            except:
                ls.append(dato)

        return ls

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

def loadOutPutsSurvival2():

    lista = []
    file = open("./outputs/survivalBinary2.txt",'r')
    
    for line in file:
        lista.append(int(float(str(line)[:-1])))

    return lista

def createDataID3():
    
    file = open('./datos/dataNV.csv','w')

    with open('./datos/data2.csv','r') as f:

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

    with open('./datos/dataNV.csv','r') as f:
        for line in f:
            data.append([float(num) for num in str(line).split(',')])

    return data        

createDataID3()