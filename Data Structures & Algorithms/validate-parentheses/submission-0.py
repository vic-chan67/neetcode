class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if len(stack) == 0 or brackets[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        