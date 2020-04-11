n = 12

def is_lucky(a):
   if str(a).find('4') >= 0: return False
   if str(a).find('13') >= 0: return False
   return True

def what_is_lucky_of(n):
    ret = 1
    for i in range(1,n):
        ret += 1
        while not is_lucky(ret): ret+=1
    return ret

i = 123
print(i,what_is_lucky_of(i))