#Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e
# calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia =

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a
# segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 1.0 7.0               4.4721
# 5.0 9.0

if __name__ == '__main__':

    p1 = input('Digite dois valores em sequência separando-os com um espaço : ').split()
    x1, y1 = float(p1[0]), float(p1[1])

    p2 = input('Digite outros dois valores em sequência separando-os com um espaço : ').split()
    x2, y2 = float(p2[0]), float(p2[1])

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

    print('{:.4f}'.format(d))
