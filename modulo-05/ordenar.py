def funcao(colecao):
    metade = len(colecao) // 2
    print(colecao[metade:] + colecao[:metade])
funcao([1, 2, 3, 4, 5])