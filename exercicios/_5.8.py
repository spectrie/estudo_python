users = ['marta', 'joão', 'tiago', 'admin', 'victor']

if users:
    for user in users:
        if user == 'admin':
            print('Olá administrador, gostária de um relatório de status?')
        else:
            print(f"Olá {user}, obrigado por fazer login novamente.")
else:
    print("É necessário encontrar alguns usuários;")