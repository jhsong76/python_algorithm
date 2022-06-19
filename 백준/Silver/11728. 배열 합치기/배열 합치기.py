import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.read().split()))
b = list(map(int, sys.stdin.read().split()))

answer_list = a + b
answer = ' '.join(map(str, sorted(answer_list)))

print(answer)
