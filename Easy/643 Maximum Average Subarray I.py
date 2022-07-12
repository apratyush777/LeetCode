class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j, max_avg = 0, 0, -999999999
        l = len(nums)
        summ = 0
        while j < l:
            summ += nums[j]
            avg = summ/k
            if j-i+1 < k:
                j += 1
            else:
                max_avg = max(max_avg, avg)
                summ -= nums[i]
                i += 1
                j += 1
        return max_avg
