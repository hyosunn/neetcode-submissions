class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")": "(", "]": "[", "}": "{"}

        for b in s:
            if b in bracketMap:
                if not stack or stack[-1] != bracketMap[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        
        return stack == []
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    OPTIMAL SOLUTION --------- (O(n) time and space complexity)
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack.pop() != bracketMap[c]:
                    return False
        
        return not stack
    """

    """Neetcode soliution in the video 10:27 is essentially the same
        except he uses peek operation before popping, but no difference in 
        time and space complexity mostly.

        NOTE: for a stack, your key operations are 
        append, pop and peeking.
        Peeking is calling stack[-1], which is the top element in the stack.
        but it doesn't remove it.
    """