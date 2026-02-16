n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))
n4 = int(input("Informe o quarto número: "))
n5 = int(input("Informe o quinto número: "))
maior = n1
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
	maior = n2
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
	maior = n3
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
	maior = n4
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
	maior = n5
print(f"O maior número informado é {maior}")