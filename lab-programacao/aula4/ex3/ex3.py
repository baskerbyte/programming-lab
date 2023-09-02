"""
    Escreva um programa que combine duas listas em uma única lista resultante.
"""


def merge(lista1, lista2):
    new_lista = []

    if len(lista1) < len(lista2):
        for i in range(len(lista2)):
            new_lista.append(lista1[i])
            new_lista.append(lista2[i])
    else:
        for i in range(len(lista1)):
            new_lista.append(lista2[i])
            new_lista.append(lista1[i])

    return new_lista
