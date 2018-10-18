n = 4
print('Enter No. of rows: ')
n = int(input())
a = []
# for i in range(n):
#     a.append([])
#     a[i] = [0] * 4
# print(a)

for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1] + a[i-1][j])
    if n != 0:
        a[i].append(1)
print(a)

for i in range(n):
    print("   " * (n - i), end=" ", sep=" ")
    for j in range(0, i+1 ):
        # print(a[i][j])
        print("{:5}".format(a[i][j]), end=" ", sep=" ")
    print()
# print(a[0][2])
