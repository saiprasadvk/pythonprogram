10. Find the key from the multi level dictionary - Should not convert as string i/o - x = {'a':{'b':{'c':{'d':1}}}} find_key - 'c' o/p - {'d':1} if find_key = 'd' o/p - 1

Ans::

x = {'a':{'b':{'c':{'d':1}}}}

print(x["a"]["b"]["c"])
print(x["a"]["b"]["c"]["d"])


D1 = {'a':{'b':{'c':{'d':1}}}}

def iterdict(d,key):
    if key in d:
        return d[key]
    else:
        for k,v in d.items():
            return iterdict(d[k],key)
            
iterdict(D1,'b')

O/P:

{'d': 1}
1
