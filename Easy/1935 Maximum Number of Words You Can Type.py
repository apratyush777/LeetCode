class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split()
        cnt = 0
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(len(temp)):
                if temp[j] in brokenLetters:
                    cnt += 1
                    break

        return len(arr)-cnt
