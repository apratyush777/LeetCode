class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        temp1 = 0
        temp2 = 0
        for i in range(l1):
            temp1 += (ord(num1[i])-48)*(10**(l1-1-i))

        for i in range(l2):
            temp2 += (ord(num2[i])-48)*(10**(l2-1-i))

        return str(temp1+temp2)
