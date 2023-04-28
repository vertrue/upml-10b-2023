#візьмемо функцію з іншого файлу
from f import v2
# розмір масиву
n=int(input())   
# створення масиву
a=[]
for i in range(n):
    el=int(input())
    a.append(el)

min_el = v2(n, a)
# виведення максимального елемента
print("Мінімальний елемент:", min_el)
