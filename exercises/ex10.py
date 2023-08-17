def verifica_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        if x == y == z:
            return "Triângulo Equilátero"
        elif x == y or y == z or x == z:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é um triângulo"
