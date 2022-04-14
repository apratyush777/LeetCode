class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''
        for i in range(len(digits)):
            temp += str(digits[i])

        temp = int(temp)
        temp += 1
        temp = str(temp)
        return list(temp)
