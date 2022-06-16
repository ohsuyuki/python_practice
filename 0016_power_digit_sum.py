def power_digit_sum():
    # ワンライナーが良いわけではないですが、
    #   print(sum(int(c) for c in str(2**1000)))
    # みたいなのもありかもしれません。
    power = 2**1000
    sum = 0
    for c in str(power):
        sum = sum + int(c)

    print(sum)


if __name__ == "__main__":
    power_digit_sum()
