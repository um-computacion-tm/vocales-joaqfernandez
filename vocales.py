def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if 'a' not in resultado:
                resultado [letra] = 0
        resultado [letra] +=  1 
        if letra == "e":
            if 'e' not in resultado:
                resultado ['e'] = 0
            resultado ['e'] = resultado['e'] + 1
    if contar_a > 0:
        resultado ["a"] = contar_a
    if contar_e > 0:
        resultado ["e"] = contar_e
    return resultado
