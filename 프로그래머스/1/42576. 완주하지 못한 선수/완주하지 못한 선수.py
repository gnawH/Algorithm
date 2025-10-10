def solution(participant, completion):

    player = {}
    
    for name in participant:
        player[name] = player.get(name, 0) + 1
        
    for name in completion:
        if player[name] > 0:
            player[name] -= 1
            
    for k, v in player.items():
        if v > 0:
            return k