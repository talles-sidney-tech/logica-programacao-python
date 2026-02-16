numeros = [
int(input("Informe o primeiro número: ")),
int(input("Informe o segundo número: ")),
int(input("Informe o terceiro número: ")),
int(input("Informe o quarto número: ")),
int(input("Informe o quinto número: ")),
int(input("Informe o sexto número: ")),
int(input("Informe o sétimo número: ")),
int(input("Informe o oitavo número: ")),
int(input("Informe o nono número: ")),
int(input("Informe o décimo número: ")),
]
pares = []
impares = []
for numero in numeros:
	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")