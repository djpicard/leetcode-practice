class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = list(ransomNote)
        mg = list(magazine)
        while rn:
            if rn[0] in mg:
                mg.remove(rn[0])
                rn.pop(0)
            else:
                return False
        return True