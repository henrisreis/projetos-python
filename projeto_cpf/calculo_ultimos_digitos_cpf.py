def calculo_digito(cpf):
    soma_produto = 0
    contador = len(cpf) + 1
    for digito in cpf:
        soma_produto += int(digito) * contador
        contador -= 1

    resultado = (soma_produto * 10) % 11
    digito_calculado = resultado if resultado <= 9 else 0
    return digito_calculado


while True:

    cpf_entrada = input('Digite um número de CPF (apenas números): ')
    cpf_inteiro = 0

    try:
        cpf_inteiro = int(cpf_entrada)
    except ValueError:
        print('Digite apenas números!')

    if len(cpf_entrada) > 11:
        print('Digite apenas 11 números!')
        continue

    digitos_repetidos = cpf_entrada == cpf_entrada[0] * len(cpf_entrada)

    if digitos_repetidos:
        print('Valor inválido! Foi digitada uma sequência de números repetidos!')
        continue

    cpf_nove_digitos = cpf_entrada[:9]
    penultimo_digito = calculo_digito(cpf_nove_digitos)
    print(f'O penúltimo digito do CPF é {penultimo_digito}.')

    cpf_dez_digitos = cpf_nove_digitos + str(penultimo_digito)
    ultimo_digito = calculo_digito(cpf_dez_digitos)
    print(f'O último digito do CPF é {ultimo_digito}.')

    cpf_gerado = cpf_dez_digitos + str(ultimo_digito)
    cpf_invalido = cpf_entrada != cpf_gerado 
    if cpf_invalido:
        print('O CPF fornecido é inválido!')
