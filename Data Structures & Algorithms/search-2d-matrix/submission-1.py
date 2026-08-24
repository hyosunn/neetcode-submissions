class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix[0]) - 1
        l2, r2 = 0, len(matrix) - 1

        while l1 <= r1:

            while l2 <= r2:
                mid2 = (l2 + r2) // 2

                if matrix[mid2][-1] >= target >= matrix[mid2][0]:
                    l2, r2 = mid2, mid2
                    break;
                elif target < matrix[mid2][0]:
                    r2 = mid2 - 1
                else:
                    l2 = mid2 + 1
            
            if l2 > r2:
                return False
            
            mid1 = (l1 + r1) // 2
            if target < matrix[l2][mid1]:
                r1 = mid1 - 1
            elif target > matrix[l2][mid1]:
                l1 = mid1 + 1
            else:
                return True
    
        return False
            


