class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        myMap = {}
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] not in myMap:
                if nums[i]-1 in myMap:
                    myMap[nums[i]] = myMap[nums[i]-1] + 1
                else:
                    myMap[nums[i]] = 1

        return max(myMap.values())