A = [1, 2, 5, 1, 1, 2, 3, 5, 1]
X = 5

# A = [1, 2, 3, 5, 8, 13, 21, 34]
# X = 5
from itertools import combinations

def bin_search(B, n):
    l = 0
    r = length-1

    while l<r:
        m = (l+r)//2
        if n > B[m]:
            l = m+1
        elif n < B[m]:
            r = m-1
        else:
            return m

    return l

# import bisect 
# B = [1, 2, 5]
# length = len(B)

def solution2(A, X):
    cand = {}
    cnt = 0
    for i in A:
        if i not in cand and A.count(i) >= 2:
            cand[i] = A.count(i)
            if A.count(i) >= 4:
                possible = i ** 2

                if possible >= X:
                    cnt += 1

    length = len(cand.keys())
    B = sorted(cand.keys())
    for i in range(0,length//2 +1):
        mod = X // B[i]
        target = bin_search(B, mod)
        if i == target:
            cnt += length - (target + 1)
        else:
            cnt += length - target
    return cnt



def solution(A, X):
    cand = {}
    cnt = 0
    for i in A:
        if i not in cand and A.count(i) >= 2:
            cand[i] = A.count(i)
            if A.count(i) >= 4:
                possible = i ** 2

                if possible >= X:
                    cnt += 1

    for l in list(combinations(cand.keys(), 2)):
        possible = l[0] * l[1]

        if possible >= X:
            cnt += 1

    if cnt >= 1000000000:
        return -1
    else:
        return  cnt

A = sorted(A, reverse=True)
# print(A)

