def is_prime(num):
	for x in range(2, num):
		if num%x == 0:
			return False

	return True


def func_10001st_prime():
	num = 3
	count = 2
	while count < 10001:
		num = num+2
		if is_prime(num):
			count = count+1

	print(num)


if __name__ == "__main__":
	func_10001st_prime()