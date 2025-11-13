def solution(answers):
    top_scores = []
    # 점수
    score1, score2, score3 = 0, 0, 0
    # 규칙
    first = [5 if i % 5 == 0 else i % 5 for i in range(1, len(answers)+1)]
    # 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    # 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10)
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    
    for index, answer in enumerate(answers):
        if answer == first[index]:
            score1 += 1
        if answer == second[index]:
            score2 += 1
        if answer == third[index]:
            score3 += 1
            
    scores = [score1, score2, score3]
    for idx, score in enumerate(scores):
        if score == max(scores):
            top_scores.append(idx+1)
    return top_scores