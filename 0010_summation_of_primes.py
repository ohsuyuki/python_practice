import math
# import numpy


# def is_prime(num):
# 	for x in range(2, num):
# 		if num%x == 0:
# 			return False

# 	return True
def is_prime(n):
	if n == 1:
		return False

	if n < 4:
		return True

	if n % 2 == 0:
		return False

	if n < 9:
		return True

	if n % 3 == 0:
		return False

	r = math.sqrt(n)
	f = 5
	while f<=r:
		if n % f == 0:
			return False
		if n % (f+2) == 0:
			return False

		f = f+6

	return True


def summation_of_primes():
	sum = 0
	for x in range(2, 2000000):
		if is_prime(x):
			sum = sum+x

	print(sum)


if __name__ == "__main__":
	summation_of_primes()