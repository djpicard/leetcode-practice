class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]: return len(nums)
        if target < nums[0]: return 0
        
        def search(nums, target, high, low):
            mid = int((high + low)/2)
            if nums[mid] == target:
                return mid

            if high - low == 1:
                return high

            if nums[mid] > target:
                return search(nums, target, mid, low)
            if nums[mid] < target:
                return search(nums, target, high, mid)

        return search(nums, target, len(nums) - 1, 0)