import random 
import os
from lib import menu, clear
from colorama import Fore, Back

def empate():
    qst1 = input(Fore.YELLOW + '\nEmpate!!' + Fore.CYAN + ' Deseja jogar novamente? ' + Fore.WHITE).capitalize()

    if qst1 == 'Sim':
        game()
    elif qst1 == 'Não':
        print('a')
    else:
        empate()

def win():
    qst1 = input(Fore.GREEN + '\nVocê ganhou!!' + Fore.CYAN + ' Deseja jogar novamente? ' + Fore.WHITE).capitalize()

    if qst1 == 'Sim':
        game()
    elif qst1 == 'Não':
        print('a')
    else:
        win()

def lose():
    qst1 = input(Fore.RED + '\nVocê perdeu!!' + Fore.CYAN + ' Deseja jogar novamente? ' + Fore.WHITE).capitalize()

    if qst1 == 'Sim':
        game()
    elif qst1 == 'Não':
        print('a')
    else:
        lose()

def game():
    opt = ['Pedra', 'Papel', 'Tesoura']
    bot = random.choice(opt)
    myOpt = None

    clear()
    menu()
    
    myOpt = input(Fore.CYAN + '\nOlá ' + Fore.MAGENTA + f'{name}'+ Fore.CYAN + ', vamos jogar? Em caso afirmativo, selecione' 
          + Fore.WHITE + ' Pedra/Papel/Tesoura: ').strip().capitalize()
    
    if myOpt == bot:
        empate()
        
    elif myOpt == 'Pedra':
        if bot == 'Papel':
            lose()
        else:
            win()
    
    elif myOpt == 'Papel':
        if bot == 'Tesoura':
            lose()
        else:
            win()

    elif myOpt == 'Tesoura':
        if bot == 'Pedra':
            lose()
        else:
            win()


os.system('cls' if os.name == 'nt' else 'clear')
menu()
name = input(Fore.CYAN + '\nQual é o seu nome? ' + Fore.WHITE).capitalize()
game()