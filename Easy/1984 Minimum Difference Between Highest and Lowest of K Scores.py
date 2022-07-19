class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        i, j = 0, 0
        diff = 9999999
        while j < len(nums):
            if j-i+1 < k:
                j += 1
            else:
                diff = min(diff, nums[j]-nums[i])
                i += 1
                j += 1

        return diff
