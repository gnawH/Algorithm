def solution(phone_book):
    phone_book.sort()
    
    phone_book_dict = {}
    for number in phone_book:
        phone_book_dict[number] = 1
        
    for number in phone_book:
        tmp = ''
        for num in number:
            tmp += num
            if tmp in phone_book_dict and tmp != number:
                return False
    return True