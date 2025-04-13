def solution(board, k):
    a = len(board)
    b = len(board[0])
    sum = 0
    for i in range(a):
        for j in range(b):
            if i + j <= k:
                sum += board[i][j]
    return sum