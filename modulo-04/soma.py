numeros = [
int(input("Informe o primeiro número: ")),
int(input("Informe o segundo número: ")),
int(input("Informe o terceiro número: ")),
int(input("Informe o quarto número: ")),
int(input("Informe o quinto número: "))]
soma = 0
for numero in numeros:
	soma += numero
print(soma)