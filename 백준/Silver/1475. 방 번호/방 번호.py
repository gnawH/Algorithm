import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(N: str) -> int:
    number_set = [0] * 10

    for num in N:
        number_set[int(num)] += 1

    duplicated_cnt = number_set[6] + number_set[9]

    if (duplicated_cnt) % 2 == 0:
        number_set[6], number_set[9] = duplicated_cnt//2, duplicated_cnt//2
    else:
        number_set[6], number_set[9] = (duplicated_cnt//2)+1, (duplicated_cnt//2)+1

    return max(number_set)


def main() -> None:
    N = sys_input()
    answer = solve(N)
    print(answer)


if __name__ == "__main__":
    main()