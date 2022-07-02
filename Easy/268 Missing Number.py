class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)+1
        summ = ((l-1)*l)//2
        summ2 = 0
        for i in nums:
            summ2 += i
        return summ-summ2
