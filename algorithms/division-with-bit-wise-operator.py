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


