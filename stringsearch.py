def kmp_table(W: str):
    pos = 1
    cnd = 0
    T = [-1]

    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1

    T[pos] = cnd

    return T


def kmp_search(S: str, W: str):
    j = 0
    k = 0
    T = kmp_table(W)

    nP = 0

    while i < len(S):
        if W[k] == S[j]:
            j += 1
            k += 1
            if k == len(W):
                P[nP] = j - k
                nP += 1
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
