numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))
if numero1 > numero2:
	numero1, numero2 = numero2, numero1
if numero1 > numero3:
	numero1, numero3 = numero3, numero1
if numero2 > numero3:
	numero2, numero3 = numero3, numero2
print(f"O menor número informado é {numero1} e o maior número informado é {numero3}")