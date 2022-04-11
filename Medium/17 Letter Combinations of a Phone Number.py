class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(d[digits[0]])
        elif len(digits) == 2:
            arr = []

            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    temp = ''
                    temp += i
                    temp += j
                    arr.append(temp)

            return arr
        elif len(digits) == 3:
            arr = []
            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    for k in d[digits[2]]:
                        temp = ''
                        temp += i
                        temp += j
                        temp += k
                        arr.append(temp)

            return arr
        else:
            arr = []
            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    for k in d[digits[2]]:
                        for l in d[digits[3]]:
                            temp = ''
                            temp += i
                            temp += j
                            temp += k
                            temp += l
                            arr.append(temp)

            return arr
