def getkey(dic, val):
    for key, value in dic.items():
        if val == value:
            return key


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] not in dic.values():
                dic[i] = nums[i]
            else:
                return [i, getkey(dic, target-nums[i])]
