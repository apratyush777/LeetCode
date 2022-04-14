class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0
        k = len(nums)-1
        while j <= k:
            if nums[j] == 0:
                # swap(nums,i,j)
                nums[j] = nums[i]
                nums[i] = 0
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                # swap(nums,j,k)
                nums[j] = nums[k]
                nums[k] = 2
                k -= 1
