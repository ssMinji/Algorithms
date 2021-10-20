import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
def solution(a, b):
    
    
    if check[a][b]:
        return 
    check[a][b] = True
    x = [a, b, total-(a+b)]
    for i in range(3):
        for j in range(3):
            if x[i] < x[j]:
                y = [a, b, total-(a+b)]
                y[i] += x[i]
                y[j] -= x[i]
                solution(y[0], y[1])
    


    

a, b, c = map(int, input().split())
total = a+b+c
if total % 3 != 0:
    print(0)
else:
    solution(a,b)
    if check[total//3][total//3]:
        print(1)
    else:
        print(0)