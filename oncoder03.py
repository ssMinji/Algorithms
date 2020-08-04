text = "ONE TWO THREE FOUR FIVE"
width = 150
height = 40

textList = text.split(' ')

textlen = [len(t) for t in textList] # [3,3,5,4,4]


# hegiht = (numLine) * 2 * font
# width = (numWord) * (2+font)


idxList = [1, 2, 3, 4]

from itertools import combinations

split = 1
font = 7
while split <= len(textlen) - 1:
    result = []
    cand = list(combinations(idxList, split))
    flag = True
    print(cand, font)
    for ca in cand:
        subset = []
        for i in range(len(ca)+1):
            if i == 0:
                ws = ca[i] - 1
                subset.append(sum(textlen[:ca[i]]) + ws)
                
            elif 0 < i < len(ca):
                ws = ca[i] - ca[i-1] - 1
                subset.append(sum(textlen[ca[i-1]:ca[i]]) + ws)

            elif i == len(ca):
                ws = len(textlen) - ca[i-1] - 1
                subset.append(sum(textlen[ca[i-1]:]) + ws)
        w = max(subset)
        curWidth = w * (font + 2)
        curHeight = len(subset) * 2 * font
        if curWidth <= width and curHeight <= height:
            print('a', font)
            answer = font 
            font += 1
            flag = False
            break
    split += 1

print(answer)
