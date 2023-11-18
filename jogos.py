import forca
import adivinhacao

print("Escolha o seu jogo!")
print("(1) Adivinhação "
      "(2) Forca")

escolha = int(input("Opção escolhida: "))

if (escolha == 1):
    print("Jogando Adivinhação...")
    adivinhacao.jogar()
elif (escolha ==2):
    print("Jogando Forca...")
    forca.jogar()