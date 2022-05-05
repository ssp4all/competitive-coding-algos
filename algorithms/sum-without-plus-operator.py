#Do sum without a + operator 

def sum(x: str, y: str)->int:
    # x will store output 
    # y stores carry 
    while y != 0:
        sum = x ^ y #sum without carry 
        carry = (x & y) << 1 
        x, y = sum, carry
    return x 

op = sum(2, 2)
print(op)



####################

class Solution {
public:
    int sum(int num1, int num2) {
        return (num1 ^ num2) + 2 * (num1 & num2);
    }
};
