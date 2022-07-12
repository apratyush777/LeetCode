class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if k <= len(nums)//2:
            i, j = 0, 0
            op = []
            summ = 0
            l = len(nums)
            for it in range(k):
                op.append(-1)

            while j < l:
                summ += nums[j]
                if j-i < 2*k:
                    j += 1

                else:
                    avg = summ//(2*k+1)
                    op.append(avg)
                    summ -= nums[i]
                    i += 1
                    j += 1

            for it in range(k):
                op.append(-1)
            return op
        else:
            op = []
            for it in range(len(nums)):
                op.append(-1)
            return op
