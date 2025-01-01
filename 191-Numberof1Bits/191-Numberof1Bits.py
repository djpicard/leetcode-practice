class Solution:
    def hammingWeight(self, n: int) -> int:
        tmp = bin(n).replace("0b", "")
        out = 0
        for i in tmp:
            if i == "1":
                out += 1
        return out