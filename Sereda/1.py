n = int(input())
a=[]
for i in range(n):
    el = int(input())
    a.append(el)
max_el = a[0]
for i in range(n):
    if a[i]>max_el:
        max_el=a[i]
print(max_el)