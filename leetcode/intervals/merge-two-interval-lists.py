https://leetcode.com/discuss/interview-question/algorithms/124616/facebook-merge-two-interval-lists

"""
Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution

A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.

For example,
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]

output [1,6], [8, 20]

"""

ip1 = [[1, 6], [8, 14], [16, 18]]
ip2 = [[2, 6], [8, 10], [11, 20]]

#now merge this two intervals
i, j = 0, 0
combined = []

if ip1[i][0] < ip2[j][0]:
    curr = ip1[i]
    i += 1
else:
    curr = ip2[j]
    j += 1

while i < len(ip1) or j < len(ip2):
    
    if j == len(ip2) or ip1[i][0] < ip2[j][0]:
        nxt = ip1[i]
        i += 1
    else:
        nxt = ip2[j]
        j += 1

    if curr[1] < nxt[0]:
        combined += [curr]
        curr = nxt
    else:
        curr[1] = max(curr[1], nxt[1])

combined += [curr]
print(combined)
    