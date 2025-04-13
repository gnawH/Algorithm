def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in range(row):
            arr[i].extend([0] *(row - col))
    elif col > row:
        for i in range(col-row):
            arr.append([0]*col)
    return arr