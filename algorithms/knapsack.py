"""KnapSack program recursive """
def ks(weight, val, w, n):
    if weight == 0 or n == 0:
        return 0
    if weight < w[n - 1]:
        return ks(weight, val, w, n - 1)
    return max(val[n - 1] + ks(weight - w[n - 1], val, w, n - 1),
               ks(weight, val, w, n - 1))

w = [10, 20, 30] 
val = [60, 100, 120]
weight = 50
n = 3
x = ks(weight, val, w, n)
print(x)
