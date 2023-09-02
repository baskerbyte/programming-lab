import ex6

lista = []

for _ in range(5):
    inpt = float(input("Digite uma nota: "))
    lista.append(inpt)

print(f'Média das notas: {ex6.media_notas(lista)}')
