class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == len(set(nums)):
            return []

        res = [0] * (len(nums) - len(set(nums)))
        val = [0] * (len(nums)+1)
        count = 0
        

        for num in nums:
            val[num] += 1
            if val[num] == 2:
                res[count] = num
                count += 1

        return res

# Brute force solution but done fast. Took 7 minutes to code and 5 minutes to debug