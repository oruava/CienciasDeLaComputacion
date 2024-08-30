def exponenciacion_rapida(base, exponente, modulo):
    resultado = 1
    base = base % modulo
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo
    return resultado

base = 3
exponente = 13
modulo = 7
print(f"{base}^{exponente} mod {modulo} = {exponenciacion_rapida(base, exponente, modulo)}")
