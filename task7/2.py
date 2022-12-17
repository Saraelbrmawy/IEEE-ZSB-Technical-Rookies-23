class Solution(object):
    def lastStoneWeight(self, stones):
        if len(stones) == 1:
                return stones[0]

        elif len(stones) >= 2:
            stones = sorted(stones)
            a, b = stones[-1], stones[-2]
            if a == b:
                stones.remove(stones[-1])
                stones.remove(stones[-1])
            else:
                a = a-b
                stones[-1] = a
                stones.remove(stones[-2])
            return self.lastStoneWeight(stones)
        else:
            return 0
m=Solution()
print(m.lastStoneWeight([2,7,4,1,8,1]))