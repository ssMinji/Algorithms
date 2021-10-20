n, m, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = -999999999
def solution(px, py, cnt, sum):
    if cnt == k:
        global ans
        ans = max(ans, sum)
        return

    for i in range(px, n):
        for j in range(py if i == px else 0, m):
            if chk[i][j]: 
                continue
            flag = True 
            for a in range(4):
                x = i + dx[a]
                y = j + dy[a]
                if x >= 0 and x < n and y >= 0 and y < m:
                    if chk[x][y]:
                        flag = False 
            if flag:
                chk[i][j] = True 
                solution(x, y, cnt+1, sum+mat[i][j])
                chk[i][j] = False 

solution(0, 0)
print(ans) 

            
                

