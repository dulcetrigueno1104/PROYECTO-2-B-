import random

def validar_adn(cadena_adn):
    """Valida que la cadena de ADN contenga solo caracteres válidos (A, T, C, G) y tenga al menos 13 caracteres"""
    if len(cadena_adn) < 13 or not all(base in 'ATCG' for base in cadena_adn):
        return False
    return True

def generar_adn_aleatorio(longitud):
    """Genera una cadena de ADN aleatoria de una longitud dada"""
    bases = ['A', 'T', 'C', 'G']
    cadena_adn = ""
    for _ in range(longitud):
        cadena_adn += random.choice(bases)
    return cadena_adn
