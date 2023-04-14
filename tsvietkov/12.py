n = int(input())
a=[]
for i in range(n):
    l = int(input())
    a.append(l)

b = false

for i in range(n):
    if a[i] == 0:
        b = true

if b == true:
    print("yes")
else: 
    print("no")