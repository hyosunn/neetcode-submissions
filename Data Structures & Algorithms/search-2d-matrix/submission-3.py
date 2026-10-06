class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1

        while l1 <= r1:
            m1 = (l1 + r1)// 2

            if target < matrix[m1][0]:
                r1 = m1 - 1
            elif target > matrix[m1][-1]:
                l1 = m1 + 1
            else:
                break

        l2, r2 = 0, len(matrix[m1]) - 1
        while l2 <= r2:
            m2 = (l2 + r2)// 2

            if target < matrix[m1][m2]:
                r2 = m2 - 1
            elif target > matrix[m1][m2]:
                l2 = m2 + 1
            else:
                return True
        
        return False
        

            









    



    """
    OPTIMAL 1D ARRAY ABSTRACTION SOLUTION:
    - This is easier logic and still runtime of O(log(n * m))

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2
            row = m // COLS
            col = m % COLS

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False

    

    Another options is Neetcodes way, which is the find with row its in
    FIRST by doing binary search on the first or last number in each row.
    
    Then, once you find the right row, do binary search again to find the
    exact target number (if it exists).
    """
            


