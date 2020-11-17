

def seg_tree(input, seg, left, right, pos):
    if left == right:
        seg[pos] = input[left]
        return
    m = left + (right - left) // 2
    seg_tree(input, seg, left, m, 2*pos + 1)
    seg_tree(input, seg, m + 1, right, 2*pos + 2)
    seg[pos] = min(seg[2 * pos + 1], seg[2 * pos + 2])

def range_query(seg, left, right, qlow, qhigh, pos):
    if qlow <= left and qhigh >= right:
        return seg[pos]
    if qlow > right or qhigh < left:
        return float('inf')
    m = left + (right - left) // 2
    return min(range_query(seg, left, m, qlow, qhigh, 2*pos + 1), 
                range_query(seg, m + 1, right, qlow, qhigh, 2*pos + 2))


ip = [-1, 2, 4, 0]
n = len(ip)
seg = [float('inf')] * (2 ** (n - 1) - 1)
seg_tree(ip, seg, 0, n - 1, 0)
print(seg)

val = range_query(seg, 0, n - 1, 1, 3, 0)
print(val)