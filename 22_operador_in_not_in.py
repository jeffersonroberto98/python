# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = "Jefferson"

# print(nome[2])

# print('J' in nome)
# print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite a letra que deseja encontrar dentro do nome: ')

if encontrar in nome:
    print(f'A letra "{encontrar}" está dentro de "{nome}"!')
else:
    print(f'A letra "{encontrar}" não está dentro de "{nome}"!')