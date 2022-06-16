# sumはBuilt-in Functionなので、変数名として使う場合は sum_ とするのが良いと思います。
# cf. Built-in Functions
#     https://docs.python.org/3/library/functions.html
#
# PEP8（ https://peps.python.org/pep-0008/#descriptive-naming-styles ）には
#   > single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.
#   > tkinter.Toplevel(master, class_='ClassName')
# と書いてあります。
#
# また、
#   print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))
# などとするとちょっとPythonicかもしれません。

def multiple_of_3_or_5():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

    print(sum)


if __name__ == "__main__":
    multiple_of_3_or_5()
