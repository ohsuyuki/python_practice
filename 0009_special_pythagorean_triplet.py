def is_target_numbers(a, b, c):
	if a + b + c != 1000:
		return False

	if a**2 + b**2 != c**2:
		return False

	return True


def special_pythagorean_triplet():
	for a in range(1, 1000):
		for b in range(1, 1000):
			for c in range(1, 1000):
				if is_target_numbers(a, b, c):
					print(a*b*c)
					return None

	return None


if __name__ == "__main__":
	special_pythagorean_triplet()