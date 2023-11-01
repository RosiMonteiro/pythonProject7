import random
print('''Bem-vindo ao Tabuadex! 
O objetivo é responder corretamente a multiplicação de 7 pelo número gerado abaixo para ganhar pontos.''')

ponto = 0
soma = 0
tabuada = 7

sair = False
while sair == False:

    n = random.randint(0, 10)
    print(n)
    computador = n * tabuada

    escolha = input('Jogar ou sair?')

    if escolha == 'sair':
        sair = True
        print('Até a Próxima!!!')
        break

    if escolha == 'jogar':
        jogar = input('Resutado de 7 * n: ')
        print("Você digitou: ", jogar)
        jogada = int(jogar)

        if jogada == computador:
            print('Parabéns!!!')
            soma += ponto + 10
            print('Você já conseguiu {} pontos '.format(soma))

        elif jogada != computador:
            print('Que pena, você errou!')

print('FIM DO JOGO!!!')
