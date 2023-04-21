# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.
#Entrada
#O arquivo de entrada contém três valores com um dígito após o ponto decimal.

#Saída
#O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com
# mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígito
# após o ponto decimal.

#Exemplos de Entrada	Exemplos de Saída
#3.0 4.0 5.2            TRIANGULO: 7.800
#                       CIRCULO: 84.949
#                       TRAPEZIO: 18.200
#                       QUADRADO: 16.000
#                       RETANGULO: 12.000

if __name__ == '__main__':
    v = input('Digite três valores em sequencia dando um espaço entre eles: ').split()
    a, b, c = float(v[0]), float(v[1]), float(v[2])
    tri = a * c / 2
    cir = c ** 3 * 3.14159
    tra = (a + b) * c / 2
    qua = b * b
    ret = a * b
    print('TRIANGULO : {:.3f}'.format(tri))
    print('CIRCULO : {:.3f}'.format(cir))
    print('TRAPEZIO : {:.3f}'.format(tra))
    print('QUADRADO : {:.3f}'.format(qua))
    print('RETANGULO : {:.3f}'.format(ret))
