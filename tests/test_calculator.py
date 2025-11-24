"""
Pruebas unitarias para el módulo calculator.
Unit tests for the calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide, power


class TestCalculator:
    """Clase de pruebas para las funciones de calculadora."""
    
    def test_add_positive_numbers(self):
        """Prueba la suma de números positivos."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(100, 200) == 300
    
    def test_add_negative_numbers(self):
        """Prueba la suma de números negativos."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5
    
    def test_add_zero(self):
        """Prueba la suma con cero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
    
    def test_subtract_positive_numbers(self):
        """Prueba la resta de números positivos."""
        assert subtract(10, 5) == 5
        assert subtract(20, 8) == 12
    
    def test_subtract_negative_numbers(self):
        """Prueba la resta con números negativos."""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8
    
    def test_multiply_positive_numbers(self):
        """Prueba la multiplicación de números positivos."""
        assert multiply(3, 4) == 12
        assert multiply(5, 6) == 30
    
    def test_multiply_by_zero(self):
        """Prueba la multiplicación por cero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
    
    def test_multiply_negative_numbers(self):
        """Prueba la multiplicación con números negativos."""
        assert multiply(-5, 3) == -15
        assert multiply(-5, -3) == 15
    
    def test_divide_positive_numbers(self):
        """Prueba la división de números positivos."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
    
    def test_divide_by_zero(self):
        """Prueba que la división por cero lanza una excepción."""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            divide(10, 0)
    
    def test_divide_negative_numbers(self):
        """Prueba la división con números negativos."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5
    
    def test_power_positive_numbers(self):
        """Prueba la potencia con números positivos."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1
    
    def test_power_negative_exponent(self):
        """Prueba la potencia con exponente negativo."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
