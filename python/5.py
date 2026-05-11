def media(notas, qtd_notas):
    notas_somadas = sum(notas)
    media = notas_somadas / qtd_notas
    return media

print('==-==' * 10)
print('Média Escolar')
print('==-==' * 10)

while True: # motor infinito
    try: # validação de numeros inteiros
        notas = []
        qtd_notas = int(input('Digite a quantidade total de notas:  '))
        if qtd_notas <= 0: # validação de números negativos e 0
            if qtd_notas == 0:
                print(f'Garanto que você não teve {qtd_notas} notas. Tente novamente.')
            elif qtd_notas <= 0:
                print(f'ERRO, {qtd_notas} é um número negativo. Tente novamente.')
            continue # volta para o começo 
        for nota in range(qtd_notas):
            notas.append(float(input(f'Digite a nota {nota + 1}: ')))
        break # sai do loop
    except ValueError:
        print('ERRO, digite um número válido.')

media_final = media(notas, qtd_notas)

print(f'Você teve {qtd_notas} notas, que foram: ')
print(notas)
print(f'Sua média final é {media_final:.2f}.')