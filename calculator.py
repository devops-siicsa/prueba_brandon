"""
Módulo de calculadora simple para pruebas internas de Copilot.
Simple calculator module for internal Copilot testing.
"""


def add(a, b):
    """
    Suma dos números.
    Add two numbers.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La suma de a y b
    """
    return a + b


def subtract(a, b):
    """
    Resta dos números.
    Subtract two numbers.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La resta de a menos b
    """
    return a - b


def multiply(a, b):
    """
    Multiplica dos números.
    Multiply two numbers.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        El producto de a y b
    """
    return a * b


def divide(a, b):
    """
    Divide dos números.
    Divide two numbers.
    
    Args:
        a: Numerador
        b: Denominador
    
    Returns:
        El cociente de a dividido por b
    
    Raises:
        ValueError: Si b es cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero / Cannot divide by zero")
    return a / b


def power(a, b):
    """
    Calcula la potencia de un número.
    Calculate the power of a number.
    
    Args:
        a: Base
        b: Exponente
    
    Returns:
        a elevado a la potencia b
    """
    return a ** b
