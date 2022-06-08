class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = len(s)
        i, j = 0, l-1
        arr = []
        for k in s:
            arr.append(k)
        print(arr)
        while i < j:
            if s[i] in v and s[j] in v:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif s[i] not in v:
                i += 1
            elif s[j] not in v:
                j -= 1
        ans = ''
        for k in arr:
            ans += k

        return ans
