n, m = map(int, input().split())
card = list(map(int, input().split()))
result = []

for i in range(0, len(card)):
    for j in range(1, len(card)):
        for k in range(0, len(card)):
            if card[i] != card[j] and card[j] != card[k] and card[i] != card[k]:
                if card[i]+card[j]+card[k] <= m:
                    result.append(card[i]+card[j]+card[k])
            
print(max(result))