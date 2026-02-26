import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    t = np.arange(1, n + 1)

    r = y / ppy
    discount = 1 / (1 + r) ** t

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] = cf[-1] + face

    pv = cf * discount
    price = np.sum(pv)

    t_years = t / ppy
    duration = np.sum(t_years * pv) / price

    return float(np.round(duration, 2))