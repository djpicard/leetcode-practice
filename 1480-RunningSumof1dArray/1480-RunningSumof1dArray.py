class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] += cur
            cur += tmp
        return nums
        