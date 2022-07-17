class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        summ = 0
        minn = 999999999
        while j < len(nums):
            summ += nums[j]
            if summ < target:
                j += 1

            else:
                while summ >= target:
                    minn = min(minn, j-i+1)
                    summ -= nums[i]
                    i += 1
                j += 1
        if minn == 999999999:
            return 0

        return minn
