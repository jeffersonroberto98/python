entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    num = int(entrada)
    par_impar = num % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {num} é {par_impar_texto}')

else:
    print('Você não digitou um número inteiro.')