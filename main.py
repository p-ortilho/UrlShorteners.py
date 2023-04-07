from art import *
import pyshorteners as ps

tprint("URL Shorteners.Py")

print("URL Shorteners.py é um encurtador de url simples para terminal\n")

print("1.Para encurtar link\n99.Para sair\n")

link_encurtado = False

while link_encurtado == False:

    escolha = int(input("Digite uma opção:\n"))

    if escolha == 1:
        link = input("Digite o link que deseja encurtar:\n")

        encurta = ps.Shortener()

        print("\nLink encurtado!")
        print(f"{encurta.tinyurl.short(link)}\n")

    elif escolha == 99:
        print("Você saiu!")
        exit()
    elif escolha != 1 and escolha != 99:
        print("Entrada invalida!")

