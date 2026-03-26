import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: list[int], x: int) -> int:
    a.sort()

    count = 0
    left = 0
    right = n-1

    while (left < right):
        combination = a[left] + a[right]
        if combination == x:
            count += 1
            left += 1
            right -= 1
        elif combination > x:
            right -= 1
        else:
            left += 1

    return count


def main() -> None:
    n = int(sys_input())    # 수열 개수
    a = list(map(int, sys_input().split()))    # 수열
    x = int(sys_input())    # 기준값

    answer = solve(n, a, x)
    print(answer)


if __name__ == "__main__":
    main()