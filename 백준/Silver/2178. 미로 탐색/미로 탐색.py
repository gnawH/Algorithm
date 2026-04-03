import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[int]]) -> int:
    dist = [[-1] * m for _ in range(n)]

    queue = deque([(0, 0)])
    dist[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == 1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    return dist[n-1][m-1]


def solve(n: int, m: int, board: list[list[int]]) -> int:
    min_cnt = bfs(n, m, board)
    return min_cnt + 1


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [[int(i) for i in sys_input()] for _ in range(n)]

    answer = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()