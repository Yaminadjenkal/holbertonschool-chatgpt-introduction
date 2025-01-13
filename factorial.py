#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n   # Cette ligne doit être indentée avec 4 espaces
		n -= 1        # Cette ligne aussi doit être indentée avec 4 espaces
	return result

	if len(sys.argv) > 1:
		f = factorial(int(sys.argv[1]))
		print(f)
	else:
		print("Veuillez fournir un nombre en argument.")

