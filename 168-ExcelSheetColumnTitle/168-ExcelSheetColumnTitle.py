class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        offset = 65
        out = ""
        while columnNumber > 0:
            x = (columnNumber-1) // 26
            y = (columnNumber-1) % 26
            if y >= 0:
                out += chr(offset + y)
            columnNumber = x
        return out[::-1]
