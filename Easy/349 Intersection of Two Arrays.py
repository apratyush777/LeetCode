class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        d = {}
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in nums2:
            if i in d:
                d[i] -= 1
        li = []
        for i in d:
            if d[i] == 0:
                li.append(i)
        return li
