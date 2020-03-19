class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        def possible_index(i, j):
            if i >= len(mat):
                i = len(mat)-1
            if j >= len(mat[0]):
                j = len(mat[0])-1

            return i, j

        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        # row-wise
        for i in range(len(mat)):
            for j in range(1,len(mat[0])):
                mat[i][j] += mat[i][j-1]

        # column-wise
        for j in range(len(mat[0])):
            for i in range(1,len(mat)):
                mat[i][j] += mat[i-1][j]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_index, col_index = possible_index(i+k, j+k)

                if 0 <= i-k-1 < len(mat) and 0 <= j-k-1 < len(mat[0]):

                    answer[i][j] = mat[row_index][col_index] - mat[row_index][j-k-1] - mat[i-k-1][col_index] + mat[i-k-1][j-k-1]

                elif 0 <= i-k-1 < len(mat) and not (0 <= j-k-1 < len(mat[0])):

                    answer[i][j] = mat[row_index][col_index] - mat[i-k-1][col_index]

                elif not(0 <= i-k-1 < len(mat)) and 0 <= j-k-1 < len(mat[0]):

                    answer[i][j] = mat[row_index][col_index] - mat[row_index][j-k-1]

                else:
                    answer[i][j] = mat[row_index][col_index]

        return answer

'''
Time complexity: O(N*M) - N is number of rows and M in number of columns in mat
Space complexity: O(N*M)
'''

'''
Improve points:
- Convert row-wise and column-wise loop to one loop structure
- Check other solutions in discussions
'''
