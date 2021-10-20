def solution(mat):
    ans = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j+1 < n:
                mat[i][j], mat[i][j+1] =  mat[i][j+1], mat[i][j]
                # tmp = check(mat)
                tmp = check(mat, i, i, j, j+1)
                ans = max(ans, tmp)
                mat[i][j], mat[i][j+1] =  mat[i][j+1], mat[i][j]
            if i+1 < n:
                mat[i][j], mat[i+1][j] =  mat[i+1][j], mat[i][j]
                # tmp = check(mat)
                tmp = check(mat, i, i+1, j, j)
                ans = max(ans, tmp)
                mat[i][j], mat[i+1][j] =  mat[i+1][j], mat[i][j]
    return ans

def check_old(mat):
    n = len(mat)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if mat[i][j] == mat[i][j-1]:
                cnt +=1 
            else:
                cnt = 1 
            ans = max(ans, cnt)
        cnt = 1
        for j in range(1, n):
            if mat[j][i] == mat[j-1][i]:
                cnt += 1
            else: 
                cnt = 1
            ans = max(ans, cnt)
    return ans 

def check(mat, start_row, end_row, start_col, end_col):
    ans = 1
    for i in range(start_row, end_row+1):
        cnt = 1
        for j in range(1, len(mat)):
            if mat[i][j] == mat[i][j-1]:
                cnt +=1 
            else:
                cnt = 1
            ans = max(ans, cnt)
    for i in range(start_col, end_col+1):
        cnt  = 1
        for j in range(1, len(mat)):
            if mat[j][i] == mat[j-1][i]:
                cnt +=1 
            else:
                cnt = 1
            ans = max(ans, cnt)

    return ans 

n = int(input())
mat = [list(input()) for _ in range(n)]

print(solution(mat))