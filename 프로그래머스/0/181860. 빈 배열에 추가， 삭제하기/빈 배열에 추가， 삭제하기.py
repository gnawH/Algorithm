def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i] == True:
            X.extend([arr[i]] * arr[i] * 2)
        else:
            for i in range(arr[i]):
                X.pop()
    return X