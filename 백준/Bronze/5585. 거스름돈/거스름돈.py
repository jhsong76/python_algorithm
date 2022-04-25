import sys
input = sys.stdin.readline

N = int(input())
rest = 1000 - N
mon = [500, 100, 50, 10, 5, 1]
result = 0

for money in mon:
    if rest == 0:
        break

    result += rest // money
    rest %= money

print(result)