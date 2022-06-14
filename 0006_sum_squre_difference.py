def sum_squre_difference():
    sum_of_square = 0
    sum = 0
    for x in range(1, 101):
        sum_of_square = sum_of_square + x**2
        sum = sum + x

    print(sum)
    print(sum_of_square)
    ans = sum**2 - sum_of_square
    print(ans)


if __name__ == "__main__":
    sum_squre_difference()
