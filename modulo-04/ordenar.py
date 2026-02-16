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
continua = True
while continua:
	continua = False
	if numeros[0] > numeros[1]:
		numeros[0], numeros[1] = numeros[1], numeros[0]
		continua = True
	if numeros[1] > numeros[2]:
		numeros[1], numeros[2] = numeros[2], numeros[1]
		continua = True
	if numeros[2] > numeros[3]:
		numeros[2], numeros[3] = numeros[3], numeros[2]
		continua = True
	if numeros[3] > numeros[4]:
		numeros[3], numeros[4] = numeros[4], numeros[3]
		continua = True
	if numeros[4] > numeros[5]:
		numeros[4], numeros[5] = numeros[5], numeros[4]
		continua = True
	if numeros[5] > numeros[6]:
		numeros[5], numeros[6] = numeros[6], numeros[5]
		continua = True
	if numeros[6] > numeros[7]:
		numeros[6], numeros[7] = numeros[7], numeros[6]
		continua = True
	if numeros[7] > numeros[8]:
		numeros[7], numeros[8] = numeros[8], numeros[7]
		continua = True
	if numeros[8] > numeros[9]:
		numeros[8], numeros[9] = numeros[9], numeros[8]
		continua = True
print(f"Menor: {numeros[0]}")
print(f"Maior: {numeros[9]}")