class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        output = 0
        skip = False
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if "C" == s[i] or "X" == s[i] or"I" == s[i]:
                if i+1 < len(s) and s[i:i+2] in symbols:
                    output += symbols[s[i:i+2]]
                    skip = True
                    continue
            output += symbols[s[i]]

        return output