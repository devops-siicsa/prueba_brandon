# prueba_brandon

## Pruebas Internas de Copilot / Internal Copilot Tests

Este repositorio contiene pruebas internas para demostrar las capacidades de GitHub Copilot.

This repository contains internal tests to demonstrate GitHub Copilot capabilities.

## Estructura del Proyecto / Project Structure

```
prueba_brandon/
├── calculator.py          # Módulo de calculadora / Calculator module
├── string_utils.py        # Utilidades de cadenas / String utilities
├── tests/                 # Directorio de pruebas / Tests directory
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_string_utils.py
├── requirements.txt       # Dependencias / Dependencies
├── pytest.ini            # Configuración de pytest / Pytest configuration
└── README.md
```

## Instalación / Installation

1. Instalar las dependencias / Install dependencies:
```bash
pip install -r requirements.txt
```

## Ejecutar las Pruebas / Run Tests

Para ejecutar todas las pruebas / To run all tests:
```bash
pytest
```

Para ejecutar las pruebas con cobertura / To run tests with coverage:
```bash
pytest --cov=. --cov-report=html
```

Para ejecutar pruebas específicas / To run specific tests:
```bash
pytest tests/test_calculator.py
pytest tests/test_string_utils.py
```

## Módulos / Modules

### calculator.py
Módulo con funciones matemáticas básicas:
- `add(a, b)`: Suma dos números
- `subtract(a, b)`: Resta dos números
- `multiply(a, b)`: Multiplica dos números
- `divide(a, b)`: Divide dos números
- `power(a, b)`: Calcula la potencia de un número

### string_utils.py
Módulo con utilidades para manejo de cadenas:
- `reverse_string(text)`: Invierte una cadena
- `is_palindrome(text)`: Verifica si es un palíndromo
- `count_vowels(text)`: Cuenta las vocales
- `capitalize_words(text)`: Capitaliza cada palabra