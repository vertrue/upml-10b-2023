n = int(input())

a=[]
for i in range(n):
    a.append(int(input()))

zeros = 0
for i in range(n):
    if a[i] == 0:
        zeros += 1 
print(zeros)
