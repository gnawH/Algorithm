N = int(input())

for num in range(1, N+1):
    count = 0
    str_num = str(num)
    for i in str_num:
        if i in ['3', '6', '9']:
            count += 1
    if count == 0:
        print(num, end=' ')
    else:
        print('-'*count, end=' ')