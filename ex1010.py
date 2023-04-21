# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de
# uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um
# valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos
# e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

# Exemplos de Entrada	Exemplos de Saída
# 12 1 5.30             VALOR A PAGAR: R$ 15.50
# 16 2 5.10

if __name__ == '__main__':
    p1 = input("Digite o código da peça 1, o número de peças e o valor unitário: ").split()
    c1, n1, v1 = int(p1[0]), int(p1[1]), float(p1[2])

    p2 = input("Digite o código da peça 2, o número de peças e o valor unitário: ").split()
    c2, n2, v2 = int(p2[0]), int(p2[1]), float(p2[2])

    t = (n1 * v1) + (n2 * v2)

    print('VALOR A PAGAR = R$ {:.2f}'.format(t))
