# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
# Utilize a fórmula:

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

# Exemplos de Entrada	Exemplos de Saída
#7 14 106               106 eh o maior

if __name__ == '__main__':
    v = input('Digite três valores em sequência dando um espaço entre eles: ').split()
    a, b, c = int(v[0]), int(v[1]), int(v[2])
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    print('{} eh o maior'.format(maior))
