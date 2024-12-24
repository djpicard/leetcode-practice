class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] = digits[i] +1
            if digits[i] <= 9: break
            if digits[i] == 10:
                digits[i] = 0
            if i == len(digits) - 1: 
                digits.append(1)

        return digits
