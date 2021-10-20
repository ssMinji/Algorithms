n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

ans = 0
def solution(day, income):
    global ans
    if day == n:
        ans = max(ans, income)
        return 
    
    if day > n:
        return 
    
    solution(day+t[day], income+p[day])
    solution(day+1, income)
    
solution(0, 0)
print(ans)