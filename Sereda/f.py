def v1(n, a):
    max_el = a[0]
    for i in range(n):
        if a[i]>max_el:
            max_el=a[i]
    return max_el