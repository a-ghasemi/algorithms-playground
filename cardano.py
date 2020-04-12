t1 = Timer(True)
a = sp.Symbol("a")
# d = sp.Symbol("d")

n = 8
solv = []
for b in range(0,n+1):
    for c in range(0,n-b+1):
        # print('* ',b,c,' *')
        s = sp.solve(8 * a ** 3 + 15 * a ** 2 + 6 * a - 27 * c * b ** 2 - 1, a)
        # print(s,b,c)
        for x in s:
            print(x, b, c)
            if sp.Q.is_integer(x) and x + b + c <= n:
                solv.append((x, b, c))
t1.stop()
print(solv, len(solv))
t1.show()
