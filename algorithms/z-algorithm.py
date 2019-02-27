# A pattern matching algorithm


def search(str, pattern):
    # print(str, pattern)
    n = len(str)
    conc = str+"$"+pattern
    z = [0]*n
    calc_z_array(conc, z)


def calc_z_array(conc, z):
    l = len(conc)
    L=R=0
    for i in range(l):
        if i>R:
            while R<n and str[R-L] == str[R]:
                R += 1
                

def main():
    # str = input()
    str = "baabaa"
    pattern = "aab"
    # pattern = input()
    calc_z_array(str, pattern)










if __name__ == "__main__":
    main()
