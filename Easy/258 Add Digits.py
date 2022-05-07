#first method (naive)
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
            
        
#2nd method (using digital root method )
class Solution:
    def addDigits(self, num: int) -> int:
        ans = num%9
        if ans!=0:
            return ans
        elif num==0:
            return 0
        return 9
