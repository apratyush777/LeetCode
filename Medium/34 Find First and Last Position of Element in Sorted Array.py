class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, m = 0, 0
        h = len(nums)-1
        temp = -1
        length = len(nums)
        while(l <= h):
            m = (h+l)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                h = m-1
            else:
                temp = m
                break
        print(temp)
        if temp == -1:
            return [-1, -1]
        else:
            j = temp
            while j > 0:
                if nums[j-1] == target:
                    temp -= 1
                j -= 1

            i = temp
            ans = temp
            while i < length:
                if nums[i] == target:
                    ans = i
                i += 1

            return [temp, ans]
