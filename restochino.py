def mcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    mcd, x1, y1 = mcd_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return mcd, x, y

def inverso_modular(a, m):
    mcd, x, y = mcd_extendido(a, m)
    if mcd != 1:
        raise ValueError("No existe un inverso multiplicativo")
    else:
        return x % m

def teorema_del_resto_chino(restos, modulos):
    producto_total = 1
    for modulo in modulos:
        producto_total *= modulo

    resultado = 0
    for resto, modulo in zip(restos, modulos):
        producto_parcial = producto_total // modulo
        inverso = inverso_modular(producto_parcial, modulo)
        resultado += resto * producto_parcial * inverso

    return resultado % producto_total

restos = [2, 3, 1]
modulos = [3, 4, 5]

resultado = teorema_del_resto_chino(restos, modulos)
print(f"El resultado del sistema de ecuaciones es: {resultado}")
