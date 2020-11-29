def findMin(num):
    l = 0
    n = len(num)
    r = n - 1
    while l < r:
        if num[l] < num[r]:
            return num[l]
        m = (l + r) // 2
        if num[m] >= num[l]:
            l = m + 1
        else:
            r = m
    return num[l]
