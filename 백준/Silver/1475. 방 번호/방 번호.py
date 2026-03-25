import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: str) -> int:
    number_list = [0] * 10    # 0 ~ 9

    for num in n:
        number_list[int(num)] += 1

    duplicated_cnt = number_list[6] + number_list[9]

    if duplicated_cnt % 2 == 0:
        number_list[6], number_list[9] = duplicated_cnt // 2, duplicated_cnt // 2
    else:
        number_list[6], number_list[9] = (duplicated_cnt // 2) + 1, (duplicated_cnt // 2) + 1

    return max(number_list)


def main() -> None:
    n = sys_input()
    answer = solve(n)
    print(answer)


if __name__ == "__main__":
    main()