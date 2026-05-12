from datetime import date

print('-=' * 10)
print('Par ou Ímpar 3x')
print('-=' * 10)

for c in range(3):
    while True:
        try:
            numero = int(input('Digite um número: '))
            if numero % 2 == 0:
                print(f'O número {numero} é par!')
            else:
                print(f'O número {numero} é impar!')
            break
        except ValueError:
            print('ERRO! Digite um valor válido.')