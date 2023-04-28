from f import v10

n = int(input())
a = []
for i in range(n):
    el = int(input())
    a.append(el)
    
if v10(n, a):
    print("є")
else:
    print("нема")
