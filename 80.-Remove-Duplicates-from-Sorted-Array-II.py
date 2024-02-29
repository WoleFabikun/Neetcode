class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        myMap = {}

        for i in range(len(nums)):
            if nums[i] not in myMap:
                myMap[nums[i]] = 1
                nums[pointer] = nums[i]
                pointer += 1
            else:
                if myMap[nums[i]] == 1:
                    myMap[nums[i]] +=1 
                    nums[pointer] = nums[i]
                    pointer += 1
                else:
                    continue

        return pointer