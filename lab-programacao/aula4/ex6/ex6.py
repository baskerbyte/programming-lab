"""
    Crie uma função chamada media _ notas que receba uma lista de notas de estudantes e retorne a média das notas.
"""


def media_notas(lista):
    soma = 0

    for i in lista:
        soma += i

    return soma / len(lista)
