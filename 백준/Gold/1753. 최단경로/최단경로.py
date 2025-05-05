import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = [[] for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def daextra(start):
    distance = [float("inf")] * (V+1)
    distance[start] = 0
    que = []

    heapq.heappush(que, (distance[start], start))

    while que:
        node_distance, node = heapq.heappop(que)

        if distance[node] < node_distance:
            continue

        for nod, dis in graph[node]:
            total_distance = distance[node] + dis
            
            if total_distance < distance[nod]:
                distance[nod] = total_distance
                heapq.heappush(que, (total_distance, nod))

    return distance

result = daextra(k)

for i in range(1, len(result)):
    print("INF" if result[i] == float("inf") else result[i])