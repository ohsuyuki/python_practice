def get_word(num):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return words[num]


def get_word_teen(num):
    words = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    return words[num % 10]


def get_word_ten(num):
    words = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    return words[num]


def convert_to_word_less_than_hundred(num):
    if num <= 9:
        return get_word(num)
    elif 10 <= num and num <= 19:
        return get_word_teen(num)
    elif 20 <= num and num <= 99:
        ten = get_word_ten(num / 10)
        if num % 10 == 0:
            return ten
        one = get_word(num % 10)
        return ten + one
    else:
        return None


def convert_to_word_more_than_hundred(num):
    if num <= 99 or 1000 <= num:
        return None

    hundred = get_word(num / 100)
    remain = num % 100
    if remain == 0:
        return hundred + "hundred"

    remain_word = convert_to_word_less_than_hundred(remain)
    return hundred + "hundredand" + remain_word


def convert_to_word_more_than_thousand(num):
    return "onethousand"


def convert_to_word(num):
    if 1 <= num <= 99:
        return convert_to_word_less_than_hundred(num)
    elif 100 <= num and num <= 999:
        return convert_to_word_more_than_hundred(num)
    else:
        return convert_to_word_more_than_thousand(num)


def number_letter_counts():
    sum = 0
    for x in range(1, 1001):
        word = convert_to_word(x)
        print(word, x)
        sum = sum + len(word)

    print(sum)


if __name__ == "__main__":
    number_letter_counts()
