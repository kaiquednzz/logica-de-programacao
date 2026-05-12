from datetime import date

def nascimento(ano_nascimento):
    nascimento = date.today().year - ano_nascimento
    return nascimento

print('==-==' * 2)
print('Sua Idade')
print('==-==' * 2)

while True:
    try:
        ano_nascimento = int(input('Digite seu ano de nascimento: '))
        if ano_nascimento > date.today().year:
            print(f'Digite um ano anterior à {date.today().year}.')
            continue

        idade = nascimento(ano_nascimento)
        print(f'Você têm {idade} anos de idade!')
        break
    except ValueError:
        print('ERRO! Digite um valor válido.')