from random import randint
from Pessoa import Pessoa
from Canal import Canal

# TODO verbose do e91 e do coin

def bb84():
    # leitura de dados
    nQubits = input("Quantos qubits? ")
    onEve = input("Com eve? 1-T 0-F ")
    verbose = input("Exibicao completa? 1-T 0-F ")
    print("")

    # instancia de pessoas 
    bob = Pessoa("bob")
    alice = Pessoa("alice")

    # gera bases e bits aleatorios de bob 
    bob.geraBasesAleatorias(nQubits)
    bob.geraBitsAleatorios(nQubits)
    if verbose == 1:
        print("bits do bob",bob.bits)
        print("bases bob",bob.bases)
        raw_input("")

    # gera as bases aleatorias de alice
    alice.geraBasesAleatorias(nQubits)
    if verbose == 1:
        print("bases alice",alice.bases)
        raw_input("")

    # bob envia os qubits para o canal
    canal = Canal(bob.enviarQubits())
    if verbose == 1:
        print("bob envia qubits",bob.enviarQubits())
        raw_input("")

    # se a eve observar o canal gera as bases de eve e le os qubits do canal
    if onEve:
        eve = Pessoa("eve")
        eve.geraBasesAleatorias(nQubits)
        eve.lerQubits(canal.getQubits())
        if verbose == 1:
            print("bits que eve leu",eve.bits)
            raw_input("")
    
    # alice le os bits do canal
    alice.lerQubits(canal.getQubits())
    if verbose == 1:
        print("bits que alice intercepta",alice.bits)
        raw_input("")

    # alice envia as bases que recebeu para bob validar
    if verbose == 1:
        print("bases que alice envia para revisar",alice.enviaBaseRevisao())
        raw_input("")

    # bob revisa as bases de alice
    if verbose == 1:
        print("bob revisa as bases enviadas de alice",bob.revisaBase(alice.enviaBaseRevisao()))
    alice.recebeRevisaBase(bob.revisaBase(alice.enviaBaseRevisao()))
    if verbose == 1:
        raw_input("")

    # bits que estao com alice
    if verbose == 1:
        print("bits confirmados de alice",alice.bits)
        raw_input("")

    # alice envia 1/3 de bits para revisao
    bitsRevisao = alice.enviaBitRevisao()
    if verbose == 1:
        print("bits que alice envia para revisao",bitsRevisao)
        raw_input("")

    # bob verifica os bits enviados por alice
    
    if bob.revisaBit(bitsRevisao):
        print("bits compartilhados de modo seguro")
        print("bits secretos com alice",alice.bitsSecretos())
        print("bits secretos com bob",bob.bitsSecretos())
    else:
        print("alguem interceptou os bits!")
        print("bits com alice",alice.bitsSecretos())
        print("bits com bob",bob.bitsSecretos())
    

def e91():
    # leitura de valores
    nQubits = input("Quantos qubits? ")
    onEve = input("Com eve? 1-T 0-F ")
    verbose = input("Exibicao completa? 1-T 0-F ")
    print("")

    # cria unidade que gera o spin singleto e os canais, e distribui o spin
    fulano = Pessoa("fulano")
    fulano.geraBasesAleatorias(nQubits)
    fulano.geraBitsAleatorios(nQubits)
    spin = fulano.geraSpinSingleto()

    canal1 = Canal(spin[0])
    canal2 = Canal(spin[1])

    print("spin1",spin[0])
    print("spin2",spin[1])
    raw_input("")

    # se a eve observar o canal gera as bases de eve e le os qubits de um canal aleatorio
    if onEve == 1:
        eve = Pessoa("eve")
        eve.geraBasesAleatorias(nQubits)
        eve.lerQubits(canal1.getQubits())
        print("bits que eve leu",eve.bits)
        raw_input("")
     
    
    # gera bases aleatorias de alice e bob
    alice = Pessoa("alice")
    bob = Pessoa("bob")
    alice.geraBasesAleatorias(nQubits)
    bob.geraBasesAleatorias(nQubits)

    print("bases de bob",bob.bases)
    print("bases de alice",alice.bases)
    raw_input("")

    # alice e bob leem os qubits do canal
    alice.lerQubits(canal1.getQubits())
    bob.lerQubits(canal2.getQubits())

    print("bits de bob",bob.bits)
    print("bits de alice",alice.bits)
    raw_input("")

    print("bob envia bases para revisao",bob.enviaBaseRevisao())
    raw_input("")

    revisAlice = alice.revisaBase(bob.enviaBaseRevisao())
    print("alice revisa bases",revisAlice)
    raw_input("")

    bob.recebeRevisaBase(revisAlice)

    print("bits de bob",bob.bits)
    print("bits de alice",alice.bits)
    raw_input("")

    bob.inverteBits()
    print("bob inverte os bits",bob.bits)
    raw_input("")
    
    bitsRevisao = bob.enviaBitRevisao()
    print("bob envia bits para revisao",bitsRevisao)
    raw_input("")

    if(alice.revisaBit(bitsRevisao)):
        print("bits compartilhados de modo seguro")
        print("bits secretos com alice",alice.bitsSecretos())
        print("bits secretos com bob",bob.bitsSecretos())
    else:
        print("alguem interceptou os bits!")
        print("bits com alice",alice.bitsSecretos())
        print("bits com bob",bob.bitsSecretos())

def coin():
    nQubits = input("Procedimento com quantos qubits? ")

    alice = Pessoa("alice")
    bob = Pessoa("bob")

    alice.geraBitsAleatorios(nQubits)
    alice.geraUmaBaseAleatoria(nQubits)

    bob.geraBasesAleatorias(nQubits)

    canal = Canal(alice.enviarQubits())

    tabs = alice.geraTabelaBases(canal.getQubits())
    
    print("tab1",tabs[0])
    print("tab2",tabs[1])


print("--------------------------------------------------------------")
print("[1] bb84 ")
print("[2] e91 ")
print("[3] lancamento de moeda ")

op = input("qual protocolo? ")

if op == 1:
    bb84()
elif op == 2:
    e91()
elif op == 3:
    coin()
   
