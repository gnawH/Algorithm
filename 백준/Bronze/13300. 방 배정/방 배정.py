import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, students: list[str]) -> int:
    rooms = {}
    count = 0

    for student in students:
        if rooms.get(student):
            rooms[student] += 1
        else:
            rooms[student] = 1

    for v in rooms.values():
        if v % k == 0:
            count += v // k
        else:
            count += (v // k) + 1

    return count


def main() -> None:
    n, k = map(int, sys_input().split())
    students = [sys_input() for _ in range(n)]

    answer = solve(k, students)
    print(answer)


if __name__ == "__main__":
    main()