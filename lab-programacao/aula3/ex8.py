def media(lista):
    lista_medias = 0

    for i in lista:
        lista_media = 0

        for j in i:
            lista_media += j

        lista_media /= len(i)

        lista_medias += lista_media
        i.append(lista_media)

    lista.append(lista_medias / len(lista))

    return lista


print(media([[1.1, 5.3, 24.1], [21, 432.3, 21.0]]))
