class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        if len(arr) > 2:
            for i in range(len(arr)-2):
                diff1 = abs(arr[i+1]-arr[i])
                diff2 = abs(arr[i+2]-arr[i+1])

                if diff1 != diff2:
                    return False
            return True
        else:
            return True
