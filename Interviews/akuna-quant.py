from math import ceil
from collections import Counter

def reduceCapacity(model):
    if not model: return 0
    # n = model[0]
    # model = model[1:]
    ans = 0
    xx = Counter(model)
    mini = ceil(n/2)
    temp = sorted(xx.values(), reverse=1)
    # print(temp)
    sum = 0
    for i, j in enumerate(temp):
        sum += j
        if sum >= mini:
            return i+1
    return 0
    
model = [7,10, 1,2,7,7,1]
xx = reduceCapacity(model)
print(xx)


def stokes_to_print(given):
    if not given: return 0
    # picture = [list(a) for a in given]
    row = len(picture)
    col = len(picture[0])
    ans = 0
    seen = set()
    def color(u, v, orig):
        if u < 0 or v < 0 or u >= row or v >= col or \
             picture[u][v] != orig or (u, v) in seen:
            return
        seen.add((u, v))
        # picture[u][v] = "@"

        color(u, v+1, orig)
        color(u, v-1, orig)
        color(u+1, v, orig)
        color(u-1, v, orig)

    for i in range(row):
        for j in range(col):
            if (i, j) not in seen:
                color(i, j, picture[i][j])
                ans += 1
    return ans

tp = ["aabba", "aabba", "aaacb"]
xx = stokes_to_print(tp)
print(xx)
-----------------------------------------------
def max_height(sp, sh):
    n = len(sp)
    m = len(sh)
    ans = 0
    for i in range(n-1):
        cells = abs(sp[i+1]-sp[i]-1)
        if cells < 1:
            continue
        temp = sh[i]
        x = sp[i] + 1
        while x < sp[i+1]-1:
            x += 1
            temp += 1
        tt = temp + 1
        if sh[i+1] - tt >= -1 :
            temp += 1
        ans = max(ans, temp)
    return ans

def max_height(sp, sh):
    n = len(sp)
    for i in range(n):
        diff = sp[i+1] - sp[i] - 1
        if diff < 1:    continue
        hd = sh[i+1] - sh[i]
        gap_len = diff
        maxi = 0
        if gap_len > hd:
            low = max(sh[i+1], sh[i]) + 1
            range_gap = gap_len - hd - 1
            maxi = low + (range_gap//2)
        else:
            maxi = min(sh[i+1], sh[i]) + 1
    return maxi

--------------------------


sp = [1, 2, 10]
sh = [3, 3, 3]
xx = max_height(sp, sh)
print(xx)