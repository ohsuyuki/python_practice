def get_prime_factor(num, list):
	if num == 2:
		list.append(num)
		return None

	for x in range(2, int(num/2)):
		if num%x == 0:
			get_prime_factor(x, list)
			get_prime_factor(int(num/x), list)
			return None

	list.append(num)
	return None


def largest_prime_facotr():
	prime_factors = []
	get_prime_factor(600851475143, prime_factors)
	print(max(prime_factors))


if __name__ == "__main__":
	largest_prime_facotr()