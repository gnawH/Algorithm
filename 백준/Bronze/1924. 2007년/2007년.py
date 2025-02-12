x, y = map(int, input().split())
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

if x != 1:
    for i in range(1, x):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            y += 31
            
        elif i in [4, 6, 9, 11]:
            y += 30
    
        elif i in [2]:
            y += 28

print(day[y % 7])