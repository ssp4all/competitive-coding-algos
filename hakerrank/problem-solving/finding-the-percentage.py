# Suraj Pawar
if __name__ == '__main__':
    n = int(input())
    ip = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        ip[name] = scores
    query_name = input()
    # actual code
    op = 0
    for i in range(3):
        op += ip[query_name][i]
    op = op/3
    print('%.2f'%op)