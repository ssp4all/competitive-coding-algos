from sys import argv
import string


def find_pattern(file, pattern):

    f = open(file, mode="r+")
    content = f.read().split("\n")

    op = []
    for line in content:
        print(line)
        if line.find(pattern) != -1:
            op.append(line)
    print(op)
    f.close()


if __name__ == "__main__":
    # print(argv)
    a, b = argv[1], argv[2]
    find_pattern(a, b)
