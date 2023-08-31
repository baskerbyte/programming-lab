def ordena(lista1):
    lista2 = []

    for _ in range(len(lista1)):
        menor = lista1[0]

        for j in range(len(lista1)):
            if menor > lista1[j]:
                menor = lista1[j]

        lista2.append(menor)
        lista1.remove(menor)

    return lista2


print(ordena(["4444", "55555", "1", "333", "22"]))
