def multiple_of_3_or_5():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

    print(sum)


if __name__ == "__main__":
    multiple_of_3_or_5()
