n = int(input()) 
s = list(map(int, input().split()))
cnt = 0 
seat = []
for i in range(n):
    if s[i] in seat:         
        cnt += 1               
    else:                         
        seat.append(s[i])   
print(cnt)