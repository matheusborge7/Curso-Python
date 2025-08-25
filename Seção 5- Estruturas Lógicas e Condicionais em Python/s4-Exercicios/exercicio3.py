"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

numero: int = int(input("Informe um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")