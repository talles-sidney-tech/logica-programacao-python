numeros = [
int(input("Informe o primeiro número")),
int(input("Informe o segundo número")),
int(input("Informe o terceiro número")),
int(input("Informe o quarto número")),
int(input("Informe o quinto número")),
int(input("Informe o sexto número")),
int(input("Informe o sétimo número")),
int(input("Informe o oitavo número")),
int(input("Informe o nono número")),
int(input("Informe o décimo número")),
]

numero = int(input("Informe um número para pesquisar: "))

if numero in numeros:
    print(f"O número {numero} existe na lista")
else:
    print(f"O número {numero} não existe na lista.")