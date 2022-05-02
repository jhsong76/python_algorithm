import sys

read = sys.stdin.readline

n = int(read())
data = list(map(int, read().split()))

m = int(read())
weight = list(map(int, read().split()))


data.sort(reverse=True)
weight.sort(reverse=True)

if data[0] < weight[0]:
    print(-1)
    sys.exit()
else:  
    time = 0
    while len(weight) > 0:
        for i in data:
            for j in range(len(weight)):
                if i >= weight[j]:
                    weight.remove(weight[j])
                    break
        time += 1
    print(time)