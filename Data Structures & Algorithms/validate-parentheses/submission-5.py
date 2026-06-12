class Solution:
    def isValid(self, s: str) -> bool:
        openb = ("(", "{", "[")
        closedb = (")", "}", "]")
        stack = []
        for i, x in enumerate(s):   
            if x in openb:
                stack.append(x)
            if x in closedb:
                ind = closedb.index(x)
                y = openb[ind]
                if stack and y == stack[-1]:
                    stack.pop()
                else:
                    return False 
        if len(stack) != 0:
            return False
        else: 
            return True