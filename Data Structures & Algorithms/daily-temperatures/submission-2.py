class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res= [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                sT, sI = stack.pop()
                res[sI] = i - sI

            stack.append([t, i])
        
        return res
            

        
        
        
        
        
        
        
        
        
        
        
        
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