import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factores_primos(m):
    factores = []
    for i in range(2, int(math.sqrt(m)) + 1):
        while m % i == 0:
            factores.append(i)
            m //= i
    if m > 1:
        factores.append(m)
    return factores

def totiente_de_euler(m):
    factores_unicos = set(factores_primos(m))
    resultado = m
    for p in factores_unicos:
        resultado *= (1 - 1/p)
    return int(resultado)

m = 36
print(f"El valor de la función Totiente de Euler para {m} es: {totiente_de_euler(m)}")
