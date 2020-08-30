def print_primes(n):
    if n < 2:
        return 0
    primes = [1]*(n+1)
    primes[0] = primes[1] = 0
    p = 2
    while p*p < n:
        for i in range(2*p, n+1, p):
            primes[i] = 0
        p += 1
    # print(primes.count(1))
    for i in range(n+1):
        if primes[i] == 1:
            print(i)


print_primes(10)
