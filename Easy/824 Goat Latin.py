class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr = sentence.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt = 1
        ans = ''
        for i in arr:
            temp = 'a'*cnt
            cnt += 1
            if i[0] in vowels:
                i += 'ma'
                i += temp
                ans += i
                ans += ' '
            else:
                ad = i[0]
                i = i[1:]
                i += ad
                i += 'ma'
                i += temp
                ans += i
                ans += ' '

        l = len(ans)
        ans = ans[:l-1]
        return ans
