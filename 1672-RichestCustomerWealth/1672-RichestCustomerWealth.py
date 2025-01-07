class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = 0
        for i in accounts:
            out = max(sum(i), out)
        return out