class Solution:
    def convert(self, s: str, numRows: int) -> str:
        op=''
        l=len(s)
        if numRows==1:
            return s
        for i in range(numRows):
            temp1=(numRows-1)*2
            if i==0:
                for j in range(0,l,temp1):
                    op+=s[j]
            elif i==numRows-1:
                for j in range(numRows-1,l,temp1):
                    op+=s[j]
            else:
                #temp2=(numRows-1)*2-2*i 
                for j in range(i,l,temp1):
                    op+=s[j]
                    if j+temp1-(2*i)<l:
                        op+=s[j+temp1-(2*i)]
                
        return op
                