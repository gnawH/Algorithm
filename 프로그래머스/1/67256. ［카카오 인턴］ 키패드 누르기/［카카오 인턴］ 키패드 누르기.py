def distance(left_now, right_now, i, center):
    left_dis = abs(left_now[0]-center.index(i)) + abs(left_now[1]-1)
    right_dis = abs(right_now[0]-center.index(i)) + abs(right_now[1]-1)
    return left_dis, right_dis
    

def solution(numbers, hand):
    left = [1, 4, 7]
    center = [2, 5, 8, 0]
    right = [3, 6, 9]
    result = ''
    
    left_now = [3, 0]
    right_now = [3, 2]
    
    for i in numbers:
        if i in left:
            result += 'L'
            left_now = [left.index(i), 0]
        elif i in right:
            result += 'R'
            right_now = [right.index(i), 2]
        else:
            left_dis, right_dis = distance(left_now, right_now, i, center)
            if left_dis < right_dis:
                result += 'L'
                left_now = [center.index(i), 1]
            elif left_dis > right_dis:
                result += 'R'
                right_now = [center.index(i), 1]
            else:
                if hand == 'right':
                    result += 'R'
                    right_now = [center.index(i), 1]
                else:
                    result += 'L'
                    left_now = [center.index(i), 1]
    return result
    
    
    