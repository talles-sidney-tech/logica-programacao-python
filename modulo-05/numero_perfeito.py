def numero_perfeito(n):
    n = abs(int(n))
    perfeito = 0
    
    for x in range(1, n):
        if n % x == 0:
            perfeito += x
    
    return perfeito == n
print(numero_perfeito(6))