def countSawSubarrays(arr):
    if len(arr) < 2:
        return 0
    if len(arr) == 2 and arr[0] != arr[1]:
        return 1
    elif len(arr) == 2 and arr[0] == arr[1]:
        return 0
    count = 0
    for i in range(1, len(arr)):
        prevdiff = arr[i] - arr[i-1]
        if prevdiff != 0:
            count += 1
        for j in range(i+1, len(arr)):
            newdiff = arr[j] - arr[j-1]
            if (newdiff > 0 and prevdiff < 0) or (newdiff < 0 and prevdiff > 0):
                count += 1
                prevdiff = newdiff
            else:
                break
    return count
#####################
def numberSigningSum(n):
    pos = []
    neg = []
    for ind, num in enumerate(str(n)):
        if ind % 2 == 0:
            pos += [int(num)]
        else:
            neg += [int(num)]
            
    return sum(pos) - sum(neg)
#####################
def divisorSubstrings(n, k):
    distinct = set()
    sn = str(n)
    l = len(str(n))

    for ind in range(k - 1, l):
        if ind - k + 1 >= 0:
            cur = sn[ind - k + 1: ind + 1]
            if len(cur) > 0 and cur not in distinct and int(cur) > 0 and n % int(cur) == 0:
                distinct.add(int(cur))
    return len(distinct)
#####################
def diagonalsArranging(mat):
    allStrings = []

    n = len(mat)
    for i in range(0, n):
        r = n-1-i
        c = 0
        w = ""
        for j in range(0, n):
            w += mat[r][c]
            r+= 1
            c+= 1
            if r == n:
                r = n-1-i
                c = 0
        allStrings.append(w)

    for i in range(1, n):
        r = 0
        c = i
        w = ""
        for j in range(0, n):
            w += mat[r][c]
            r+= 1
            c+= 1
            if c == n:
                c = i
                r = 0
        allStrings.append(w)
    return [i[0]+1 for i in sorted(enumerate(allStrings), key=lambda x:x[1])]

