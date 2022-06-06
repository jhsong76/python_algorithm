n = int(input())
num = 0
m = n

while True:
    a = n // 10
    b = n % 10
    n = 10 * b + (a + b) % 10
    num += 1
    if n == m:
        break
print(num)