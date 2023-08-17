def ordena(num1, num2, num3):
    if num1 <= num2 <= num3:
        return f"{num1}, {num2}, {num3}"
    elif num1 <= num3 <= num2:
        return f"{num1}, {num3}, {num2}"
    elif num2 <= num1 <= num3:
        return f"{num2}, {num1}, {num3}"
    elif num2 <= num3 <= num1:
        return f"{num2}, {num3}, {num1}"
    elif num3 <= num1 <= num2:
        return f"{num3}, {num1}, {num2}"
    else:
        return f"{num3}, {num2}, {num1}"
