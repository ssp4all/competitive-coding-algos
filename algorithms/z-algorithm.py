# A pattern matching algorithm

def calc_z_array(conc, z):
    """Generates z array """
    l = r = 0
    n = len(conc)
    # print(conc)
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and conc[ r - l ] == conc[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < (r - i + 1):
                z[i] = z[k]
            else:
                l = i
                while r < n and conc[ r - l ] == conc[r]:
                    r += 1
                z[i] = r - l
                r -= 1

def search(string, pattern):
    """ Prints z array """
    conc = pattern + "$" +  string
    n = len(conc)
    z = [0] * n
    calc_z_array(conc, z)
    for i in range(1, n):
        print(z[i], end=" ")

def main():
    # str = input()
    string = "baabaa"
    pattern = "aab"
    # pattern = input()
    search(string, pattern)

if __name__ == "__main__":
    main()
