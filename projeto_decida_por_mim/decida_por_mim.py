import random

def responder(respostas):
    resposta = random.choice(respostas)
    return resposta

print('DECIDA POR MIM')
print('Faça uma pergunta e eu te darei uma resposta!')
print('(São válidas somente perguntas cujas respostas podem ser sim ou não)')

respostas = [
    'Não me restam dúvidas!', 
    'Absolutely!', 
    'Dias de luta!', 
    'Dias de glória!', 
    'Pelo amor de Deus!', 
    'Não!', 
    'Ah, pronto!', 
    'Sim', 
    'É...' ,
    'Boto fé!',
    'É sobre!',
    'Será?',
    'Viva la vida!',
    'Carpe diem!',
    'Arrasou!',
    'Lacre!'
]

opcoes = ['p', 's']

while True:

    print()
    
    entrada = input('O que deseja? [p] perguntar [s] sair? => ')

    if entrada not in opcoes:
        print('Digite uma opção válida!')
        continue

    if entrada == 'p':
        pergunta = input('Faça a sua pergunta => ')
        
        if pergunta[-1] != '?':
            print('Faça uma pergunta válida!')
            continue

        resposta = responder(respostas)
        print(resposta)

    if entrada == 's':
        break
