import random

pontuacao_maquina = 0
pontuacao_usuario = 0

texto = '''
Vamos lá! Digite uma opção:

Pedra
Papel
Tesoura
Sair

=> '''

menu = ['pedra', 'papel', 'tesoura', 'sair']
mensagem_vitoria = 'Você ganhou!'
mensagem_derrota = 'Você perdeu!'

print('Pedra, Papel, Tesoura...')

while True:
    jogada_usuario = input(texto).lower()
    print()

    if jogada_usuario not in menu:
        print('Digite uma opção válida!')
        continue

    if jogada_usuario == 'sair':
        print('Saindo do jogo...')
        break

    jogada_maquina = random.choice(['pedra', 'papel', 'tesoura'])
    print(f'Você jogou {jogada_usuario}!')
    print(f'A máquina jogou {jogada_maquina}!')
    print()

    if jogada_usuario == jogada_maquina:
        print('Jogue novamente!')
        continue

    if jogada_usuario == 'pedra':
        if jogada_maquina == 'papel':
            print(mensagem_derrota)
            pontuacao_maquina += 1
            continue

        print(mensagem_vitoria)
        pontuacao_usuario += 1

    if jogada_usuario == 'papel':
        if jogada_maquina == 'pedra':
            print(mensagem_vitoria)
            pontuacao_usuario += 1
            continue

        print(mensagem_derrota)
        pontuacao_maquina += 1

    if jogada_usuario == 'tesoura':
        if jogada_maquina == 'papel':
            print(mensagem_vitoria)
            pontuacao_usuario += 1
            continue

        print(mensagem_derrota)
        pontuacao_maquina += 1

print()
if pontuacao_usuario > pontuacao_maquina:
    print('PARABÉNS! Você ganhou o jogo!')
elif pontuacao_usuario == pontuacao_maquina:
    print('Houve um empate!')
else:
    print('Que pena! Você perdeu o jogo!')

print()
print(f'A sua pontuação foi {pontuacao_usuario}!')
print(f'A pontuação da máquina foi {pontuacao_maquina}!')