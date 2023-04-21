if __name__ == '__main__':
    num = int(input('Digite um número para\ncalcular seu fatorial: '))
    print('{}! ='.format(num), end='')
    resultado = 1
    for c in range(num, 0, -1):
        resultado *= c
        print(' {} '.format(c), end='')
        print('x' if c > 1 else '=', end='')
    print(' {}'.format(resultado))