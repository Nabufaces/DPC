from math import *
import numpy as np
from DPC import DPC

MAX = 0.1
numRange = 0.001

def DPC_Data_Filed(location):
    length = len(location)

    dist, dist_vector = DPC.caculateDistance(length, location)

    X = np.arange(0, MAX, numRange)
    Y = np.zeros((len(X)))

    for x_index, x in enumerate(X):
        if x == 0:
            Y[x_index] = float('inf')
            continue

        U = np.zeros(length)
        Z = 0

        for begin in range(length):
            for end in range(length):
                if begin != end:
                    U[begin] += exp(-(dist[begin][end]/x) ** 2)
            Z += U[begin]

        if Z == 0:
            Y[x_index] = float('inf')
            continue

        for begin in range(length):
            temp = U[begin] / Z
            if temp > 0:
                Y[x_index] += temp * log(temp, e)

        Y[x_index] = - Y[x_index]

    minY = np.min(Y)
    threshold = 0
    num = 0
    for i in range(len(Y)):
        if minY == Y[i]:
            threshold += X[i]
            num += 1
    return 3 * (threshold / num) / sqrt(2)