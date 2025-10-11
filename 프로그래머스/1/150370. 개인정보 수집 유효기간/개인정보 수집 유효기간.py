from typing import Dict

def solution(today, terms, privacies):
    # today 정수 변환(기준)
    today_num = today2num(today)
    # 약관 만료기한 정의
    term2month = create_terms2month(terms)
    # 인덱스 생성 및 약관 만료기한 계산 및 정수 변환
    answer = []
    for index, privacy in enumerate(privacies,1):
        date, term = privacy.split()
        result = today2num(date) + (term2month[term]*28)
        if result <= today_num:
            answer.append(index)
    return answer

def today2num(today) -> int:
    year, month, day = today.split('.')
    year = int(year)
    month = int(month)
    day = int(day)
    return 28*(12*year + month) + day

def create_terms2month(terms) -> Dict[str, int]:
    term2month = {}
    for term in terms:
        term, month = term.split()
        term2month[term] = int(month)
    return term2month
    