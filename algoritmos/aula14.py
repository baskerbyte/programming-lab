ministrantes = [
    ['11C', 'mestre', 40],
    ['22C', 'doutor', 10],
    ['33C', 'mestre', 20],
    ['44C', 'especialista', 40],
    ['55C', 'especialista', 60],
    ['66C', 'mestre', 20],
    ['77C', 'especialista', 10],
    ['88C', 'doutor', 30]
]
i = 0

while i < len(ministrantes):
    ministrante = ministrantes[i]
    print("Código:", ministrante[0], "- Titulação:", ministrante[1], "- Qt. de horas:", ministrante[2])
    i = i + 1

i = 0
print("---------------")

while i < len(ministrantes):
    ministrante = ministrantes[i]
    valorHora = 0

    if ministrante[1] == 'especialista':
      valorHora = 50
    elif ministrante[1] == 'mestre':
      valorHora = 100
    else:
      valorHora = 150
    
    ministrante.append(valorHora * ministrante[2])
    i = i + 1

i = 0
qtMin = 0

while i < len(ministrantes):
    ministrante = ministrantes[i]
    print("Código:", ministrante[0], "- Titulação:", ministrante[1], "- Qt. de horas:", ministrante[2], "- Recebeu:", ministrante[3])

    if ministrante[1] == 'mestre' and ministrante[2] < 40:
        qtMin = qtMin + 1

    i = i + 1

i = 0
print("---------------")
inpt = input("Digite uma titulação para filtrar ou digite \"SAIR\": ")

while inpt != 'SAIR':
    while i < len(ministrantes):
        ministrante = ministrantes[i]
        if ministrante[1] == inpt:
            print('Código:', ministrante[0], '- Recebeu:', ministrante[3])
        i = i + 1
    i = 0
    inpt = input("Digite uma titulação para filtrar ou digite \"SAIR\": ")