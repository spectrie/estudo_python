current_users = ['marta', 'joão', 'tiago', 'maria', 'victor']

new_users = ['vinicius', 'JOÃO', 'eduardo', 'laysa', 'Victor']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Nome de usuário em uso, forneça um novo nome.")
    else:
        print("Nome de usuário disponível")