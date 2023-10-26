import random


def sortear():
    numero_sorteado = random.randint(1, 6)
    return numero_sorteado

def checar(nro_lancamentos):
    if nro_lancamentos <= 1:
        print('Lance o dado pelo menos duas vezes!')
        return False
    
    return True

def maior_sorteado(valor, maior):
    if valor > maior:
        maior = valor
    return maior    

def menor_sorteado(valor, menor):
    if valor < menor:
        menor = valor
    return menor


texto = """
SIMULADOR DE DADO

[l] lançar o dado
[m] exibir o mínimo sorteado
[M] exibir o máximo sorteado
[s] sair

=> """

opcoes = ['l', 'm', 'M', 's']
nro_lancamentos = 0

while True:
    opcao = input(texto)
    print()

    if opcao not in opcoes:
        print('Opção inválida!')
        continue

    if opcao == 'l':
        numero_sorteado = sortear()
        nro_lancamentos += 1

        if nro_lancamentos == 1:
            menor = numero_sorteado
            maior = numero_sorteado        

        print(f'O número sorteado foi {numero_sorteado}.')
        maior = maior_sorteado(numero_sorteado, maior)
        menor = menor_sorteado(numero_sorteado, menor)

    if opcao == 'm':
        if checar(nro_lancamentos):
            print(f'O menor valor sorteado foi {menor}.')

        continue    

    if opcao == "M":
        if checar(nro_lancamentos):
            print(f'O maior valor sorteado foi {maior}.')

        continue

    if opcao == "s":
        break

print(f'O dado foi lançado {nro_lancamentos} vezes.')
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')    