#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérifier si un argument a été fourni
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

# Vérifier si l'argument est un nombre entier positif
try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("The number must be a non-negative integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

# Calculer le factoriel
f = factorial(n)
print(f)

