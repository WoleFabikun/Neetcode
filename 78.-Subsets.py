class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return 
            
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)

        dfs(0)
        return res

# Backtracking problem
# create a state space tree and traverse it using dfs technique to find all possible subsets
# add all subsets to a list and return it