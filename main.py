def calculate():
    operation = input('''
Digite o número correspondente a operação que você deseja fazer:
1 Adição
2 Subtração
3 Multiplicação
4 Divisão
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '1':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '4':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor rode o programa novamente')

    again()

def again():
    calc_again = input('''
Você deseja calcular novamente?
Digite Y para sim ou N para não.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais.')
    else:
        again()

calculate()