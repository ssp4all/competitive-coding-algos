https://stackoverflow.com/questions/5284898/implement-division-with-bit-wise-operator

# implment division without / and % operators


remainder = 0
def division(tempDivident, tempDivisor):
    global divisor, remainder
    quotient = 1
    if tempDivident == tempDivisor:
        remainder = 0
        return 1
    elif tempDivident < tempDivisor:
        remainder = tempDivident
        return 0 
    
    while (tempDivisor << 1) <= tempDivident:
        quotient <<= 1
        tempDivisor <<= 1 
    
    quotient += division(tempDivident - tempDivisor, divisor)
    return quotient


divisor = 3
quotient = division(13, 3)
print(quotient, remainder)

####################################
addition using bit manipulation 
####################################

def addition(x, y):
    while y > 0:
        carry = x & y 
        x = x ^ y 
        y = carry << 1 
    return x 
"""
divident = 13 
divisor = 3 

f(13, 3) 13 = 1101
              0100 0011 3 -> 6 -> 12 
                   11000
16 8 4 2 1

4 / 2 
100 / 10 
15 / 5  -> 3, 0
1111 / 0101 -> 2, 0
F(5, 5)

for addition 
15 = 01111
5 =  00101
----------
20 = 10100

15 = 01111
5 =  00101
C    01010
     01010  
     10100  
----------
C    00000
     11110       
    
"""