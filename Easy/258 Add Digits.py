def fun(s):
    summ=0
    for i in s:
        summ+=int(i)
        
    return str(summ)
        
class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        while len(s)!=1:
            temp=fun(s)
            s=temp
        return s
            