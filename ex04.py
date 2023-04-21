if __name__ == '__main__':
    a0_25 = 0
    b26_50 = 0
    c51_75 = 0
    d76_100 = 0
    n = 0
    #while n >= 0:
    while True:
        n = int(input('Digite um valor: '))
        if n > 100:
            print('Valor inválido! Digite um valor entre 0 e 100!')
        elif n >= 0 and n <= 25:
            a0_25 += 1
        elif n >= 26 and n <= 50:
            b26_50 += 1
        elif n >= 51 and n <= 75:
            c51_75 += 1
        elif n >= 76 and n <= 100:
            d76_100 += 1
        if n < 0:
            break
    print('')
    print('#'*45)
    print('O intervalo 0 até 25 recebeu: {} valor(es)'.format(a0_25))
    print('O intervalo 26 até 50 recebeu: {} valor(es)'.format(b26_50))
    print('O intervalo 51 até 75 recebeu: {} valor(es)'.format(c51_75))
    print('O intervalo 76 até 100 recebeu: {} valor(es)'.format(d76_100))
    print('#'*45)
