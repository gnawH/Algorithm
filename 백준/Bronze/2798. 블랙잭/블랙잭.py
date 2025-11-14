from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

picks = combinations(cards, 3)
sum_cards = [sum(pick) for pick in list(picks)]
best = 0

if M in sum_cards:
    print(M)
else:
    for sum in sum_cards:
        if sum < M and best < sum:
            best = sum
    print(best)