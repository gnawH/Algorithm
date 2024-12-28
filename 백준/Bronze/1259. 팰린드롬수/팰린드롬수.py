while(1):
    n = list(input())
    cnt = 0
    
    if n[0] == '0':
        break
    
    for i in range(len(n)):
        if n[i] == n[len(n)-1-i]:
            cnt += 1
    if cnt == len(n):
        print('yes')
    else:
        print('no')