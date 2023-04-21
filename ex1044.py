#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
# indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

# Exemplo de Entrada	Exemplo de Saída
# 6 24                  Sao Multiplos

if __name__ == '__main__':
    v = input('Digite dois valores iteiros: ').split()
    a, b = int(v[0]), int(v[1])

    if b % a == 0:
        print('São multiplos! ')
    else:
        print('Não são multiplos! ')
