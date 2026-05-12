while True:
    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        break
    except:
        print('ERRO, digite um número válido.')
soma = num1 + num2
print(f'A soma entre {num1} e {num2} é {soma}.')