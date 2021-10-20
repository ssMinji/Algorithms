
def solution(n,m, mat):


    for i in range(n):
        for j in range(m):
            if check[i][j] :
                continue 
            ok = go(-1,-1, i, j, a[i][j])

            if ok:
                return 'Yes'
    return 'No'


def go(px, py, x, y, color):
    if check[x][y]:
        return True
    
    check[x][y] = True 
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx and nx < n and 0<= ny and ny < m:
            if (nx != px or ny != py) and a[nx][ny] == color:
                if go(x, y, nx, ny, color):
                    return True 
    return False 



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False]*m for _ in range(n)]
print(solution(n, m, a))
