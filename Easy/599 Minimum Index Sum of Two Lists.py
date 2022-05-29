class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        cnt = 0
        for i in list1:
            if i not in d:
                d[i] = cnt
            cnt += 1
        cnt = 0
        d2 = {}
        minn = 200000000
        for i in list2:
            if i in d:
                d2[i] = cnt+d[i]
                minn = min(minn, d2[i])
            cnt += 1
        op = []
        for i in d2:
            if d2[i] == minn:
                op.append(i)

        return op
