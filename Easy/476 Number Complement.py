class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)
        b=b[2:]
        b=b.replace('1','2')
        b=b.replace('0','1')
        b=b.replace('2','0')
        return int(b,2)
    #  return int(bin(num)[2:].replace('1','2').replace('0','1').replace('2','0'),2)