from math import *
import sympy
import matplotlib.pyplot as plt
import numpy as np
from DPC import DPC
import sys

MAX = 10
sys_MAX = sys.maxsize

def DPC_Data_Filed(location, name):
    length = len(location)

    dist, dist_vector = DPC.caculateDistance(length, location)

    X = np.arange(0.1, MAX, 0.1)
    Z = np.zeros((len(X)))
    Y = np.zeros((len(X)))

    # for x_index, x in enumerate(X):
    #
    #     z = 0
    #     for begin in range(length):
    #         u = 0
    #         for end in range(length):
    #             u += exp((dist[begin][end]/x) ** 2)
    #         z += u
    #
    #
    # def localDensity():
    #
    #     for x_index, x in enumerate(X):
    #
    #     u = 0
    #     for begin in range(length):
    #
    #         if begin != index:
    #             try:
    #                 result += exp((dist[index][begin]/x) ** 2)
    #             except OverflowError:
    #                 result = float('inf')
    #                 break
    #
    #     return result
    #
    #     for i in range(length):
    #         Z[x_index] += localDensity(length, dist, i, x)
    #
    #     for i in range(length):
    #         temp = (localDensity(length, dist, i, x)) / Z[x_index]
    #         if isnan(temp):
    #             Y[x_index] = 0
    #         elif temp == 0.0:
    #             Y[x_index] = float('inf')
    #         else:
    #             Y[x_index] += temp * log(temp, 2)
    #
    #     Y[x_index] = - Y[x_index]
    #
    # print(Y)
    # plt.plot(X, Y)
    #
    # plt.show()