# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir,
# calcule e mostre o valor da conta a pagar.

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

# Exemplo de Entrada	Exemplo de Saída
# 3 2Total:             R$ 10.00

if __name__ == '__main__':
    v = input('Digite o codigo do item e a quantidade separado por espaço: ').split()
    c, q = int(v[0]), int(v[1])

    c1 = float(4.00)
    c2 = float(4.50)
    c3 = float(5.00)
    c4 = float(2.00)
    c5 = float(1.50)

    if c == 1:
        t = q * c1
    elif c == 2:
        t = q * c2
    elif c == 3:
        t = q * c3
    elif c == 4:
        t = q * c4
    elif c == 5:
        t = q * c5
    else:
        print('Opção inválida, Digite um codigo valido')

    print('Total a pagar: R$ {:.2F} '.format(t))
