"""
Given a 2d array in which each row is sorted and rotated, you need to come up with an algorithm which efficiently sort the entire 2d matrix in descenting order.

eg:
input: arr[][] = {
{41, 45, 20, 21},
{1 ,2, 3, 4},
{30, 42, 43, 29 },
{16, 17, 19, 10}
}

output: {
{ 45, 43, 42, 41},
{30, 29, 21, 20},
{19, 17, 16, 10},
{4, 3, 2, 1}
}
"""


from functools import reduce
input = [[41, 45, 20, 21], [1, 2, 3, 4], [30, 42, 43, 29], [16, 17, 19, 10]]
length_of_sublist = len(input[0])
sorted_list = iter(sorted(reduce(lambda x, y: x+ y, input), reverse=True))
print(list(zip(*[sorted_list] * length_of_sublist)))