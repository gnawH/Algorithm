def solution(order):
    # 아메리카노 : 4500원 (iceamericano, hotamericano, americano, anything)
    # 라떼 : 5000원 (icecafelatte, hotcafelatte, cafelatte)
    price = 0
    for i in order:
        if 'cafelatte' in i:
            price += 5000
        else:
            price += 4500
    return price