class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums=list(set(nums))
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return True
            if nums[mid]>nums[l]:
                if target>=nums[l] and target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target<=nums[r] and target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
                    
        return False