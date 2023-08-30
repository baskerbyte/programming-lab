def ordena(lista1):
    lista_copy = lista1[:]
    lista2 = []

    for _ in range(len(lista_copy)):
        menor = lista_copy[0]

        for j in range(len(lista_copy)):
            if menor > lista_copy[j]:
                menor = lista_copy[j]

        lista2.append(menor)
        lista_copy.remove(menor)

    return lista2

print(ordena(["4444", "55555", "1", "333", "22"]))
