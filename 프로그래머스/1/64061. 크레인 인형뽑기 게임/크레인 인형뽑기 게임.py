# 36분 소요
def solution(board, moves):
    # 1번째 접근법 (포기)
    '''
    1. 각 위치 별 배열 별도 저장
    [[1번째 위치 배열], [2번째 위치 배열], [], ..]
    
    2. (moves값 - 1) index 로 접근
    '''
    
    # 2번째 접근법 (Stack)
    '''
    1. board[:][(moves값 - 1)] 로 접근
    
    2. 값이 0이 아닐 경우 stack에 추가 & 값 0으로 변경
    
    3. stack[-1]과 값이 같을 경우, pop() & count += 2
    '''
    stack = []
    count = 0
    
    # moves 값 크레인 이동
    for i in moves:
        for j in range(len(board)):
            
            # 인형이 있을 경우
            if board[j][i-1] != 0:
                # 마지막 뽑은 인형과 같을 경우
                if len(stack) > 0 and stack[-1] == board[j][i-1]:
                    count += 2
                    stack.pop()
                # 마지막 뽑은 인형과 다를 경우
                else:
                    stack.append(board[j][i-1])
                # 뽑고 남은 자리 0 초기화
                board[j][i-1] = 0
                break
    return count
                