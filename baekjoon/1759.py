def solution(n, alpha, password, idx):
    if len(password) == n:
        if check(password):
            print(password)
        return 

    if idx >= len(alpha):
        return 
    
    solution(n, alpha, password+alpha[idx], idx+1)
    solution(n, alpha, password, idx+1)

def check(password):
    ja = 0
    mo = 0
    for p in password:
        if p in 'aeoui':
            mo+=1
        else:
            ja+=1
    
    return  mo >= 1 and ja >= 2

n, m = map(int, input().split())
a = input().split()
a.sort()
solution(n, a, '', 0)
    