def zero_matrix(a):
    n = len(a)
    m = len(a[0])
    b = [[0 for _ in range(m)] for _ in range(n)]
    ans = [[0 for _ in range(m)] for _ in range(n)]
    row_zero = [[0 for _ in range(m)] for _ in range(n)]
    column_zero = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        flag = 0
        for j in range(m):
            row_zero[i][j] = a[i][j]
            if a[i][j] == 0:
                flag = 1
                break
        if flag == 1:
            row_zero[i] = [0 for _ in range(m)]
    
    for j in range(m):
        flag = 0
        for i in range(n):
            column_zero[i][j] = a[i][j]
            if a[i][j] == 0:
                flag = 1
                break
        if flag == 1:
            for i in range(n):
                column_zero[i][j] = 0
    
    for i in range(n):
        for j in range(m):
            if row_zero[i][j] == 0 or column_zero[i][j] == 0:
                pass
            else:
                ans[i][j] = a[i][j]
        
    return ans
  
print(zero_matrix([[1,2,3,4],[5,6,0,8],[9,0,3,2]]))
