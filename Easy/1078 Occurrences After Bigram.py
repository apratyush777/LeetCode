class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.split()
        op = []
        for i in range(len(arr)-2):
            if arr[i] == first and arr[i+1] == second:
                op.append(arr[i+2])
        return op
