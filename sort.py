delta = [None] * 4

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

def binarysearch(el: int, a: list, k=None):
    k = k if k is not None else len(a)
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
print(binarysearch(11, rand))
