class Solution:
    def reformatDate(self, date: str) -> str:
        if ord(date[1]) >= 48 and ord(date[1]) <= 57:
            n = date[0:2]
            m = date[5:8]
            y = date[9:]
        else:
            n = date[0]
            m = date[4:7]
            y = date[8:]
        d = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        if len(n) == 1:
            n = '0'+n
        op = y+"-"+d[m]+"-"+n
        return op
