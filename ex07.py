if __name__ == '__main__':
    n = int(input('Digite um valor: '))
    for c in range(0, 11):
        t = n * c
        print('({} X {} = {}) '.format(c, n, t), end='')
