import random

numero_sorteado = random.randint(0, 20)

print('CHUTE UM NÚMERO')
print('Você tem três chances para acertar o valor!')

numero_chances = 1

while numero_chances <= 3:

    print()
    print(f'{numero_chances}ª TENTATIVA')
    entrada = input('Digite um número inteiro de 0 a 20 => ')
    
    print()

    if entrada.isdigit() is not True:
        print('Digite apenas números!')
        continue
        
    entrada = int(entrada)
    entrada_fora_intervalo = entrada < 0 or entrada > 20

    if entrada_fora_intervalo:
        print('Digite um número dentro do intervalo [0, 20]!')
        continue

    if entrada == numero_sorteado:
        print('PARABÉNS! Você acertou!')
        break

    if entrada > numero_sorteado:
        print('O número sorteado é menor que o digitado.')
    else:
        print('O número sorteado é maior que o digitado.')    
    
    intervalo = abs(numero_sorteado - entrada)

    intervalo_grande = intervalo >= 14
    intervalo_medio = intervalo >= 6 and intervalo < 14
    intervalo_pequeno = intervalo >= 1 and intervalo < 6

    print()

    numero_chances += 1

    if numero_chances == 4:
        print('Você perdeu!')
        print(f'O número sorteado foi {numero_sorteado}.')
        break

    if intervalo_grande:
        print('Tá frio.')

    if intervalo_medio:
        print('Tá queeente...')

    if intervalo_pequeno:
        print('TÁ PEGANDO FOGO!')        