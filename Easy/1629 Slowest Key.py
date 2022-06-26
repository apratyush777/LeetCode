class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = []
        maxx = releaseTimes[0]
        op = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i]-releaseTimes[i-1]
            if diff > maxx:
                # print(diff)
                op = keysPressed[i]
                maxx = diff
            elif diff == maxx:
                if ord(keysPressed[i]) > ord(op):
                    op = keysPressed[i]

        return op
