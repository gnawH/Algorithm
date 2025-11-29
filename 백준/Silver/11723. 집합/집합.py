import sys

def add(S, number):
    S.add(int(number))

def remove(S, number):
    if check(S, int(number)) == 1:
        S.discard(int(number))

def check(S, number):
    if len(S) != 0:
        if int(number) in S:
            return 1
        else:
            return 0
    else:
        return 0

T = int(sys.stdin.readline())
S = set()

for test_case in range(T):
    order_info = sys.stdin.readline().strip()
    if order_info == 'all':
        S = set(num for num in range(1, 21))
        continue
    elif order_info == 'empty':
        S = set()
        continue
    else:
        order, number = order_info.split()

    if order == 'add':
        add(S, number)
    elif order == 'remove':
        remove(S, number)
    elif order == 'check':
        print(check(S, number))
    elif order == 'toggle':
        if check(S, number) == 1:
            remove(S, number)
        elif check(S, number) == 0:
            add(S, number)