class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validate(x,y):
            if board[x][y] == '.':
                return True

            #row & column-validation
            for i in range(9):
                if i != y and board[x][i] == board[x][y]:
                    return False
                if i != x and board[i][y] == board[x][y]:
                    return False

            #sub-box validation
            s_x = int(x//3)*3
            s_y = int(y//3)*3

            for i in range(s_x, s_x+3):
                for j in range(s_y, s_y+3):
                    if i == x and j == y:
                        continue
                    if board[i][j] == board[x][y]:
                        return False

            return True

        for x in range(9):
            for y in range(9):
                if validate(x,y) == False:
                    return False

        return True

'''
Time complexity: O(N*N) - N is 9
Space complexity: O(1)
'''

'''
Improve points:
-
'''
