https://www.programmingsimplified.com/c/program/c-program-check-if-array-is-sorted-or-not

"""
C program to check if an array is sorted or not (ascending or descending or none)
"""

# ip = list(range(10, -1, -1))
ip = [1,1,1]
a, d = 1, 1 

i = 0
n = len(ip)
while (a == 1 or d == 1) and i < n - 1:
    if ip[i] < ip[i + 1]:
        d = 0
    elif ip[i] > ip[i + 1]:
        a = 0
    i += 1

if a == 1:
    print("ASec")
elif d == 1:
    print("Desc")
else:
    print("Nope")