class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            temp = abs(i)-1
            nums[temp] = -1*abs(nums[temp])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)

        return ans
