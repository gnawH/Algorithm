import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: list[int], x: int) -> int:
    tmp_space = set()
    count = 0

    for a_num in a:
        if a_num in tmp_space:
            tmp_space.remove(a_num)
            count += 1
        else:
            tmp_space.add(x - a_num)

    return count


def main() -> None:
    n = int(sys_input())    # 수열 개수
    a = list(map(int, sys_input().split()))    # 수열
    x = int(sys_input())    # 기준값

    answer = solve(n, a, x)
    print(answer)


if __name__ == "__main__":
    main()