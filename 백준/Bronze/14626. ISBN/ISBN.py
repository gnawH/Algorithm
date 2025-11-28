ISBN = input()
weight = 1
broken_number = 0
total = 0

for number in ISBN:
    if number != '*':
        total += (int(number) * weight)
    else:
        broken_number_weight = weight

    if weight == 1:
        weight = 3
    elif weight == 3:
        weight = 1



while (total + (broken_number_weight * broken_number)) % 10:
    broken_number += 1

print(broken_number)