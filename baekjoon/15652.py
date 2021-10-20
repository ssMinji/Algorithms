n, m = map(int, input().split())
a = [0 for _ in range(m)]

def solution(idx, n, m):
    if idx ==m:
        print(' '.join(map(str, a)))
        return 

    for i in range(1, n+1):
        if idx > 0 and a[idx-1] > i :
            continue 
        a[idx] = i
        solution(idx+1, n, m)

solution(0, n, m)