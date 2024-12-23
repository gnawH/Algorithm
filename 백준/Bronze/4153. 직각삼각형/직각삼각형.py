while(1):
    a = []
    try:
        r = list(map(int, input().split()))
        for i in r:
            a.append(i**2)
        m = max(a)
        a.remove(max(a))
        if m == 0:
            break
        elif m == sum(a):
            print('right')
        else:
            print('wrong')
    except:
        break
        