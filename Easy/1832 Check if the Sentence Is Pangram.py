class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for i in sentence:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in range(26):
            if chr(i+97) not in d:
                return False

        return True
