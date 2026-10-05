class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {']' : '[', '}' : '{', ')' : '('}

        for b in s:
            if b in close:
                if stack and stack[-1] == close[b]:
                   stack.pop()
                else: return False
            else: stack.append(b)
        return not stack