numero = int(input("Informe um número inteiro: "))
fatorial = 1
while numero > 1:
	fatorial *= numero
	numero -= 1
print("O resultado do fatorial é:", fatorial)