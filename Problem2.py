'''
1. Exclusive OR (XOR) operator outputs 1 only if there is a single one in the input
2. Since there are duplicates of each number except one when you XOR the entire array youll only be left with that unique number
3. Return the XOR sum of the array

TC: O(1)
SC: O(1)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num
        
        return ans

