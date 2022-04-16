def bs(l, r, nums, target):  # binary search function
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid] > target:
            r = mid-1
        else:
            return mid
    return -1


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        else:
            b = 0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    b = i
                    break
             # calling binary search function
            call1 = bs(0, b, nums, target)
            if call1 != -1:
                return call1
            else:
                call2 = bs(b+1, len(nums)-1, nums, target)
                return call2
