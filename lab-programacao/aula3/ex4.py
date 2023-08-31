def positions(lista):
    items = []

    for i in range(len(lista)):
        if i % 2 == 0:
            items.append(lista[i])

    return items


print(positions([0, 1, 2, 4]))
