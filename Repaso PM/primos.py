import math

x = int(input("Dame un numero:   "))

def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    limite = int(math.sqrt(n) + 1)
    for i in range (3, n, 2):
        if n % i == 0:
            return False
        return True
    
print("Primo" if es_primo(x) else "No Primo")
