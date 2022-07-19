class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, i):
            if i == len(s)//2:
                return
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            helper(s, i+1)
        helper(s, 0)
