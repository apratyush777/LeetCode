class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        d = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                if secret[i] in d:
                    d[secret[i]] += 1
                else:
                    d[secret[i]] = 1
        # print(d)
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if guess[i] in d and d[guess[i]] != 0:
                    d[guess[i]] -= 1
                    b += 1

        ans = str(a)+'A'+str(b)+'B'
        return ans
