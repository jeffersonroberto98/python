frase = 'aaaooo'

i = 0
letra_atual = ''
quantidade_da_letra_que_apareceu_mais_vezes_atual = 0
quantidade_da_letra_que_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_da_letra_que_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if quantidade_da_letra_que_apareceu_mais_vezes < quantidade_da_letra_que_apareceu_mais_vezes_atual:
        quantidade_da_letra_que_apareceu_mais_vezes = quantidade_da_letra_que_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
    i += 1

print(
    'A letra que apareceu mais vezes foi a letra: ' 
    f'{letra_que_apareceu_mais_vezes}, ela apareceu '
    f'{quantidade_da_letra_que_apareceu_mais_vezes}x.'
)