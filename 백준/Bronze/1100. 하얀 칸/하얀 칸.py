data = []
for _ in range(8):
    data.append(list(map(str, list(input()))))
result = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if data[i][j] == 'F':
                result += 1
print(result)