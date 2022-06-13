def is_divisible(num):
	for x in range(11, 21):
		if num%x != 0:
			return False

	return True


def smallest_multiple():
	step = 20
	print(step)
	num = step
	while True:
		if is_divisible(num):
			print(num)
			break

		num = num+step


if __name__ == "__main__":
	smallest_multiple()