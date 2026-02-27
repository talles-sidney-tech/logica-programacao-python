def testa_primo(n):
    n = abs(int(n))
    if n == 1 or n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for x in range(3, n):
        if n % x == 0:
            return False
    
    return True
print(testa_primo(1))