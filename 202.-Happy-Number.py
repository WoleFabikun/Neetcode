class Solution:
    def isHappy(self, n: int) -> bool:
        def transform(num):
            numStr = str(num)
            add = 0

            for i in numStr:
                add += int(i) * int(i)

            return add

        seen = set()
        trans = transform(n)

        while trans not in seen:
            if trans == 1:
                return True
            seen.add(trans)
            trans = transform(trans)

        return False