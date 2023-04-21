if __name__ == '__main__':
    a = int(input('Digite um valor inicial: '))
    r = int(input('Digite a razão: '))
    pa = a
    for c in range(1, 11):
        print('{} -> '.format(pa), end='')
        pa *= r
    print('FIM')
