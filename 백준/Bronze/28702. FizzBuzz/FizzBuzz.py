list = []

def fuzzbuzz(tmp):
    if tmp % 3 == 0 and tmp % 5 == 0:
        print("FizzBuzz")
    elif tmp % 3 == 0 and tmp % 5 != 0:
        print("Fizz")
    elif tmp % 3 != 0 and tmp % 5 == 0:
        print("Buzz")
    else :
        print(tmp)

for i in range(3):
    list.append(input())

for i in list:
    try:
        tmp = int(i)
        if list.index(i) == 0:
            tmp+=3
        elif list.index(i) == 1:
            tmp+=2
        else :
            tmp+=1
        fuzzbuzz(tmp)
        tmp = 0
        if tmp == 0:
            break

    except:
        continue

