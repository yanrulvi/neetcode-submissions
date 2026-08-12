class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        while up <= down:
            y = (down+ up) // 2
            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                x = (left + right) // 2
                if matrix[y][x] > target:
                    right = x - 1
                elif matrix[y][x] < target:
                    left = x + 1
                else:
                    return True
            
            if matrix[y][x] > target:
                down = y - 1
            else:
                up = y + 1

        return False