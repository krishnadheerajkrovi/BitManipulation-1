'''
1. The idea behind this is when we take the xor sum of all the numbers, we will have the bits set where the two unique numbers differ.
2. Find that unique diff_bit, and later xor add the numbers into their respective bins ( by checking if that diff_bit is set in the number)
3. Now we have the result of each group holding the unique number

TC: O(n)
SC: O(1)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        xor = 0
        for num in nums:
            xor ^= num

        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
        
        a, b = 0, 0
        for num in nums:
            if diff_bit & num:
                a = a^num
            else:
                b = b^num
        
        return [a,b]