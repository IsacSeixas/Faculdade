from calculadora import Calculadora

def main():
    calculadora = Calculadora()

    a = float(input('Numero 1: '))
    b = float(input('Numero 2: '))
    op = input('Operação? (escolha: * - + /): ')

    mais = '+'
    menos = '-'
    multi = '*'
    div = '/'

    if op == mais:
        resultado = calculadora.somar(a, b)
        print('Soma: ', resultado)
    elif op == menos:
        resultado = calculadora.sub(a, b)
        print('subtração: ', resultado)
    elif op == multi:
        resultado = calculadora.multiplicacao(a, b)
        print('multiplicação: ', resultado)
    elif op == div:
        resultado = calculadora.divi(a, b)
        print('divisão: ', round(resultado, 2))
    else:
        print('Operação invalida')


if __name__ == "__main__":
    main()
