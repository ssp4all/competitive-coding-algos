# https://www.geeksforgeeks.org/count-of-ways-to-split-an-array-into-three-
# 	contiguous-subarrays-having-increasing-sum/


# Brute force solution
ip = [2, 3, 4, 0, 10]
n = len(ip)
s, e = 1, 2
count = 0
tot = sum(ip)
for i in range(1, n - 1):
    for j in range(i + 1, n):
        b = sum(ip[i:j])
        c = sum(ip[j:])

        a = tot - b - c
        if a <= b <= c:
            count += 1
print(count)

#optimal sol
ip = [2, 3, 4, 10]
n = len(ip)

count = 0
tot = sum(ip)
pref = [ip[0]]
# prefix sum array
for i in range(1, n):
    pref += [ip[i] + pref[-1]]
suff = [ip[-1]]
# suffix sum array
for i in range(n - 2, -1, -1):
    suff += [ip[i] + suff[-1]]
suff.reverse()
#calculate using two pointer technique
s, e = 1, 1
curr = 0
while s < n - 1 and e < n - 1:
    while e < n - 1 and curr < pref[s - 1]:
        curr += ip[e]
        e += 1
    if curr <= suff[e]:
        count += 1
    curr -= ip[s]
    s += 1
print(count)