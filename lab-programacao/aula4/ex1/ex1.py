"""
    Escreva uma função chamada encontra maior que encontre o maior elemento em uma lista de números.
"""


def encontra_maior(lista):
    maior = lista[0]

    for item in lista:
        if item > maior:
            maior = item

    return maior
