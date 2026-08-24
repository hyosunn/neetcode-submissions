class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack.pop() != bracketMap[c]:
                    return False
        if stack:
            return False
        return True