# Backtracking problem

# My attempt, close but not quite
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i, currentSum):
            if currentSum == target:
                res.append(subsets.copy())
                return 
            
            elif currentSum > target:
                return

            else:
                subsets.append(candidates[i])
                currentSum += candidates[i]
                dfs(i, currentSum)
                subsets.pop()
                dfs(i+1, currentSum)
                

        dfs(0, 0)
        return res

# Correct Solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i, total):
            if total == target:
                res.append(subsets.copy())
                return
            elif i >= len(candidates) or total > target:
                return

            else:
                subsets.append(candidates[i])
                dfs(i, total + candidates[i])
                subsets.pop()
                dfs(i + 1, total)

        dfs(0, 0)
        return res
            
            
            