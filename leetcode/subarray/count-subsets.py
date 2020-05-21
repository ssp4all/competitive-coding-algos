https://leetcode.com/discuss/interview-question/275785/facebook-phone-screen-count-subsets

ip = [2, 4, 5, 7]
k = 8
cnt = 0
n = len(ip)
ip.sort()

l, r = 0, n - 1
while l <= r:
    print(ip[l :  r + 1])
    if ip[l] + ip[r] <= k:
        cnt += (1 << (r - l))
        l += 1
    else:
        r -= 1
print(cnt)