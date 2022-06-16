def even_fibonacci_numbers():
    pre_prev, prev = 1, 2
    current = pre_prev + prev
    sum = 2
    while current < 4_000_000:
        if current % 2 == 0:
            sum = sum + current

        pre_prev, prev, current = prev, current, prev + current

    print(sum)

    # （細かい指摘なので無視して大丈夫です）
    # prevとcurrentだけあれば十分で、こんな感じに書けます。
    # prev, current = 1, 2
    # sum_ = 0
    # while current < 4_000_000:
    #     if current % 2 == 0:
    #         sum_ += current
    #     prev, current = current, prev + current


if __name__ == "__main__":
    even_fibonacci_numbers()
