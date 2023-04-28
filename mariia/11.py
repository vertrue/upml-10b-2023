n = int(input())

a = []
for i in range(n):
    el = int(input())
    a.append(el)

c = 0
for i in range(n):
    if a[i] == 0:
        c += 1

if c >= 3:
    print ("є")
else:
    print ("нема")
