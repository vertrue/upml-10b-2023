n = int(input())

a = []
for i in range(n):
    el = int(input())
    a.append(el)
    
flag = False
for i in range(n):
    if a[i] == 0:
        flag = True
        
if flag:
    print("є")
else:
    print("нема")
