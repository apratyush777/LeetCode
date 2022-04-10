class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        l = len(s)

        arr = []
        temp = ''
        for i in range(l):
            if s[i] != ' ':
                temp += s[i]
            else:
                if temp != '':
                    arr.append(temp)
                    temp = ''
        arr.append(temp)
        for i in range(len(arr)-1, -1, -1):
            ans += arr[i]
            ans += ' '
        t = ans.strip()
        return t
