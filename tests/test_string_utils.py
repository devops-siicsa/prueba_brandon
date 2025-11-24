"""
Pruebas unitarias para el módulo string_utils.
Unit tests for the string_utils module.
"""

import pytest
from string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words


class TestStringUtils:
    """Clase de pruebas para las utilidades de cadenas."""
    
    def test_reverse_string_simple(self):
        """Prueba la inversión de cadenas simples."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("python") == "nohtyp"
    
    def test_reverse_string_empty(self):
        """Prueba la inversión de cadena vacía."""
        assert reverse_string("") == ""
    
    def test_reverse_string_single_char(self):
        """Prueba la inversión de un solo carácter."""
        assert reverse_string("a") == "a"
    
    def test_reverse_string_with_spaces(self):
        """Prueba la inversión de cadenas con espacios."""
        assert reverse_string("hello world") == "dlrow olleh"
    
    def test_is_palindrome_true(self):
        """Prueba palíndromos válidos."""
        assert is_palindrome("aba") == True
        assert is_palindrome("racecar") == True
        assert is_palindrome("A man a plan a canal Panama") == True
    
    def test_is_palindrome_false(self):
        """Prueba cadenas que no son palíndromos."""
        assert is_palindrome("hello") == False
        assert is_palindrome("python") == False
    
    def test_is_palindrome_empty(self):
        """Prueba palíndromo con cadena vacía."""
        assert is_palindrome("") == True
    
    def test_is_palindrome_case_insensitive(self):
        """Prueba que el palíndromo ignora mayúsculas."""
        assert is_palindrome("Aba") == True
        assert is_palindrome("RaceCar") == True
    
    def test_count_vowels_simple(self):
        """Prueba el conteo de vocales en cadenas simples."""
        assert count_vowels("hello") == 2
        assert count_vowels("python") == 1
        assert count_vowels("aeiou") == 5
    
    def test_count_vowels_uppercase(self):
        """Prueba el conteo de vocales con mayúsculas."""
        assert count_vowels("HELLO") == 2
        assert count_vowels("AEIOUaeiou") == 10
    
    def test_count_vowels_no_vowels(self):
        """Prueba el conteo cuando no hay vocales."""
        assert count_vowels("xyz") == 0
        assert count_vowels("bcdfg") == 0
    
    def test_count_vowels_empty(self):
        """Prueba el conteo con cadena vacía."""
        assert count_vowels("") == 0
    
    def test_capitalize_words_simple(self):
        """Prueba la capitalización de palabras simples."""
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"
    
    def test_capitalize_words_already_capitalized(self):
        """Prueba cuando las palabras ya están capitalizadas."""
        assert capitalize_words("Hello World") == "Hello World"
    
    def test_capitalize_words_empty(self):
        """Prueba capitalización con cadena vacía."""
        assert capitalize_words("") == ""
    
    def test_capitalize_words_single_word(self):
        """Prueba capitalización de una sola palabra."""
        assert capitalize_words("hello") == "Hello"
