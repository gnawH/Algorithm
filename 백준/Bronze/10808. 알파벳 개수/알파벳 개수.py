S = input()

alphabet = [0] * 26  # 97 98 99 100 101 102 103 ...  122
for c in S:
    alphabet[ord(c) % 97] += 1

print(*alphabet)