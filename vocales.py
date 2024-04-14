def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado [letra] = 0
        resultado [letra] +=  1 
    return resultado
