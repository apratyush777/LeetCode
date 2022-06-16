class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = len(s)
        i, j = 0, l-1
        a = []
        for k in s:
            a.append(k)
        while i < j:
            if ord(s[i]) < 65 or ord(s[i]) > 90 and ord(s[i]) < 97 or ord(s[i]) > 122:
                i += 1
            elif ord(s[j]) < 65 or ord(s[j]) > 90 and ord(s[j]) < 97 or ord(s[j]) > 122:
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        ans = ''
        for k in a:
            ans += k

        return ans
