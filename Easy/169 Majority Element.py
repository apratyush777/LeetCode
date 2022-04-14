class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        mode = None
        for i in nums:
            if cnt == 0:
                mode = i
            if mode == i:
                cnt += 1
            else:
                cnt -= 1

        return mode
