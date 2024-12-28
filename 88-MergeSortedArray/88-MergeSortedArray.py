class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # remove extra 
        for i in range(n):
            nums1.pop(-1)
        
        # track index
        index = 0
        while nums2 and index < len(nums1):
            if nums1 and nums1[index] > nums2[0]:
                nums1.insert(index, nums2[0])
                nums2.pop(0)
            index += 1 
        
        # if we have leftover items in nums2 just append then to the end
        nums1.extend(nums2)