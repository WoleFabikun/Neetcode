class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,res = 0,0
        keepCount = {}

        for r in range(len(s)):
            keepCount[s[r]] = 1 + keepCount.get(s[r],0)

            while (r - l + 1) - max(keepCount.values()) > k:
                keepCount[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res


# Sliding Window Problem
# Use a hashmap to keep track of the count of occurences of a certain letter in within the window
# If the limit of allowed character replacements is exceeded then the while loop will increment the 
#   left pointer to the right and remove the characters it is passing from the hashmap essentially shrinking the window
# It will then return the res which should be holding the largest substring that can be made with replacements

