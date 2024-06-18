class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0

        while count <= len(nums):
            if count in nums:
                count += 1
                continue
            else:
                return count
        