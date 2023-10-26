from cryptography.fernet import Fernet


# Trecho a ser implementado durante a primeira execução do código na máquina/ambiente
# A fim de gerar o arquivo chave.key
'''def escrever_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)


escrever_chave()'''


def carregar_chave():
    arquivo = open('chave.key', 'rb')
    chave = arquivo.read()
    arquivo.close()
    return chave


chave = carregar_chave()
fer = Fernet(chave)


def adicionar():
    nome = input('Usuário: ')
    senha = input('Senha: ')

    with open('senhas.txt', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{nome} | {fer.encrypt(senha.encode()).decode()}\n')


def visualizar():
    with open('senhas.txt', 'r', encoding='utf8') as arquivo:
        for linha in arquivo.readlines():
            dado = linha.strip()
            usuario, senha = dado.split('|')
            print(f'Usuário: {usuario} | Senha: {fer.decrypt(senha.encode()).decode()}')


texto = '''
Do que gostaria?

[a] Adicionar uma nova senha
[v] Visualizar as senhas existentes
[s] Sair

=> '''

menu = ['a', 'v', 's']

while True:
    modo = input(texto).lower()

    if modo not in menu:
        print('Digite uma opção válida!')
        continue

    if modo == 's':
        print('Saindo do programa...')
        break

    if modo == 'a':
        adicionar()
    
    if modo == 'v':
        visualizar()