def maior(lista):
    lista_maiores = []

    for i in lista:
        lista_maior = -9999

        for j in i:
            if lista_maior < j:
                lista_maior = j

        lista_maiores.append(lista_maior)
        i.remove(lista_maior)

    return lista_maiores


print(maior([[1, 2, 3, 4], [3, 23, 32], [2131, 148, 324]]))
