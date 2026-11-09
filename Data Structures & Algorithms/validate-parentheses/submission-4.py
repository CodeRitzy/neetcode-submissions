class Solution:
    def isValid(self, s: str) -> bool:
        sHash = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for c in s:
            if c in sHash:
                if stack and stack[-1] == sHash[c]:
                    stack.pop()
                else: return False
            else: stack.append(c)
        return not stack