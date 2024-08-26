# Calculadora com while

while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ - * /): ')

    nums_validos = None

    n1_f = 0
    n2_f = 0

    try:
        n1_f = float(n1)
        n2_f = float(n2)
        nums_validos = True
    except:
        nums_validos = None

    if nums_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Você digitou um operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

    if operador == '+':
        print(f'O resultado da soma é {n1_f}+{n2_f}=', n1_f + n2_f)
    elif operador == '-':
        print(f'O resultado da subtração é {n1_f}-{n2_f}=', n1_f - n2_f)
    elif operador == '*':
        print(f'O resultado da multiplicação é {n1_f}*{n2_f}=', n1_f * n2_f)
    elif operador == '/':
        print(f'O resultado da divisão é {n1_f}/{n2_f}=', n1_f / n2_f)
    else:
        print('FIZ MERDA')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair:
        break