print ('--=' * 8)
print('Média de Valores')
print ('--=' * 8)

while True:
    try:
        qtd_numeros = int(input('Digite a quantidade de números: '))
        if qtd_numeros <= 0:
            print('ERRO! Digite um valor maior que 0.')
            continue
        break
    except ValueError:
        print('ERRO! Digite um valor válido.')

numeros = []
while True:
    try:
        for contador in range(qtd_numeros):
            numero = float(input(f'Digite o {contador + 1} número: '))
            numeros.append(numero)
    except ValueError:
        print('ERRO! Digite um valor válido.')
        continue
    break

soma_numeros = sum(numeros)
media = soma_numeros / qtd_numeros
print(f'A média é {media}.')    