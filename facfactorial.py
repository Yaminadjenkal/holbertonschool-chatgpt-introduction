#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
	result *= n
	n -= 1  # Décrémente n pour sortir de la boucle
	return result

# Vérification de l'argument passé et appel de la fonction
	if len(sys.argv) > 1:
	f = factorial(int(sys.argv[1]))
print(f)
	else:
	print("Veuillez fournir un nombre en argument.")

