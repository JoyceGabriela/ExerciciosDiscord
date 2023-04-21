if __name__ == '__main__':
    maiorA = 0
    menorA = 3
    for c in range(1, 5):
        altura = float(input('Digite altura {}: '.format(c)))
        if altura > maiorA:
            maiorA = altura
        if altura < menorA:
            menorA = altura
    print('=' * 20)
    print('Maior altura:{} '.format(maiorA))
    print('Menor altura:{} '.format(menorA))
    print('=' * 20)
