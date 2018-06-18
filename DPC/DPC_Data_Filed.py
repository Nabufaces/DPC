# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt
from DPC import DPC

START = 0
END = 20
numRange = 0.01

def DPC_Data_Filed(location, name, isDist = True):
    length = len(location)

    if isDist:
        dist = location
    else:
        dist, dist_vector = DPC.caculateDistance(length, location)

    X = np.arange(START, END, numRange)
    Y = np.zeros((len(X)))
    threshold_x = 0
    threshold_y = float('inf')

    for x_index, x in enumerate(X):
        if x == 0:
            Y[x_index] = float('inf')
            continue

        U = np.zeros(length)
        Z = 0

        for begin in range(length):
            for end in range(length):
                U[begin] += exp(-(dist[begin][end]/x) ** 2)
            Z += U[begin]

        for begin in range(length):
            temp = U[begin] / Z
            if temp > 0:
                Y[x_index] += temp * log(temp, 2)

        Y[x_index] = - Y[x_index]

        if Y[x_index] <= threshold_y:
            threshold_x = x
            threshold_y = Y[x_index]
        else:
            break
        print(Y[x_index], x)

    # plt.plot(X, Y)
    # plt.savefig('result/' + name + '.png', facecolor='white', edgecolor='none')
    # plt.show()
    return 3 * threshold_x / sqrt(2) / len(dist)