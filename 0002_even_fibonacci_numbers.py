def even_fibonacci_numbers():
	pre_prev, prev = 1, 2
	current = pre_prev+prev
	sum = 2
	while current < 4_000_000:
		if current%2 == 0:
			sum = sum+current

		pre_prev, prev, current = prev, current, prev+current

	print(sum)


if __name__ == "__main__":
	even_fibonacci_numbers()