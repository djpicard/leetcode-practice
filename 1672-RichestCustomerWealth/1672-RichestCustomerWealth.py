class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = 0
        for i in accounts:
            tmp = sum(i)
            if tmp > out:
                out = tmp
        return out