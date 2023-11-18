import random


def jogar():
    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("Você possui 6 tentativas, começando agora!")

    # enquanto (True and True)
    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            tentativas = 6 - erros
            print(f'Você errou, resta(m) {tentativas} tentativa(s)!')
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu.")
    print("Fim de jogo.")


def mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo da forca!")
    print("***************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
