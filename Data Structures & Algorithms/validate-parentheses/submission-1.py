class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {']' : '[', ')' : '(', '}' : '{'}

        for b in s:
            if b in closing:
                if stack and stack[-1] == closing[b]:
                    stack.pop()
                else: return False
            else: stack.append(b)
        if not stack:
            return True
        return False