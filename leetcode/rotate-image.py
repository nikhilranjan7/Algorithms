class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # i j  i j
        # 0 0  0 len(m)-1
        # 0 1  1 len(m)-1
        # 0 2  2 len(m)-1
        # ...  ..........
        # 1 0  0 len(m)-1-i
        # 1 1  1 len(m)-1-1
        # ... ............
        # 3 3  3 len(m)-1-i

        m = len(matrix)
        if m < 2:
            return

        def do_box(m,n):
            i, j = m, n
            while(j<len(matrix[0])-1-n):
                t = 4
                new_i, new_j = i, j
                temp = matrix[new_i][new_j]
                while(t!=0):
                    new_i, new_j = new_j, len(matrix[0])-1-new_i
                    matrix[new_i][new_j], temp = temp, matrix[new_i][new_j]
                    t-=1
                j += 1

        i = 0
        while(i<len(matrix)//2):
            do_box(i,i)
            i += 1

'''
Time complexity: O(N*N) - Matrix is of N x N size
Space complexity: O(1)
'''

'''
Improve points:
-
'''
