target = int(input()) 
n = int(input())
broken = [False] * 10
if n > 0:
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    broken[x] = True

def solution(target):
   
    if target == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while target > 0:
        if broken[target%10]:
            return 0
        l+=1
        target //= 10
    return l

ans = abs(target-100)
for i in range(0, 1000000+1):
    c = i
    l = solution(c)
    if l>0:
        press = abs(c-target)
        if l+press < ans:
            ans = l+press
print(ans)

# print(solution(5457, [6,7,8]))
# print(solution(500000, [0, 2, 3, 4, 6, 7, 8, 9]))
# print(solution(101, [0,1,2,3,4]))
# print(solution(target, brokens))
        