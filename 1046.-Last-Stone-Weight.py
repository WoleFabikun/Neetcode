class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)

            if max1 == max2:
                continue
            else:
                stones.append(max1-max2)


        return stones[0] if stones else 0