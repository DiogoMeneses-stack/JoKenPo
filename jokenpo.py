from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
x = str(input('Quer jogar: '))

while x == 's' or x == 'S':
    computador = randint(0, 2)
    print('''Suas opções:
    [ 0 ] PEDRA 
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual a sua escolha: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogo {}'.format(itens[jogador]))
    print('-='*11)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCEU')
        elif jogador == 2:
            print('COMPUTADOR GANHOU')
        else:
            print('JOGADA INVALIDA!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCEU')
        else:
            print('JOGADA INVALIDA!')
    elif computador == 2:
        if jogador == 0:
            print('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('JOGADOR VENCEU')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA!')
    x = str(input('Quer jogar: '))
    
        

