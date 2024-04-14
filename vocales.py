def contar_vocales(mi_string):
    resultado = {}

    for letra in mi_string:
        if letra == "a":
            if 'a' not in resultado:
                resultado ['a'] = 0
        resultado ['a'] = resultado ['a'] + 1 
        if letra == "e":
            if 'e' not in resultado:
                resultado ['e'] = 0
            resultado ['e'] = resultado['e'] + 1
    if contar_a > 0:
        resultado ["a"] = contar_a
    if contar_e > 0:
        resultado ["e"] = contar_e
    return resultado
