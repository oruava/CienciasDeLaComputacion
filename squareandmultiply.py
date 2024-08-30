def square_and_multiply(a, n, mod):
    binario_n = bin(n)[2:]
    b = a

    for numero in binario_n[1:]:
        b = (b ** 2) % mod
        if numero == '1':
            b = (b * a) % mod

    return b


N = 7
resultado = square_and_multiply(N, 13, 17)
print(f"{N}^13 mod 17 = {resultado}")
