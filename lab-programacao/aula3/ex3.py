def merge(lista1, lista2):
    lista3 = []

    if len(lista1) > len(lista2):
        for i in range(len(lista1)):
            lista3.append(lista1[i])

            if i < len(lista2):
                lista3.append(lista2[i])
    else:
        for i in range(len(lista2)):
            if i < len(lista1):
                lista3.append(lista1[i])

            lista3.append(lista2[i])

    return lista3


print(merge(["a", "b", "c"], [1, 2, 3, 4, 5, 6]))
