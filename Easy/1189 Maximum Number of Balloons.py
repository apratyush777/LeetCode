class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i in d:
                d[i] += 1

        temp = min(d['l']//2, d['o']//2)
        minn = 99999999
        for i in d:
            minn = min(minn, d[i])
        minn = min(minn, temp)
        return minn
