def solution(participant, completion):
    hash = {}
    for name in participant:
        hash[name] = hash.get(name, 0) + 1
    for name in completion:
        if hash[name] > 0:
            hash[name] -= 1
    for k, v in hash.items():
        if v > 0:
            return k