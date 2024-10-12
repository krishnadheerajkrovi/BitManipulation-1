'''
1. We generally get the integer quotient n by removing divisor from dividend n number of times. 
2. We can speed up by removing divisor*2^n to bring down the times logarithmcally.
3. So we use bitwise operators to perform equivalent of multiplication (divisor*2^n == divisor << n)
4. So we repeat this process until the numerator becomes less than divisor. Number of divisors used at each step is 2^i or 1 << i.

TC: O(log(N))
SC: O(1)
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor: 
            return 1
        sign = True
        if (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0): 
            sign = False
        
        num = abs(dividend)
        dr = abs(divisor)
        ans = 0
        while num >= dr:
            ct = 0
            while num >= (dr << (ct+1)):
                ct += 1
            ans += 1 << ct
            num -= (dr << ct)
        if ans >= (1 << 31):
            if sign:
                return (1 << 31) - 1 
            else:
                return  0 - (1 << 31) 
        return ans if sign else 0 - ans





        
        