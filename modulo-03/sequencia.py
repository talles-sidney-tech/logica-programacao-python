termos = int(input("Informe um número: "))
while termos < 3:
	print("O número de termos deve ser no mínimo 3")
	termos = int(input("Informe um número: "))
termo1, termo2, i = 1,1, 0
print(termo1)
print(termo2)
while i < termos - 2:
	resultado = termo1 + termo2
	print(resultado)
	termo2, termo1 = resultado, termo2
	i += 1