from random import randint
class Pessoa():
    nome = None
    bits = []
    bases = []

    def __init__(self,nome):
        self.nome = nome

    # dd => diagonal direita 
    # de => diagonal esquerda 
    # rh => retilineo horizontal
    # rv => retilineo vertical

    def gerarQubits(self,bit,base):
        if(bit == 0 and base == "D"):
            return "dd"
        elif(bit == 0 and base == "R"):
            return "rv"
        elif(bit == 1 and base == "D"):
            return "de"
        elif(bit == 1 and base == "R"):
            return "rh"
        
    def lerQubit(self,qubit,base):
        if(qubit == "dd" and base == "D"):
            return 0
        elif(qubit == "de" and base == "D"):
            return 1
        elif(qubit == "rv" and base == "R"):
            return 0
        elif(qubit == "rh" and base == "R"):
            return 1
        else:
            # 1/4 de qber 2/8
            # v = randint(0,8)
            # if(v == 0): return 1
            # elif(v==1): return 0
            # else: return -1
            return -1
            
    def geraBasesAleatorias(self,nBases):
        self.bases = range(nBases)
        for I in self.bases:
            aux = randint(0,1)
            if(aux == 1):
                self.bases[I] = "R"
            else: 
                self.bases[I] = "D"

    def geraUmaBaseAleatoria(self,nQubits):
        b = randint(0,1)
        if b==1:
            for I in range(nQubits):
                self.bases.append("R")
        else: 
            for I in range(nQubits):
                self.bases.append("D")

    def geraTabelaBases(self,qubits):
        tab1 = []
        tab2 = []
        for I in range(len(qubits)):
            tab1.append(self.lerQubit(qubits[I],"R"))
            tab2.append(self.lerQubit(qubits[I],"D"))
        return [tab1,tab2]

    def geraBitsAleatorios(self,nBits):
        self.bits = range(nBits)
        for I in self.bits:
            self.bits[I] = randint(0,1)

    def enviarQubits(self):
        qubits = range(len(self.bits))
        for I in range(len(self.bits)):
            qubits[I] = self.gerarQubits(self.bits[I],self.bases[I])
        return qubits

    def lerQubits(self,qubits):
        bits = range(len(qubits))
        bases = self.bases
        for I in bits:
            bits[I] = self.lerQubit(qubits[I],bases[I])
        self.bits = bits
        
    def enviaBaseRevisao(self):
        bases = self.bases[:]
        bits = self.bits[:]
        basesRevis = range(len(self.bits))
        for I in basesRevis:
            if (bits[I] != -1):
                basesRevis[I] = bases[I]
            else:
                basesRevis[I] = -1
        return basesRevis

    def revisaBase(self,bases):
        myBases = self.bases
        tBases = range(len(bases))
        for I in tBases:
            if bases[I] == myBases[I]:
                tBases[I] = True
            else:
                self.bits[I] = -1
                tBases[I] = False
        return tBases

    def recebeRevisaBase(self,basesRevisadas):
        for I in range(len(basesRevisadas)):
            if(basesRevisadas[I] == False):
                self.bits[I] = -1
            
    def enviaBitRevisao(self):
        myBits = self.bits
        sendBits = myBits[:]
        iHBits = 0
        for I in range(len(sendBits)):
            if sendBits[I] != -1:
                sendBits[I] = -1
                iHBits += 1
        if(iHBits ==0):
            return myBits
        s=False
        I=0
        if iHBits//3 < 1:
            s=True
        while I<iHBits//3 or s:
            aux = randint(0,len(myBits)-1)
            if myBits[aux] != -1:
                if s:
                    sendBits[aux] = myBits[aux]
                    self.bits[aux] = -1
                    return sendBits
                sendBits[aux] = myBits[aux]
                self.bits[aux] = -1
                I+=1
        return sendBits

    def revisaBit(self,bits):
        valido = True
        for I in range(len(self.bits)):
            if(self.bits[I] != bits[I] and bits[I] != -1):
                self.bits[I] = -1
                valido = False
            elif(self.bits[I] == bits[I]):
                self.bits[I] = -1
        return valido

    def bitsSecretos(self):
        sBits = []
        for I in range(len(self.bits)):
            if(self.bits[I] != -1):
                sBits.append(self.bits[I])
        return sBits 

    def inverteBits(self):
        newBits = self.bits[:]
        for I in range(len(self.bits)):
            if(self.bits[I] == 1):
                newBits[I] = 0
            elif(self.bits[I] == 0):
                newBits[I] = 1
            else:
                newBits[I] = -1
        self.bits = newBits

    def geraSpinSingleto(self):
        v =[]
        v.append(self.enviarQubits())
        self.inverteBits()
        v.append(self.enviarQubits())
        return v
