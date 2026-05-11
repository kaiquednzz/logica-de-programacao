from time import sleep

def celsius_to_farenheit(valor_celsius):
    farenheit = (valor_celsius * 1.8) + 32
    return farenheit

def farenheit_to_celsius(valor_farenheit):
    celsius = (valor_farenheit - 32) / 1.8
    return celsius

print('==-==' * 10)
print('Conversor de Celsius para Farenheit')
print('==-==' * 10)
sleep(1)

print('1 - Celsius para Farenheit')
print('2 - Farenheit para Celsius')
sleep(1)
while True:
    try:    
        escolha = int(input('Digite sua escolha: '))
        if escolha < 1 or escolha > 2:
            print('ERRO! Digite uma opção válida.')
            continue
        break
    except ValueError:
        print('ERRO! Digite um número válido.')

if escolha == 1:
    while True:
        try:
            sleep(0.5)
            valor_celsius = float(input('Digite um valor em Celsius: '))
            farenheit = celsius_to_farenheit(valor_celsius)
            print('Calculando...')
            sleep(0.5)
            print(f'{valor_celsius}°C são {farenheit:.1f}°F!')
            break
        except ValueError:
            print('ERRO! Digite um número válido.')



if escolha == 2:
    while True:
        try:
            sleep(0.5)
            valor_farenheit = float(input('Digite um valor em Farenheit: '))
            print('Calculando...')
            sleep(0.5)
            celsius = farenheit_to_celsius(valor_farenheit)
            print(f'{valor_farenheit}°F são {celsius:.1f}°C!')
            break
        except ValueError:
            print('ERRO! Digite um número válido.')