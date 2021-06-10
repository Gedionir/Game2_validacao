from random import randint
from time import sleep

print('================ GAME - PEDRA, PAPEL E TESOURA ================')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('=' * 63)
jogador = int(input('Qual é a sua jogada? '))
while jogador not in (0, 1, 2):
    jogador = int(input('Dados Inválidos. Qual é a sua jogada? '))
print('=' * 63)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {} '.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('\033[34m***** EMPATE *****')
    elif jogador == 1:
        print('\033[34m***** JOGADOR VENCEU *****')
    elif jogador == 2:
        print('\033[34m***** COMPUTADOR VENCEU *****')

elif computador == 1:
    if jogador == 0:
        print('\033[34m***** COMPUTADOR VENCEU *****')
    elif jogador == 1:
        print('\033[34m***** EMPATE *****')
    elif jogador == 2:
        print('\033[34m***** JOGADOR VENCEU *****')

elif computador == 2:
    if jogador == 0:
        print('\033[34m***** JOGADOR VENCEU *****')
    elif jogador == 1:
        print('\033[34m***** COMPUTADOR VENCEU *****')
    elif jogador == 2:
        print('\033[34m***** EMPATE *****')

print('\n\033[m======================== FIM DO GAME ==========================')
