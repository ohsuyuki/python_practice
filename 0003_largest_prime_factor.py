# listも予約語です。
# cf. https://docs.python.org/3/library/functions.html
#
# num / x はfloat型を返しますが、整数の商を取得したい場合は num // x が使えます。
# これはPython3で取り入れられた修正なのですが、個人的にはちょっと気持ち悪いと感じます笑

def get_prime_factor(num, list):
    # （超細かいですが）num == 2の時のif文は不要かもですね。
    # 後述のfor文が range(2, 1) となって、実行されないfor文となります。
    if num == 2:
        list.append(num)
        return None

    for x in range(2, int(num / 2)):
        if num % x == 0:
            get_prime_factor(x, list)
            # （超細かいですが）↑この呼び出しは
            # xが素数であることが証明できるので不要で、
            # list.append(x)だけ実行してしまうのが良いかもしれませんね。
            get_prime_factor(int(num / x), list)
            return None

    list.append(num)
    return None


def largest_prime_facotr():
    prime_factors = []
    get_prime_factor(600851475143, prime_factors)
    print(max(prime_factors))


if __name__ == "__main__":
    largest_prime_facotr()
