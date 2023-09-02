import ex3

lista1 = []
lista2 = []

for _ in range(5):
    inpt = input("Digite um elemento: ")
    lista1.append(inpt)

print("---------")

for _ in range(5):
    inpt = input("Digite um elemento: ")
    lista2.append(inpt)

print(f'Lista misturada: {ex3.merge(lista1, lista2)}')
