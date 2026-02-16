numeros = []
i = 0
while i < 5:
	entrada = int(input(f"{i + 1}. Informe um número: "))
	if entrada == 0:
		print("O número 0 não é permitido!")
		continue
	numeros.append(entrada)
	i += 1
while True:
	posicao = int(input("Qual posição deseja exibir? Informe 0 para sair: "))
	if posicao < 0 or posicao > 5:
		print("Informe uma posição de 1 a 5!")
		continue
	if posicao == 0:
		print("Obrigado! Volte sempre que quiser.")
		break
	print(numeros[posicao - 1])