class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 1
        return False

    '''
    better code
    if len(set(nums))!=len(nums):
        return True
    return False
    '''
