class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = {}
        for i in nums:
            if tmp.get(i) == None:
                tmp[i] = 0
            else: 
                return True
        return False