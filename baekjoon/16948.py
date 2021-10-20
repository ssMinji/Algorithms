from collections import deque
n = int(input())
sr, sc, er, ec = map(int, input().split())
a = [[0]*n for _ in range(n)]
q = deque()
q.append((sr, sc))
dist = [[-1]*n for _ in range(n)]
dist[sr][sc] = 0

dx = [0,0,2,2,-2,-2]
dy = [2,-2,-1,1,-1,1]
while q:
    x, y = q.popleft()

    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))
            

if dist[er][ec] == 0:
    print(-1)
else:
    print(dist[er][ec])

