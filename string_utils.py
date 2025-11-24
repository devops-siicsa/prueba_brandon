"""
Utilidades de cadenas para pruebas internas de Copilot.
String utilities for internal Copilot testing.
"""


def reverse_string(text):
    """
    Invierte una cadena de texto.
    Reverse a string.
    
    Args:
        text: Cadena a invertir
    
    Returns:
        La cadena invertida
    """
    return text[::-1]


def is_palindrome(text):
    """
    Verifica si una cadena es un palíndromo.
    Check if a string is a palindrome.
    
    Args:
        text: Cadena a verificar
    
    Returns:
        True si es palíndromo, False en caso contrario
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """
    Cuenta las vocales en una cadena.
    Count vowels in a string.
    
    Args:
        text: Cadena a analizar
    
    Returns:
        Número de vocales en la cadena
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def capitalize_words(text):
    """
    Capitaliza la primera letra de cada palabra.
    Capitalize the first letter of each word.
    
    Args:
        text: Cadena a capitalizar
    
    Returns:
        Cadena con cada palabra capitalizada
    """
    return ' '.join(word.capitalize() for word in text.split())
