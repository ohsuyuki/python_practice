import math


def lattice_paths():
    ans = math.factorial(40) / (math.factorial(20) * math.factorial(20))
    print(ans)


if __name__ == "__main__":
    lattice_paths()
