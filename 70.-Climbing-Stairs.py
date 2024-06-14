class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(n: int, memo: dict[int,int]) -> int:
            if n==0 or n==1:
                return 1
            
            if n not in memo:
                memo[n] = climb(n-1, memo) + climb(n-2, memo)
            
            return memo[n]
        return climb(n,memo)