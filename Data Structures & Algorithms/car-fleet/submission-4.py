class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for car in sorted(pairs)[::-1]:
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)

            

        
        
        
        
        
        
        
        
        
        
        
        
        

        """ TIME: O(nlogn) and space is O(n)
        
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        """

        