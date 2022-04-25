a = int(input())
b = input()

for n in range(len(b), 0, -1):
    result = a * int(b[n-1])
    print(result)
    
print(a * int(b))