from collections import Counter

def common_elements(arr1, arr2):
    # Write your code here
    if not arr1 and not arr2:   return []
    if not arr1 or not arr2:   return []
    print(arr1, arr2)
    x = Counter(arr1) & Counter(arr2)
    op = []
    for key, v in x.items():
        op += [key] * v
    return op


Q 2
t = int(input())
res = []
for _ in range(t):
    ip = list(map(int, input().split(" ")))
    m1, m2 = ip
    i = 1
    while 1:
        if i > max(m1, m2):
            break 
        if m1 >= m2:
            m1 -= i 
        else:
            m2 -= i 
        i += 1
    res += [[i, m1, m2]]
for r in res:
    print(*r)


Q 3 
import math
t = int(input())

def solve(a, b, c):
    dis = b * b - 4 * a * c 
    sqrt = math.sqrt(abs(dis))
    ans1, ans2 = 0, 0 
    if dis >0 :
        ans1 = (- b + sqrt) / (2 * a)
        ans2 = (- b - sqrt) / (2 * a)
    elif dis == 0:
        ans1, ans2 = - b / (2 * a)
    return math.floor(max(ans1, ans2))


    
for _ in range(t):
    ip = list(map(int, input().split(" ")))
    m1, m2 = ip
    i = 1
    while 1:
        d = abs(m1 - m2)
        if i > max(m1, m2):
            break 
        if d > min(m1, m2):
            quad = solve(1, 1, - (math.pow(i, 2) - i + d*2))
            if quad > 0:
                if m1 >= m2:
                    m1 -= ((quad*(quad + 1)) + i*(i - 1)) // 2 
                    i += quad 
                else:
                    m2 -= ((quad*(quad + 1)) + i*(i - 1)) // 2 
                    i += quad 
        else:
            if m1 >= m2:
                m1 -= i 
            else:
                m2 -= i 
            i += 1 
    print(i, m1, m2)
                    

Q 4
from collections import Counter, defaultdict
def getMinTransform(source, target):
    # Write your code here

    
    sl, tl = len(source), len(target)
    if sl != tl:    return -1
    t_set = set()
    # if len(s) == 26:    return -1
    s, t = defaultdict(), defaultdict()
    m = defaultdict()
    for i in range(sl):
        t_set.add(target[i])
        if source[i] in m and m[source[i]] != target[i]:
            return -1 
        m[source[i]] = target[i]
    if source != target and len(m) == 26 and len(t_set) == 26:
        return -1 
    
    c = 0 
    for i in m:
        if m[i] != i:
            c += 1
    return c 
            