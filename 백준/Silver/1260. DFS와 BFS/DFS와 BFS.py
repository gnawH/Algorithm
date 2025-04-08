# 깊이 우선 탐색
def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

# 너비 우선 탐색
def BFS(v):
    queue = [v]
    visited[v] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]    # 연결된 노드
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

DFS(v)

# 방문 초기화
visited = [False] * (n+1)
print()

BFS(v)