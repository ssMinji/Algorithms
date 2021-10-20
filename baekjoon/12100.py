

LIMIT = 5
def gen(k):
    a =[0]*LIMIT
    for i in range(len(a)):
        a[i] = k&3
        k >>= 2
    return a

def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    for dir in dirs:
        ok = False # 블록이 움직였는지 체크
        merged = [[False]*n for _ in range(n)] # 합쳐졌는지 아닌지 체크 

        while True: # 0: down, 1: up, 2: left, 3:right 
            ok = False 
            if dir == 0:
                for i in range(n-2, -1, -1):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue

                        if d[i+1][j] == 0:
                            d[i+1][j] = d[i][j]
                            merged[i+1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True 
                        elif d[i+1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i+1][j]:
                                d[i+1][j] *= 2
                                merged[i+1][j] = True
                                d[i][j] = 0
                                ok = True 
            elif dir == 1:
                for i in range(1,n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue

                        if d[i-1][j] == 0:
                            d[i-1][j] = d[i][j]
                            merged[i-1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True 
                        elif d[i-1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i-1][j]:
                                d[i-1][j] *= 2
                                merged[i-1][j] = True
                                d[i][j] = 0
                                ok = True 
            elif dir == 2:
                for i in range(n):
                    for j in range(1,n):
                        if d[i][j] == 0:
                            continue

                        if d[i][j-1] == 0:
                            d[i][j-1] = d[i][j]
                            merged[i][j-1] = merged[i][j]
                            d[i][j] = 0
                            ok = True 
                        elif d[i][j-1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j-1]:
                                d[i][j-1] *= 2
                                merged[i][j-1] = True
                                d[i][j] = 0
                                ok = True 
            elif dir == 3:
                for i in range(n):
                    for j in range(n-2, -1, -1):
                        if d[i][j] == 0:
                            continue

                        if d[i][j+1] == 0:
                            d[i][j+1] = d[i][j]
                            merged[i][j+1] = merged[i][j]
                            d[i][j] = 0
                            ok = True 
                        elif d[i][j+1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j+1]:
                                d[i][j+1] *= 2
                                merged[i][j+1] = True
                                d[i][j] = 0
                                ok = True 
            if not ok:
                break
    ans = max([max(row) for row in d])
    return ans

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(1<<(LIMIT*2)):
    dirs = gen(i)
    cur = check(a, dirs)
    ans = max(ans, cur)

print(ans)
