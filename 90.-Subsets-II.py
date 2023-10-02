class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        seen = set()

        def dfs(i):
            if i >= len(nums) and tuple(sorted(subsets)) in seen:
                return 

            if i >= len(nums):
                res.append(subsets.copy())
                seen.add(tuple(sorted(subsets)))
                return 
            
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)

        dfs(0)
        return res

# The same approach as the first subset problem, just check for duplicates after sorting each subset