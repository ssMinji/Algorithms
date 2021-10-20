n, m = map(int, input().split())

chk = [False for _ in range(n+1)]
a = [0 for _ in range(m)]
def solution(idx, n, m):
    if idx == m:
        print(' '.join(map(str, a)))
        return 
    for i in range(1, n+1):
        if chk[i]:
           continue
        chk[i] = True
        a[idx] = i
        solution(idx+1, n, m)
        chk[i] = False

solution(0, n, m)