class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {(0, 0)}
        cnt = [0, 0]
        for i in path:
            if i == 'N':
                cnt[1] += 1
            elif i == 'E':
                cnt[0] += 1
            elif i == 'S':
                cnt[1] -= 1
            else:
                cnt[0] -= 1
            if tuple(cnt) not in d:
                d.add(tuple(cnt))
            else:
                return True

        return False
