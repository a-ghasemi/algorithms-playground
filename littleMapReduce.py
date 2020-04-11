# peoblem is converting [5,5,5,7,7,3,4,4,9,9,2,1,4,3,5,5,4,3,3,4,6,7] into ['5:3', '7:2', '3', '4:2', '9:2', '2', '1', '4', '3', '5:2', '4', '3:2', '4', '6', '7']
C = [5,5,5,7,7,3,4,4,9,9,2,1,4,3,5,5,4,3,3,4,6,7]

def pack(arr):
    if len(arr) == 0: return []
    def append(a):
        nonlocal l,c
        l.append((str(a), '{}:{}'.format(a, c))[c > 1])

    l = list()

    p = arr[0]
    c = 1
    for i in arr[1:]:
        if p == i: c += 1
        else:
            append(p)
            p = i
            c = 1
    append(i)
    return l

print(pack(C))