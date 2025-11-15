N, M = map(int, input().split())
board = []

for i in range(N):
    tmp = []
    line = input()
    for j in range(M):
        tmp += line[j]
    board.append(tmp)

test = {True: 'W', False: 'B'}

result = []

for height in range(N-7):
    for width in range(M-7):
        count1 = 0
        count2 = 0
        if board[height][width] == 'W':
            switch = True
        elif board[height][width] == 'B':
            switch = False
        for i in range(height, height+8): # 10 9 8
            switch = not switch
            for j in range(width, width+8):
                if board[i][j] != test[switch]:
                    count1 += 1
                elif board[i][j] != test[not switch]:
                    count2 += 1
                switch = not switch
        result.append(count1)
        result.append(count2)
print(min(result))