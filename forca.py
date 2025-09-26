#Jogo da forca no terminal
from dtbs import lista_de_palavras as lista
import random

#Últimas mudanças:
#1 - Aumento da lista de palavras usando o chatgpt para gerá-las

class Palavra:
    palavra = []
    categoria = ""
    popularidade = ""

#Define a palavra
def definirPalavra(ls):
    i = random.randint(0, len(ls))
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
        if letra == "a":
            match palavra[l]:
                case "á":
                    p_tentativa[l] = palavra[l]
                case "à":
                    p_tentativa[l] = palavra[l]
                case "ã":
                    p_tentativa[l] = palavra [l]
                case "â":
                    p_tentativa[l] = palavra [l]
        elif letra == "e":
            match palavra[l]:
                case "é":
                    p_tentativa[l] = palavra[l]
                case "è":
                    p_tentativa[l] = palavra[l]
                case "ê":
                    p_tentativa[l] = palavra[l]
        elif letra == "i":
            match palavra[l]:
                case "í":
                    p_tentativa[l] = palavra[l]
                case "ì":
                    p_tentativa[l] = palavra[l]
                case "î":
                    p_tentativa[l] = palavra[l]
        elif letra == "o":
            match palavra[l]:
                case "ó":
                    p_tentativa[l] = palavra[l]
                case "ò":
                    p_tentativa[l] = palavra[l]
                case "õ":
                    p_tentativa[l] = palavra[l]
                case "ô":
                    p_tentativa[l] = palavra[l]
        elif letra == "u":
            match palavra[l]:
                case "ú":
                    p_tentativa[l] = palavra[l]
                case "ù":
                    p_tentativa[l] = palavra[l]
        elif letra == palavra[l]:
            if l == 0:
                p_tentativa = palavra[l].upper()
            else:
                p_tentativa = palavra[l]

        #passar for de baixo pra cá

    for l in range(len(palavra)):
        if letra == palavra[l]:
            if l == 0:
                p_tentativa[l] = palavra[l].upper()
            else:
                p_tentativa[l] = palavra[l]
        elif letra == "a":
            match palavra[l]:
                case "á":
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
                    if int(input("1 = Jogar novamente\n2 = Encerrar\nOpção desejada: ")) == 1:
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