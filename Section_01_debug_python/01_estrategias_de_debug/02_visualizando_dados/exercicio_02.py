from math import factorial


def map_factorial(numbers):
    result = []

    for num in numbers:
        result.append(factorial(num))

    return result


def main():
    input_list = [1, '2', 3, 4, 5]
    return map_factorial(input_list)


if __name__ == "__main__":
    main()


# * 1. Um dos elementos da input_list for um inteiro negativo.
#      Exception has occured: ValueError

# * 2. Um dos elementos da input_list for uma string.
#      Exception has occured: TypeError
