def v10(n, a):
    flag = False
    for i in range(n):
        if a[i] == 0:
            flag = True
    return flag
