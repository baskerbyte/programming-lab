"""
Crie uma função chamada primos_em_intervalo que aceite dois números como argumentos e retorna uma lista de todos os números primos no intervalo entre esses dois números.
"""


def primos_em_intervalo(num1, num2):
    primos = []
    highest = num1 if num1 > num2 else num2

    for i in range(num1, num2):
        divisions = []

        for j in range(1, highest):
            if i % j == 0:
                divisions.append(i)

        if len(divisions) < 3:
            primos.append(i)

    return primos
