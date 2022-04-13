class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ''
        for i in s:
            if i.isalnum():
                temp += i

        if temp == temp[::-1]:
            return True
        return False
