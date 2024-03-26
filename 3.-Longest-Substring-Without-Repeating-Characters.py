class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = len(s)
        if leng == 0:
            return 0
        if leng == 1:
            return 1
        l, r, maxi = 0, 0, 0
        check = set()
        
        while r < leng:
            if s[r] not in check:
                check.add(s[r])
                r += 1
                maxi = max(maxi, r - l)
            else:
                check.remove(s[l])
                l += 1
                
        return maxi