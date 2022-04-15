class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        diff1 = len(nums1)-m
        diff2 = len(nums2)-n
        for i in range(diff1):
            nums1.pop()
        for i in range(diff2):
            nums2.pop()
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
