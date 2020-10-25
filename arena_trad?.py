import random
import numpy as np


if __name__ == "__main__":

    n = 1000
    data = np.random.binomial(n=1, p=0.55, size=n)
    res1 = 0
    res2 = 0
    i=0

    while i < n-2:
        if data[i] == data[i + 1]:
            res2 += data[i]
            res2 += data[i+1]
            res1 += data[i]
            res1 += data[i + 1]
            i=i+2

        if data[i] != data[i + 1]:
            res2 += data[i + 2] + data[i + 2]

            res1 += data[i]
            res1 += data[i + 1]
            res1 += data[i + 2]
            i = i + 3

    print(res1, res2)

    #
    # res = 0
    # m = 10
    # for meta in range(m):
    #     n = 10
    #     score_a = 0
    #     score_b = 0
    #
    #     for i in range(n):
    #         g3 = 0
    #         g1 = random.randint(0, 1)
    #         g2 = random.randint(0, 1)
    #         g3 = random.randint(0, 1)
    #
    #         if g1 != g2:
    #             score_a += 2*g3
    #         else:
    #             score_a += g1+g2
    #         score_b += g1+g2
    #
    #     if score_a > score_b:
    #         res += 1
    #
    #
    # print(res/m)


