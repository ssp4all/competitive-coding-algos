Consider a skyline with buildings of different heights. You are scanning them from left to right.
a. Can you identify if there exist three buildings (not necessarily adjacent) with heights x, 2x and 4x (in that order).
Example: x, y, 2x, z, 2y, 4x -> Yes, x, y, 4x, z, 2y, 2x -> No
b. Can you count all such combinations?
Example: x,2x,4x,2x,4x -> 3 (2 combinations possible for the second 4x). x,2x,2x,4x,8x -> 4 (2 for x,2x,4x and 2 for 2x,4x,8x)
c. Can you generalise it to be a sequence of any length? Say 5 buildings of lengths x, 2x, 4x, 8x, 16x?


global ans

used = []
dd = ["x", "2x", "4x"]
ans = 0

def bt(temp, st):

    global ans
    print(temp, used)
    if len(temp) == 3:
        if dd == temp:
            # print(used)
            ans += 1
        else:
            del temp[-1]
            del used[-1]
            print("->", temp, used)
            
    else:
        for i in range(st, n):
            # print(used)
            if i in used:   continue
            used.append(i)
            bt(temp + [ip[i]], i + 1)
            if i in used:
                used.remove(i)

ip = ["x", "2x", "2x", "4x", "4x"]
n = len(ip)
bt([], 0)
print(ans)