class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1, num2, num3 = '', '', ''
        for i in firstWord:
            temp = str(ord(i)-97)
            num1 += temp
        for i in secondWord:
            temp = str(ord(i)-97)
            num2 += temp
        for i in targetWord:
            temp = str(ord(i)-97)
            num3 += temp
        if int(num1)+int(num2) == int(num3):
            return True
        return False
