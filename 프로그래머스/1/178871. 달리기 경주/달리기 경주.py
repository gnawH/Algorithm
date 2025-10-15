def solution(players, callings):
    
    players_rank = {player:idx for idx, player in enumerate(players, 0)}
    
    for call in callings:
        idx = players_rank[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        players_rank[players[idx]] += 1 
        players_rank[players[idx-1]] -= 1 
    
    return players