import sys

N, M = map(int, sys.stdin.readline().split())
password_dict = {}

for _ in range(N):
    domain, password = sys.stdin.readline().split()
    password_dict[domain] = password

for _ in range(M):
    check_domain = sys.stdin.readline().strip()
    print(password_dict[check_domain])