def solution(relation):
    answer_list = []
    colNum = len(relation[0])
    rowNum = len(relation)

    for i in range(1, 1 << colNum):
        tmp_set = set()
        for j in range(0, rowNum):
            tmp = ''
            for k in range(0, colNum):
                if (i & (1<<k)): # 해당 부분조합에 포합된 컬럼 추출
                    tmp += relation[j][k]

            tmp_set.add(tmp)

        if len(tmp_set) == rowNum: # 유일성 검증
            is_unique = True
            for answer in answer_list:
                if (answer & i) == answer: # 최소성 검증
                    is_unique = False
                    break

            if is_unique:
                answer_list.append(i)

    return len(answer_list)

relation = [["100","ryan","music","2"], ["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation)) # return 2