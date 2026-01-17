computers = int(input())    # 컴퓨터의 수 (0 ~ 100)
pairs = int(input())    # 직접 연결되어있는 컴퓨터 쌍의 수

networks = [[] for _ in range(computers + 1)]   # 각 컴퓨터 별 연결된 기기 저장
visited = [False for _ in range(computers + 1)]
count = -1

for pair in range(pairs):
    A, B = map(int, input().split())
    networks[A].append(B)
    networks[B].append(A)

def dfs(x):
    global count
    visited[x] = True
    count += 1
    for connected_computer in networks[x]:
        if visited[connected_computer]:
            continue
        dfs(connected_computer)

dfs(1)
print(count)