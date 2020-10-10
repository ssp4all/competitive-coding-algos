https://www.codechef.com/problems/UNITGCD

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("1")
        print("1 1")
    else:
        print(n // 2)
        if n & 1:
            print("3 1 2", n)
        else:
            print("2 1 2")
        for i in range(4, n + 1, 2):
            print("2", i - 1, i)