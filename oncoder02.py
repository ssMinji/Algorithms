# goldValues = [2, 1, 4, 1, 2, 1, 8, 1]
# goldValues = [5, 2, 1, 4, 3, 1]
# goldValues = [1, 2, 1]
goldValues = [4239,4579,6980,4064,5943]

def solution(goldValues):
    totalGold = 0
    goldValues = [[x, i] for i, x in enumerate(goldValues)]

    idx = 0
    while True:
        if idx > len(goldValues):
            break

        groupIdx = list(filter(lambda x: goldValues[x][0] == 0, range(len(goldValues))))
        print(groupIdx)

        if len(groupIdx) == len(goldValues):
            return totalGold

        if len(groupIdx) < 2:
            curMax = max(goldValues)
            if idx % 2 == 0:
                totalGold += curMax[0]
            goldValues[curMax[1]][0] = 0
        else:
            for i in range(len(groupIdx)):
                if i == len(groupIdx) - 1:
                    curMax = max(goldValues[groupIdx[i]:] + goldValues[:groupIdx[0]])
                else:
                    curMax = max(goldValues[groupIdx[i]:groupIdx[i+1]])
                if idx%2 == 0:
                    print(curMax[0])
                    totalGold += curMax[0]

                goldValues[curMax[1]][0] = 0

        idx += 1 

    return totalGold

print(solution(goldValues))