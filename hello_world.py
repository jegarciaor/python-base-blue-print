import sys


def sumar_numeros(numero_1: int, numero_2: int) -> int:
    return numero_1 + numero_2


if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    result = sumar_numeros(num1, num2)

    print(f"{num1} + {num2} = {result}")
