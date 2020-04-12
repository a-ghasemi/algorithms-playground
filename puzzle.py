def y(x):
    return 1 / 38 * (9 - 41 * x)


def z(x):
    return 1 / 38 * (21 - 45 * x)


def p(x, y, z, a, b, c):
    return x * a + y * b + z * c


cases = [
    (99,72,18),
    (45,27,21),
    (36,21,13),
]

cases2 = [
    (39, 18, 0),
    (36,21,13),
    (28, 0, 7),
]


for x in range(-50,10):
    print(f'{x},{y(x)},{z(x)}',end = ' | ')
    for (a,b,c) in cases:
        print('{},{},{}:{}'.format(a,b,c,p(x,y(x),z(x),a,b,c)), end = ' | ')
    print("")
