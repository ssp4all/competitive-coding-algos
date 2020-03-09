https: // www.geeksforgeeks.org/number-of-steps-required-to-convert-a-binary-number-to-one/

"""
Input: str = “1001001”
Output: 12



Input: str = “101110”
Output: 8

Number ‘101110’ is even, after dividing it by 2 we get an odd number ‘10111’ so we will add 1 to it. Then we’ll get ‘11000’ which is even and can be divide three times continuously in a row and get ’11’ which is odd, adding 1 to it will give us ‘100’ which is even and can be divided 2 times in a row. As, a result we get 1.
So 8 times the above two operations were required in this number.
"""


def helper(ip):
    n = len(ip)
    r = n - 1
    count_ = 0
    while r > 0:
        if ip[r] == "0":
            count_ += 1
            r -= 1
        else:
            count_ += 1
            # if r == 1:
            #     return count
            while r > 0 and ip[r] == "1":
                r -= 1
                count_ += 1
            if r == 0:
                count_ += 1
            ip = ip[:r] + "1" + ip[r+1:]
            print(ip)
    return count_


ip = "101110"
x = helper(ip)
print(x)
