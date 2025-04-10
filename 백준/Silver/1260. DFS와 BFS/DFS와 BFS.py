def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

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
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

DFS(v)
print()

visited = [False] * (n+1)
BFS(v)
