class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max1 = -2**31
        max2 = -2**31
        max3 = -2**31
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i

        if len(nums) > 2:
            return max3
        else:
            return max(nums)
