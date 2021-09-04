import random

vencedor = ''

jogadaMaquina = random.randint(0,2)

if jogadaMaquina == 0:
    escolhaMaquina = 'Pedra'
elif jogadaMaquina == 1:
    escolhaMaquina = 'Papel'
else:
    escolhaMaquina = 'Tesoura'


jogadaDoUsuario = input('Pedra, Papel ou Tesoura?')

if escolhaMaquina == jogadaDoUsuario:
    vencedor = 'Empate'
elif escolhaMaquina == 'Papel' and jogadaDoUsuario == 'Pedra':
    vencedor = 'Máquina'
elif escolhaMaquina == 'Pedra' and jogadaDoUsuario == 'Tesoura':
    vencedor = 'Máquina'
elif escolhaMaquina == 'Tesoura' and jogadaDoUsuario == 'Papel':
    vencedor = 'Máquina'
else:
    vencedor = 'Usuário'


if vencedor == 'Empate':
    print('A jogada deu empate')
else: 
    print( 'Você venceu a máquina')

    
