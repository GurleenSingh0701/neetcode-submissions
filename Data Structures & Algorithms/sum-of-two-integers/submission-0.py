class Solution:
    
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            # ^ finds the sum bits without carries
            # & finds the carry bits, then we shift them left
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # If 'a' is within the positive range of 32-bit signed int, return it.
        # Otherwise, convert the 32-bit mask value back to a Python negative int.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)