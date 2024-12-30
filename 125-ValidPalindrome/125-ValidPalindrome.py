class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join([x for x in s if x.isalnum()]).lower()
        return pal == pal[::-1]