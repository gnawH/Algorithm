string = input()
count = 0

for char in string: # A : 65
    num = ord(char)
    if num <= 67 :  # A ~ C
        count += 3
    elif num <= 70 :  # D ~ F
        count += 4
    elif num <= 73 :  # G ~ I
        count += 5
    elif num <= 76 :  # J ~ L
        count += 6
    elif num <= 79 :  # M ~ O
        count += 7
    elif num <= 83 :  # P ~ S
        count += 8
    elif num <= 86 :  # T ~ V
        count += 9
    elif num <= 90 :  # W ~ Z
        count += 10
    else:
        count += 11
print(count)