import helpers

M1 = 3
M2 = 5
N = 1000


res = set()
t1 = helpers.Timer(True)
for i in range((N // M1)+1):
    for j in range((N // M2)+1):
        S = (i * M1,1)[i == 0] * (j * M2,1)[j == 0]
        if S > 1 and S < N:
            res.add(S)
t1.stop()
t1.show()

sumi = 0
for i in res:
    sumi += i

print(res)
print(sumi)
