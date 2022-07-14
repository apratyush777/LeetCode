class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        op = []
        i, j = 0, 0
        d = []
        while j < len(nums):
            while d and nums[d[-1]] < nums[j]:
                d.pop()
            d.append(j)
            if d[0] < i:
                d.pop(0)
            if j-i+1 == k:
                op.append(nums[d[0]])
                i += 1
            j += 1
        return op
