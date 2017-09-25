def rotate_matrix(m):
    n = len(m)
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[j][-i-1] = m[i][j] 
    
    return

t = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(t)
print(t)

a = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
    ]
rotate_matrix(a)
print(a)
