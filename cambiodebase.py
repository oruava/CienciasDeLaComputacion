def base_a_decimal(numero, base):
    valor_decimal = 0
    for i, digito in enumerate(reversed(numero)):
        valor_decimal += int(digito) * (base ** i)
    return valor_decimal

def decimal_a_base(numero_decimal, base):
    if numero_decimal == 0:
        return '0'
    digitos = []
    while numero_decimal:
        digitos.append(int(numero_decimal % base))
        numero_decimal //= base
    return ''.join(str(x) for x in digitos[::-1])

def cambio_de_base(numero, base_origen, base_destino):
    valor_decimal = base_a_decimal(numero, base_origen)
    return decimal_a_base(valor_decimal, base_destino)


numero = '1011'
base_origen = 2
base_destino = 16

resultado = cambio_de_base(numero, base_origen, base_destino)
print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}.")
