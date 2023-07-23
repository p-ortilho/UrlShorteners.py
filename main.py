import qrcode
import pyshorteners
from colorama import Fore
from art import *

def Menu():
    print(Fore.YELLOW + text2art("URL Shorteners.py"))
    print(Fore.RESET)
    print('Menu de funções')
    print(Fore.YELLOW + '1. Encurtador de URL')
    print('2. Gerar QrCode')
    print('99. Sair' + Fore.RESET)

def MenuShorteners():
     print('Escolha uma opção:')
     print(Fore.YELLOW + '1. tinyurl\n2. isgd\n3. clckru\n98. Voltar\n99. Sair' + Fore.RESET)

def GerarQrcode():
    try:
        link = input(Fore.YELLOW + 'Digite a URL: ')
        
        tamanho_box = int(input('Digite o box size: '))
        tamanho_border = int(input('Digite o tamanho da borda: '))
        name = input('Digite o nome do arquivo: ' + Fore.RESET).replace(' ', '')

        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= tamanho_box,
        border= tamanho_border
    )
        qr.add_data(f'{link}')
        qr.make(fit=True)

        imagem = qr.make_image(fill_color='black', back_color='white')

        imagem.save(f'{name}.png')
        print(Fore.GREEN + 'QrCode gerado com sucesso!' + Fore.RESET)
    except:
        print(Fore.RED + 'Algo deu errado tente novamente!' + Fore.RESET)
        GerarQrcode()

def Shorteners():
    s = pyshorteners.Shortener()

    option = input('Digite uma opção: ')
    while option not in ['1', '2', '3', '98', '99']:
        option = input('Digite uma opção: ')    
    if option == '98':
        main()
    elif option == '99':
        exit()
    else:
        try:
            link = input(Fore.YELLOW + 'Digite a URL: ' + Fore.RESET)
            if option == '1':
                shortenings = s.tinyurl.short(link)
                print(Fore.GREEN + 'URL gerada com sucesso!' + Fore.RESET)
                print(shortenings)
            elif option == '2':
                shortenings = s.isgd.short(link)
                print(Fore.GREEN + 'URL gerada com sucesso!' + Fore.RESET)
                print(shortenings)
            elif option == '3':
                shortenings = s.clckru.short(link)
                print(Fore.GREEN + 'URL gerada com sucesso!' + Fore.RESET)
                print(shortenings)
            else:
                exit()
        except:
            print(Fore.RED + 'Entrada Invalida!' + Fore.RESET)
            MenuShorteners()
            Shorteners()
def main():
    Menu()
    option_menu = ''
    while option_menu not in['1', '2', '99']:
        option_menu = input('Digite uma opção: ')    
    if option_menu == '1':
        MenuShorteners()
        Shorteners()
    elif option_menu == '2':
        GerarQrcode()
    elif option_menu == '99':
        exit()

main()