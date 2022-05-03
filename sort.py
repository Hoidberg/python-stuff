delta = [None] * 4

def initArgs(func):
    @wraps(func)
    def functionWrapper(*args, **kw):

        argNames, defaults = inspect.getargspec(func)[::3]

        for k in kw:
            for i in argNames:
                if k != i and ('_' + k) == i:
                    kw['_' + k] = kw[k]
                    del kw[k]

        argValues = list(args) + [
            kw[y] if y in kw else defaults[x]
            for x,y in enumerate(argNames[len(args):])
        ]

        oldGlobals = {}
        for n,v in zip(argNames, argValues):

            try:
                oldGlobals[n] = globals()[n]
            except:
                oldGlobals[n] = None

            if not n.startswith('_') or n in kw:
                globals()[n] = v
            else:
                globals()[n] = kw[n] = eval(v)

        for o,v in oldGlobals.items(): globals()[o] = v

        return func(*args, **kw)

    return functionWrapper

def make_delta(N: int):
    power = 1
    i = 0

    while True:
        half = power
        power <<= 1
        delta[i] = int((N + half) / power)
        if delta[i] == 0:
            break
        i += 1

def binarysearch(el: int, a: list, k: int):
    make_delta(k)
    i = delta[0] - 1
    d = 0

    while True:
        if el == a[i]:
            return i
        elif delta[d] == 0:
            return -1
        else:
            if el < a[i]:
                d += 1
                i -= delta[d]
            else:
                d += 1
                i += delta[d]
            if i < 0:
                return -1

rand = [1, 3, 5, 8, 9, 11]
print(binarysearch(9, rand, 5))
