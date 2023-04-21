# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir,
# determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

# Se o ponto estiver na origem, escreva a mensagem “Origem”.

# Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

# Entrada
# A entrada contem as coordenadas de um ponto.

# Saída
# A saída deve apresentar o quadrante em que o ponto se encontra.

# Exemplo de Entrada	Exemplo de Saída
# 4.5 -2.2              Q4

if __name__ == '__main__':
    v = input('Digite dois valores separando-os com um espaço: ').split()
    x, y = float(v[0]), float(v[1])

    if x > 0 and y > 0:
        print('Os valores estão no primeiro quadrante! ')
    elif x < 0 and y > 0:
        print('Os valores estão no segundo quadrante! ')
    elif x < 0 and y < 0:
        print('Os valores estão no terceiro quadrante! ')
    elif x > 0 and y < 0:
        print('Os valores estão no quarto quadrante! ')
    elif x == 0 and y == 0:
        print('os valores estão na origem! ')
    elif x == 0 or y == 0:
        print('Um dos valores estão sobre um dos eixos! ')
