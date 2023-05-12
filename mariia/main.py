from f import v11

n = int(input())
a = []
for i in range(n):
    el = int(input())
    a.append(el)

if v11(n, a) >= 3:
    print("є")
else:
    print("нема")
