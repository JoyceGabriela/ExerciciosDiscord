# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
# hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

# Entrada
# O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade
# de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

# Saída
# Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da
# igualdade. No caso do salário, também deve haver um espaço em branco após o $.

# Exemplos de Entrada	Exemplos de Saída
# 25                    NUMBER = 25
# 100                   SALARY = U$ 550.00
# 5.5


if __name__ == '__main__':
    m = int(input('Digite a matrícula do colaborador: '))
    h = int(input('Digite agora a quantidade de horas trabalhadas: '))
    v = float(input('Para finalizar digite o valor da hora trabalhada: '))
    s = h * v
    print('NUMBER = {}'.format(m))
    print('SALARY = U$ {:.2f}'.format(s))
