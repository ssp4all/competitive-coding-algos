
"""
find maximum profit made by salesman after travelling between two cities. Salesman can make profit only in one city at a day and requires some travel cost to travel between the cities.
"""

a = [3, 7,2,10]
b = [1,100,1,10]
c = 2

def helper(a, b):
    if not a and not b:
        return 0
    first =  max(a[0] + helper(a[1:], b[1:]), \
                b[0] + helper(a[1:], b[1:]) - c)
    second =  max(a[0] + helper(a[1:], b[1:]) - c, \
                b[0] + helper(a[1:], b[1:]))
    return max(first, second)

x = helper(a, b) 
print(x)