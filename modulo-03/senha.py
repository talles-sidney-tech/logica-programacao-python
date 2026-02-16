usuario = input("Informe o seu nome de usuário: ")
senha = input("Informe a senha: ")
while usuario == senha:
	print("O nome do usuário e a senha devem ser diferentes")
	usuario = input("informe o seu nome de usuário: ")
	senha = input("Informe a senha: ")