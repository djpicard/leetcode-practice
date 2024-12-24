class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        tmp = strs[0]
        for i in range(len(tmp)):
            for j in range(len(strs)):
                if not strs[j].startswith(tmp[:i+1]):
                    return output
            output += tmp[i]
        return output
                