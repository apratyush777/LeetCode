class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        else:
            i,j=0,1
            
            
            while(j<len(nums)):
                if nums[i]==nums[j]:
                    j+=1
                else:
                    i+=1
                    nums[i]=nums[j]
                    j+=1
                    
        return i+1