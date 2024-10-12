'''
1. Character takes 8 bits, whereas a binary integer takes only 2 bits. So we can reduce comparison of 10 chars from 80 bits to 20.
2. First encode the 4 chars to 4 integers, have a mask bit of length 20 to extract that window from that string.
3. For every new character processing shift the 20 bit placholder to left to accomodate new char (2 bit int).
4. Maintain a set to keep track of seen substrings. We can use the hashValue ( bitstring) to check that. 
5. If in case we see this substring again, add that substring from s to the repeated set.

TC: O(n)
SC: O(n)
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 10:
            return []

        hashMap = {
            'A': 0, 'C': 1, 'G': 2, 'T': 3
        }

        seen = set()
        repeated = set()

        hashValue = 0 
        mask_bit = ( 1 << 20) - 1

        for i in range(len(s)):
            hashValue = ((hashValue << 2) | hashMap[s[i]]) & mask_bit

            if i >= 9:
                if hashValue not in seen:
                    seen.add(hashValue)
                else:
                    repeated.add(s[i-9:i+1])
        return list(repeated)