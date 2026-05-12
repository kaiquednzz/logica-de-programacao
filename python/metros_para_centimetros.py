def conversor(valor_metro): #função conversor
    centimetro = valor_metro * 100
    return centimetro

print('==-==' * 10)
print('Conversor de Metros para Centímetros')
print('==-==' * 10)

while True: #"motor" infinito
    try: #validação de números
        valor_metro = float(input(f'Digite um valor em metro: '))
        if valor_metro <= 0:
            print(f'ERRO! Digite um valor maior que 0.')
            continue #volta para o início
        break #sai do loop
    except ValueError:
        print(f'Erro! Digite um número válido.')

valor_centimetros = conversor(valor_metro)
print(f'{valor_metro}m  são {valor_centimetros}cm!')