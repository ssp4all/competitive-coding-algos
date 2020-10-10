ip = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    ip.append([name, score])
second_high = sorted(list(set([marks for name, marks in ip])))[1]
print('\n'.join([name for name, marks in sorted(ip) if marks == second_high]))

