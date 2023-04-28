def v2(n, a):
    # знаходження мінімуму
    min_el=a[0]
    for i in range(n):
        if a[i]<min_el:
            min_el=a[i]

    return min_el

