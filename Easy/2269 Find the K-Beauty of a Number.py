class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        new = str(num)
        l = len(new)
        for i in range(l-k+1):
            new1 = new[i:i+k]
            if int(new1) == 0:
                continue
            elif num % int(new1) == 0:
                count += 1
        return count
