
text = "ONE TWO THREE FOUR FIVE"
width = 150
height = 60

import math
def solution(text, width, height):
    l_word = text.split(' ')
    len_word = [len(word) for word in l_word] # 3 3 5 4 4
    result = -1
    f_size = 7
    while f_size > 0:
        chk = True
        for i in range(len(l_word)): # 5
            wb = i+1 # 첫째줄 단어 개수 
            hb = math.ceil(len(l_word) / wb) # 줄개수 

            chk_word = []

            for j in range(hb):
                chk_word.append(sum(len_word[j*wb:(j+1)*wb]))
            w = max(chk_word) + i
            cw = (f_size + 2) * w
            ch = 2 * f_size * hb
            if cw <= width and ch <= height:
                result = f_size
                f_size += 1
                chk = False
                break
            
        if chk:
            f_size = -1
    return result

# print(solution(text, width, height))
lenList = [3, 3, 5, 4, 4]


# print(result)

ans = []

# def splitList(ls):
#     if len(ls) == 1:
#         ans.append(ls) 

#     for i in range(1, len(ls)+1):
#         a1 = sum(ls[:i])
#         ans.append(a1)
#         a2 = ls[i:]
#         splitList(a2)

# print(splitList(lenList))
# print(ans)

idxList = [i for i in range(len(lenList))]
print(idxList)
from itertools import combinations
print(list(combinations(idxList, 2)))