lista = []

def separa(lista):
    lista2 = []
    lista3 = []

    for i in lista:
        if i % 2 == 0:
            lista2.append(i)
        else:
            lista3.append(i)
    
    return (lista2, lista3)

while len(lista) < 10:
    item = float(input("Digite um valor: "))
    lista.append(item)

separad = separa(lista)

print(f"Lista par {separad[0]}, lista impar: {separad[1]}")
