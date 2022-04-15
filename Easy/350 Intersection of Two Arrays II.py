from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = collections.Counter(nums1)
        final = []
        for i in nums2:
            if i in d:
                if d[i] > 1:
                    d[i] -= 1
                else:
                    del d[i]
                final.append(i)

        return final
