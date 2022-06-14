def longest_collatz_sequence():
    target = 1
    max_chain = 0
    for x in range(1, 1000000):
        current_chain = 1
        num = x
        while num != 1:
            current_chain = current_chain + 1

            if num % 2 == 0:
                num = num / 2
            else:
                num = num * 3 + 1

        if current_chain > max_chain:
            target = x
            max_chain = current_chain

    print(target, max_chain)


if __name__ == "__main__":
    longest_collatz_sequence()
