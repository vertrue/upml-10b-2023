# розмір масиву
n=int(input())   
# створення масиву
a=[]
for i in range(n):
    el=int(input())
    a.append(el)
# знаходження мінімуму
min_el=a[0]
for i in range(n):
    if a[i]<min_el:
        min_el=a[i]
# виведення максимального елемента
print("Мінімальний елемент:", min_el)
