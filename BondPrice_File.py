import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    t = np.arange(1, n + 1)

    r = y / ppy
    discount = 1 / (1 + r) ** t

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] = cf[-1] + face

    price = np.sum(cf * discount)
    return float(price)