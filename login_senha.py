#Pedido de informacao de dados pro usuario
login = input("Olá digite o login de usuario que voce deseja cadastrar: ")
senha = input("Agora, digite a senha de usuario que voce deseja cadastrar: ")

#Teste de validacao
tentativa_login = input("Ola, digite o seu usuario: ")
while tentativa_login != login:
    tentativa_login = input("Usuario invalido. \n Tente novamente: ")
if tentativa_login == login:
    tentativa_senha = input("Agora, digite sua senha: ")
    while tentativa_senha != senha:
        tentativa_senha = input("Senha ivalida. \n Tente novamente: ")
    if tentativa_senha == senha:
        print("BEM VINDO!!!")