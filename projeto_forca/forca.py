import random


def escolher(lista):
    escolha = random.choice(lista)
    return escolha


categorias = {
    'animais': [
        'chinchila', 'ornitorrinco', 'escaravelho', 'hamster', 'rouxinol', 'bacalhau', 'lhama',
        ],
    'objetos': [
        'ampulheta', 'almofariz', 'candelabro', 'nebulizador', 'desfibrilador', 'vuvuzela', 'novelo',
        ],
    'frutas': [
        'bergamota', 'nectarina', 'groselha', 'jenipapo', 'jabuticaba', 'pitaya', 'seriguela',
        ],
}

categoria = escolher(list(categorias.keys()))
palavra = escolher(categorias[categoria])
palavra_formada = '_' * len(palavra)
letras_acertadas = ''
tentativas = 1

print('JOGO DA FORCA')
print('Adivinhe a palavra em 6 tentativas!')
print()
print(f'A categoria é {categoria.upper()}: {palavra_formada}')

while tentativas <= 6:

    print()
    letra_digitada = input(
        'Digite uma letra \n(Caso queira sair digite "sair"): '
    ).lower()

    if letra_digitada == 'sair':
        print('Saindo...')
        break

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    else:
        print()
        print(f'A palavra não tem a letra {letra_digitada}! Resta(m) {6 - tentativas} tentativa(s).')
        tentativas += 1    

    if tentativas > 6:
        print()
        print('Que pena! Não foi dessa vez...')
        print(f'A palavra era {palavra}.')

    palavra_formada = ''

    for letra in palavra:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '_'

    print()
    print(palavra_formada)

    if palavra_formada == palavra:
        print('PARABÉNS! Você ganhou o jogo!')
        break

    print()
    palpite = input('Tente adivinhar a palavra: ').lower()

    if palpite == palavra:
        print()
        print('PARABÉNS! Você ganhou o jogo!')
        break
