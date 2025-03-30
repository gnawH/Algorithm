def solution(arr):
    result = 0
    while True:
        sign = False
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
                sign = True
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                sign = True
        if sign == False:
            return result
        else:
            result += 1
    