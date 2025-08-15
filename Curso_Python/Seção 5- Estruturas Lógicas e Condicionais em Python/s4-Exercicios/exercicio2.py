"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

numero1: int = int(input("Informe o primeiro número: "))
numero2: int = int(input("Informe o segundo número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 == numero2:
    print(f"O número {numero1} é igual ao número {numero2}")
else:
    print(f"O número {numero2} é maior que o número {numero1}")