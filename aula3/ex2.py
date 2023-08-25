def alfabetica(lista1):
    lista2 = []

    for _ in range(len(lista1)):
        inicio = lista1[0]

        for j in range(len(lista1)):
            for k in range(len(inicio)):
                print(inicio[k])

alfabetica(["aaa", "bbb"])
