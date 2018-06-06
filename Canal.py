from random import randint
class Canal():
    qubits = None

    def __init__(self,qubits):
        self.qubits = qubits

    def convertQubit(self,n):
        if(n == "de" or n == "dd"):
            if(randint(0,1) == 0):
                return "de"
            else:
                return "dd"
        else:
            if(randint(0,1) == 0):
                return "rh"
            else:
                return "rv"

    def alteraQubits(self):
        aux = self.qubits
        for I in range(len(self.qubits)):
            aux[I] = self.convertQubit(aux[I])
        self.qubits = aux

    def getQubits(self):
        auxQubits = self.qubits[:]
        self.alteraQubits()
        return auxQubits 

