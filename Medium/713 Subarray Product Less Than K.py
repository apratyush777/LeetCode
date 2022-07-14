class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        i, j, prod = 0, 0, 1
        cnt = 0
        while j < len(nums):
            prod *= nums[j]
            while prod >= k:
                prod /= nums[i]
                i += 1
            cnt += j-i+1
            j += 1
        return cnt
