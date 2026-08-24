class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                rmvd = stack.pop()
                ans[rmvd[0]] = i - rmvd[0]
            stack.append((i, t))
            
        return ans
                



        
        
        
        
        
        
        
        
        
        
        
        
        """
        OPTIMAL SOLUTION (O(n) time and space with
                          Monotonic Decreasing Stack)
                          
        res = [0] * len(temperatures)
        stack = [] #pair[temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        
        return res

        """