class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i, j = 0, 0
        l = len(arr)
        summ = 0
        cnt = 0
        while j < l:
            summ += arr[j]
            avg = summ//k
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if avg >= threshold:
                    cnt += 1
                j += 1
                summ -= arr[i]
                i += 1

        return cnt
