class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]: return len(nums)
        if target < nums[0]: return 0
        
        def search(nums, target, high, low):
            mid = (high + low)//2
            print(f"high: {high}, low: {low}, mid: {mid}")
            if nums[mid] == target:
                return mid

            if high < low:
                return low

            if nums[mid] > target:
                return search(nums, target, mid -1, low)
            if nums[mid] < target:
                return search(nums, target, high, mid +1)

        return search(nums, target, len(nums) - 1, 0)
