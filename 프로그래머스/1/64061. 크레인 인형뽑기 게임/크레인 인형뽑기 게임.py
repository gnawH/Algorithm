def solution(board, moves):
    # 1~5번째 각각 위치 인형 별도의 배열로 저장
    # [0, 0, 0, 4, 3], [0, 0, 2, 2, 5], ...
    
    # moves에 따라 pop(0)
    tmp = []
    cnt = 0
    # 크레인 작동
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(tmp) > 0 and tmp[-1] == board[j][i-1]:
                    cnt += 2
                    tmp.pop()
                else:
                    tmp.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return cnt
                