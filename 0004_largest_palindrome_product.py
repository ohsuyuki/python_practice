def is_palindrome(num):
	text = str(num)
	for i in range(int(len(text)/2)):
		if text[i] != text[len(text)-1-i]:
			return False

	return True


def largest_palindrome_product():
	numbers = list({x*y for x in range(100,1000) for y in range(100, 1000)})

	for num in sorted(numbers, reverse=True):
		if is_palindrome(num):
			print(num)
			return None

	return None


if __name__ == "__main__":
	largest_palindrome_product()