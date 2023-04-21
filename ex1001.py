#Leia 2 valores inteiros  e armazene-os nas variaveis A e B. Efetue  a soma de A e B atribuindo o seu resultado na
#variavel X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que etá sendo
#especificado e não esqueça de imprimir o fim da linha após o resultado, caso contrário você receberá "Presentation Error"

if __name__ == '__main__':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    x = a + b
    print('X = {} '.format(x))
