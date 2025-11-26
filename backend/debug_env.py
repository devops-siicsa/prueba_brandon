import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"Current Working Directory: {os.getcwd()}")
print("System Path:")
for p in sys.path:
    print(f"  - {p}")

try:
    import jwt
    print(f"JWT Module found at: {jwt.__file__}")
except ImportError as e:
    print(f"Error importing jwt: {e}")

try:
    import flask
    print(f"Flask Module found at: {flask.__file__}")
except ImportError as e:
    print(f"Error importing flask: {e}")
