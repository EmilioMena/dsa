"""

Given two binary strings a and b, return their sum as a binary string.

"""

"""
to avoid converting to integers and then back to binary, which is O(N+M) and causes overflow in java,
we do bit-by-bit manipulation. It's very similar to adding base 10 numbers on paper.
"""

class Solution(object):
    
    def addBinary(self, a, b):
        if len(a) >= len(b):
            largest, smallest = a, b
        else:
            largest, smallest = b, a
        
        carry_over = 0
        result = ''
        for i in range(-1, -len(largest)-1, -1):
            sum_at_idx = int(largest[i]) + carry_over
            sum_at_idx = sum_at_idx + int(smallest[i]) if i >= -len(smallest) else sum_at_idx
            
            if sum_at_idx == 3:
                carry_over = 1
                result = '1' + result
            elif sum_at_idx == 2:
                carry_over = 1
                result = '0' + result
            elif sum_at_idx == 1:
                carry_over = 0
                result = '1' + result
            else:
                carry_over = 0
                result = '0' + result
                                
        return str(carry_over) + result if carry_over == 1 else result
