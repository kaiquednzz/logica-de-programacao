"""
Descubra porcentagens.
"""
from time import sleep
def calculo_porcentagem(valor, porcentagem):
    porcento =  (porcentagem * valor) / 100
    return porcento

print('--=' * 8)
print('Porcentagem')
print('--=' * 8)
sleep(1)

while True:
    try:
        valor = float(input('Digite um valor: '))
        porcentagem = int(input('Digite a porcentagem: '))
        porcento = calculo_porcentagem(valor, porcentagem)
        print(f'{porcentagem}% de {valor} é {porcento}!')

    except ValueError:
        print('ERRO! Digite um valor válido.')
        