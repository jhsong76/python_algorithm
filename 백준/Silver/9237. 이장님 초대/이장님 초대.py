n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

for i in range(n):
  data[i] = data[i] + i + 1

print(max(data) + 1)