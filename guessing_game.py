secreto = 'olá'
digitadas = []
tentativas = 3

while True:

    if tentativas <= 0:
        print('Vc perdeu!')
        break

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Ops, apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Parabéns, esta letra existe')
    else:
        print('Que pena, não existe!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Parabéns, você ganhou!')
        break
    else:
        print(f'Que pena, a palavra está assim {secreto_temporario}')

    if letra not in secreto:
        tentativas -= 1


    