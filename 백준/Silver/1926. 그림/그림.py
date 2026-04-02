import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n, m, start: tuple[int, int], visited: list[list[int]], canvas: list[list[int]]) -> int:

    size = 1
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and canvas[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                size += 1

    return size


def solve(n: int, m: int, canvas: list[list[int]]) -> tuple[int, int]:
    paints_size = []
    visited = [[False] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if not visited[x][y] and canvas[x][y] == 1:
                size = bfs(n, m, (x, y), visited, canvas)
                paints_size.append(size)

    return (len(paints_size), max(paints_size) if paints_size else 0)


def main() -> None:
    n, m = map(int, sys_input().split())
    canvas = [list(map(int, sys_input().split())) for _ in range(n)]

    answer = solve(n, m, canvas)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()