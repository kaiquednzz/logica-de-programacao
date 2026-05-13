"""
Crie um sistema de cadastro de usuários.
"""
from time import sleep

print('--=' * 8)
print('Cadastro de Usuários')
print('--=' * 8)
sleep(1.5)

usuarios = []
while True:
    try:
        print('1 - Adicionar | 2 - Listar | 3 - Atualizar | 4 - Remover | 5 - Sair')
        sleep(0.5)
        escolha = int(input('Digite sua escolha: '))

        if escolha == 1:
            usuario = input('Digite o nome do usuário: ')
            usuario = usuario.strip()
            usuario = usuario.capitalize()
            usuarios.append(usuario)
            
        elif escolha == 2:
            for usuario in usuarios:
                print(f'{usuarios.index(usuario) + 1} - {usuario}')
                sleep(0.25)

        elif escolha == 3:
            print(usuarios)

        elif escolha == 4:
            print(usuarios)

    except ValueError:
        print('ERRO! Digite uma opção válida.')