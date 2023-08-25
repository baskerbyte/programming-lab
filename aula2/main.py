from exercises import ex1, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10


def ex1_input():
    num = int(input("Digite um número: "))
    return num


def ex2_input():
    num = int(input("Digite um número: "))
    return num


def ex3_input():
    num = int(input("Digite um numero: "))
    return num


def ex4_input():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    tipo = input("Digite o tipo de operação (A, P): ")
    return nota1, nota2, nota3, tipo


def ex5_input():
    anos = int(input("Digite quantos anos você tem: "))
    meses = int(input("Digite os meses adicionais: "))
    dias = int(input("Digite os dias adicionais: "))
    return anos, meses, dias


def ex6_input():
    num1 = int(input('Digite o numero 1: '))
    num2 = int(input('Digite o numero 2: '))
    num3 = int(input('Digite o numero 3: '))
    return num1, num2, num3


def ex7_input():
    sec = int(input("Digite o tempo: "))
    return sec


def ex8_input():
    num = int(input("Digite um número: "))
    return num


def ex9_input():
    sex = input("Digite o sexo (H ou F): ")
    alt = float(input("Digite a altura em metros: "))
    return sex, alt


def ex10_input():
    x = float(input("Digite o valor de X: "))
    y = float(input("Digite o valor de Y: "))
    z = float(input("Digite o valor de Z: "))
    return x, y, z


exercise = int(input("Digite um exercício (1-10) ou 0 para sair: "))

while exercise != 0:
    if exercise == 1:
        num = ex1_input()

        print(ex1.is_positive(num))
    elif exercise == 2:
        num = ex2_input()
        isPositive = ex1.is_positive(num)

        if isPositive:
            print(f'O valor {num} é positivo')
        else:
            print(f'O valor {num} é negativo')
    elif exercise == 3:
        num = ex3_input()

        if ex3.is_odd(num):
            print(f"O valor {num} é impar")
        else:
            print(f"O valor {num} é par")
    elif exercise == 4:
        nota1, nota2, nota3, tipo = ex4_input()

        if tipo != "A" and tipo != "P":
            print("Tipo não aceito")
        else:
            print(f'Retorno do calculo {ex4.calcula_nota(nota1, nota2, nota3, tipo)}')
    elif exercise == 5:
        anos, meses, dias = ex5_input()

        print(f"Já fazem {ex5.idade_em_dias(anos, meses, dias)} dias que você nasceu")
    elif exercise == 6:
        num1, num2, num3 = ex6_input()

        print(f'Valor ordenado {ex6.ordena(num1, num2, num3)}')
    elif exercise == 7:
        sec = ex7_input()

        print(ex7.formata_tempo(sec))
    elif exercise == 8:
        num = ex8_input()

        print(ex8.is_perfect_num(num))
    elif exercise == 9:
        sex, alt = ex9_input()

        print(ex9.calcula_imc(alt, sex))
    elif exercise == 10:
        x, y, z = ex10_input()

        print(ex10.verifica_triangulo(x, y, z))
    else:
        print("Opção inválida!")

    exercise = int(input("Digite um exercício (1-10) ou 0 para sair: "))
