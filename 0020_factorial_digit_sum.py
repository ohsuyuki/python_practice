import math


def factorial_digit_sum():
    factorial = math.factorial(100)

    sum = 0
    for c in str(factorial):
        sum = sum + int(c)

    print(sum)


if __name__ == "__main__":
    factorial_digit_sum()
