if __name__ == '__main__':
    soma = 0
    quantidade = 0
    positivos = 0
    negativos = 0
    while True:
        v = int(input('Digite um valor: '))
        sair = input('Se deseja encerrar tecle (ENTER)')
        soma += v
        quantidade += 1
        if v >= 0:
            positivos += 1
        else:
            negativos += 1
        if sair in 'enter':
            break
    media = soma / quantidade
    percentuualPositivos = positivos*100/quantidade
    percentualNegativos = negativos*100/quantidade
    print('Média: {:.2f}'.format(media))
    print('Positivos: ', positivos)
    print('Negativos: ', negativos)
    print('% de positivos:{:.0f} '.format(percentuualPositivos))
    print('% de negativos:{:.0f} '.format(percentualNegativos))
