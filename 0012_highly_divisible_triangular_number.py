# def is_over_five_hundred_divisors(num):
# 	divisors = set()
# 	for x in range(1, num):
# 		if x in divisors:
# 			break

# 		if num%x == 0:
# 			divisors.add(x)
# 			divisors.add(num/x)

# 	global debug
# 	debug = debug + 1
# 	if debug % 100 == 0:
# 		print(num, len(divisors))

# 	return len(divisors) >= 500


def is_over_five_hundred_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1

    divisors = lower_divisors + upper_divisors[::-1]

    print(n, len(divisors))
    return len(divisors) >= 500


def highly_divisible_triangular_number():
    num = 1
    i = 1
    while True:
        if is_over_five_hundred_divisors(num):
            print(num)
            break

        i = i + 1
        num = num + i


if __name__ == "__main__":
    highly_divisible_triangular_number()
