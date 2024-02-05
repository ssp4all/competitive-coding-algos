# https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

# Fenwick tree implementation

# TC: O(lgn)
def get_sum(BIT: list, i:int):
    i += 1
    sum_ = 0
    while i > 0:
        sum_ += BIT[i]
        i -= i & (-i)
    return sum_

TC: O(lgn)
def update_tree(BIT: list, i:int, n:int, val):
    i += 1
    while i <= n:
        BIT[i] += val 
        i += i & (-i) # This basically add decimal value 
                        # corresponding to the last set from i.
                         #eg., 4 = 0100 => 4 + 4 => 8 
                           #     10 = 1010 +  0010 => 12 (1100) 

TC: O(nlgn)
def construct(arr: list):
    n = len(arr)
    BIT = [0] * (n + 1)
    for i in range(n):
        update_tree(BIT, i, n, arr[i])
    return BIT

arr = [2, 1, 1, 3]
BIT = construct(arr)
print(BIT)

val = get_sum(BIT, 3) - get_sum(BIT, 1)
print(val)

# Binary Indexed Tree requires less space and is easier to implement..

"""
Example BIT 

       8
   /   \\   \
  4     6   7
/   \
2   3   4
1

"""