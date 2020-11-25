https://www.geeksforgeeks.org/merge-sort-with-o1-extra-space-merge-and-on-lg-n-time/

def merge(l, m, r):

    i, j, k = l, m + 1, l

    while i <= m and j <= r:

        if ip[i] % maxi <= ip[j] % maxi:
            ip[k] += (ip[i] % maxi) * maxi
            i += 1
        else:
            ip[k] += (ip[j] % maxi) * maxi
            j += 1
        k += 1

    while i <= m:
        ip[k] += (ip[i] % maxi) * maxi
        i += 1
        k += 1
    while j <= r:
        ip[k] += (ip[j] % maxi) * maxi
        j += 1
        k += 1
    for i in range(l, r + 1):
        ip[i] //= maxi
    print(ip)

def merge_sort(l, r):
    if l >= r:   return
    m = (l + r) // 2
    merge_sort(l, m)
    merge_sort(m + 1, r)
    merge(l, m, r)

ip = [5, 4, 3, 1] 
maxi = max(ip) + 1
merge_sort(0, len(ip) - 1)
