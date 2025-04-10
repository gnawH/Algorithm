def solution(rank, attendance):
    tmp = []
    # (rank, index)
    for i in range(len(rank)):
        if attendance[i]:
            tmp.append((rank[i], i))
            
    s_tmp = sorted(tmp)
    return (s_tmp[0][1] * 10000 + s_tmp[1][1] * 100 + s_tmp[2][1] * 1)
        
        