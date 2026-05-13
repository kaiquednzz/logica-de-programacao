from time import sleep
import random

print('--=' * 8)
print('Pedra, Papel e Tesoura')
print('--=' * 8)
sleep(1)
print('Escolha:')
sleep(0.5)
print('Pedra')
sleep(0.5)
print('Papel')
sleep(0.5)
print('Tesoura')
sleep(0.5)

escolhas = ['pedra', 'papel', 'tesoura']
pontos_user = 0
pontos_bot = 0

for c in range(3):
    escolha_bot = random.choice(escolhas)
    escolha_user = str(input('Sua jogada: '))
    sleep(0.5)
    escolha_user = escolha_user.lower()
    if escolha_user not in escolhas:
        print('Escolha Pedra, Papel, ou Tesoura.')
        continue

    if escolha_user == 'pedra' and escolha_bot == 'pedra':
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Empate.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)
    
    elif escolha_user == 'pedra' and escolha_bot == 'papel':
        pontos_bot += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Derrota.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'pedra' and escolha_bot == 'tesoura':
        pontos_user += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Vitória.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'papel' and escolha_bot == 'pedra':
        pontos_user += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Vitória.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'papel' and escolha_bot == 'papel':
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Empate.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'papel' and escolha_bot == 'tesoura':
        pontos_bot += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Derrota.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'tesoura' and escolha_bot == 'pedra':
        pontos_bot += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Derrota.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'tesoura' and escolha_bot == 'papel':
        pontos_user += 1
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Vitória.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

    elif escolha_user == 'tesoura' and escolha_bot == 'tesoura':
        print(f'Escolha do bot: {escolha_bot}.')
        sleep(1)
        print(f'{c + 1} rodada: Empate.')
        sleep(1)
        print(f'Seus pontos: {pontos_user} | Pontos do bot {pontos_bot}.')
        sleep(1)

if pontos_user > pontos_bot:
    print('Parabéns! Você venceu.')

elif pontos_user == pontos_bot:
    print('Ops... Deu empate.')

else:
    print('F...')