#Jogo da forca no terminal
from dtbs import lista_de_palavras as lista
import random

#Últimas mudanças:
#1 - Correção do bug indíce da palavra maior que o total
#2 - Formatação: letra da tentativa sempre em minúsculo
#3 - Formação: primeira letra sempre em maiúsculo

class Palavra:
    palavra = []
    categoria = ""
    popularidade = ""

#    def __init__(self):
#        palavra = ""
#        categoria = ""
#        popularidade = ""

#Define a palavra
def definirPalavra(ls):
    i = random.randint(0, 2)
    print(i)
    p_data = ls[i].split("_")
    p = Palavra()
    p.palavra = p_data[0]
    p.categoria = p_data[1]
    p.popularidade = p_data[2]

    return p

#Opções disponíveis apenas durante o desenvolvimento
def opcDev(palavra, p_tentativa, letras_tentadas):
    print("\n\n***OPÇÕES DO DESENVOLVEDOR***\n\n1 - Mostrar palavra\n2 - Mostrar palavra com letras acertadas\n3 - Mostrar letras tentadas\n4 - Mostrar tudo\n5 - Nova Palavra\n\n")
    opcao = int(input("Digite a opção desejada: "))
    print("\n")

    return opcao

#Menu principal
def Menu():
    print("\nOPÇÕES")
    print("1 = Tentar Letra\n2 = Dica\n3 = Tentar palavra\n4 = Desistir")

    return int(input("\nDigite a opção desejada: "))

#Recebe a letra da tentativa e verifica se ela é repetida ou não
def TentaLetra(vet_letras):
    letra = input("\nDigite a letra: ").lower()
    repetida = False

    for l in range(len(vet_letras)):
        if vet_letras[l] == letra:
            repetida = True
    
    if repetida == True:
        print("\nLetra repetida.\n")
        print("Tente novamente, outra letra.")
        TentaLetra(vet_letras)
    else:
        vet_letras.append(letra)

    return letra

#
def VerificarLetra(letra, p_tentativa, palavra):
    for l in range(len(palavra)):
        if letra == palavra[l]:
            if l == 0:
                p_tentativa[l] = palavra[l].upper()
            else:
                p_tentativa[l] = palavra[l]

    print("".join(p_tentativa))

def Main():
    p = definirPalavra(lista)
    p_tentativa = []
    letras_tentadas = []

    print(f"Palavra de {len(p.palavra)} letras.")
    print("_"*len(p.palavra),"\n")

    opcao = Menu()

    for l in range(len(p.palavra)):
        p_tentativa.append("_")

    while opcao > 0 and opcao <= 4  or opcao == 69:
        match opcao:
            case 1:
                VerificarLetra(TentaLetra(letras_tentadas), p_tentativa, p.palavra)
            case 3:
                if input("Digite a tentativa: ") == p.palavra:
                    print("Você Acertou!!\n")
                    if input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ") == 1:
                        Main()
                    else:
                        break
                else:
                    pass
            case 4:
                break
            case 69:
                opcaoDev = opcDev(p.palavra, p_tentativa, letras_tentadas)
                match opcaoDev:
                    case 1:
                        print("".join(p.palavra))
                    case 2:
                        print("".join(p_tentativa))
                    case 3:
                        print("".join(letras_tentadas))
                    case 4:
                        print("".join(p.palavra), "".join(p_tentativa), "".join(letras_tentadas))
                    case 5:
                        Main()
        opcao = Menu()

Main()