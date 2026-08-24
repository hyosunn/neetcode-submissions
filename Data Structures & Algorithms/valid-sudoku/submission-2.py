class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue

                if n in rowMap[i] or n in colMap[j] or n in squares[(i // 3, j // 3)]:
                    return False
                rowMap[i].add(n)
                colMap[j].add(n)
                squares[(i // 3, j // 3)].add(n)
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        OPTIMAL SOLUTION (O(n^2) time and space)
        rowMap, colMap = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowMap[i] 
                or board[i][j] in colMap[j] 
                or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        return True
        """
        
                





            
            


        

