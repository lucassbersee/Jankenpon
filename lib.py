from colorama import * 
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(Back.MAGENTA + Fore.WHITE + '=================================================================' + Back.RESET)
    print(Back.MAGENTA + Fore.WHITE + '=' + Back.RESET + '             Bem-vindo(a) ao meu jogo de Jankenpon             ' + Back.MAGENTA + '=' + Back.RESET)
    print(Back.MAGENTA + Fore.WHITE + '=' + Back.RESET + '             Esse jogo foi desenvolvido em Python!             ' + Back.MAGENTA + '=' + Back.RESET)
    print(Back.MAGENTA + Fore.WHITE + '=' + Back.RESET + '               Código feito por Lucas Sberse ⬇                 ' + Back.MAGENTA + '=' + Back.RESET)
    print(Back.MAGENTA + Fore.WHITE + '=' + Back.RESET + '                                       @lucassbersee           ' + Back.MAGENTA + '=' + Back.RESET)
    print(Back.MAGENTA + Fore.WHITE + '=================================================================' + Back.RESET + Fore.RESET)