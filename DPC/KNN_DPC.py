# -*- coding: utf-8 -*-

from math import *
from queue import Queue
import numpy as np
import matplotlib.pyplot as plt
from DPC import DPC

def localDensity(length, dist):
    rho = np.zeros((length, 1))

    for begin in range(length):
        for end in range(length):
            if begin != end:
                rho[begin] += exp(-dist[begin][end])

    return rho

def k_dist(length, dist):
    k_dist_arr = np.zeros((length, 1))

    for begin in range(length):
        k_dist_arr[begin] = np.max(dist[begin])

    return k_dist_arr

def outlier(length, k_dist_arr, threshold):
    # 0为非离群点，1为离群点
    outlier_arr = np.zeros((length, 1))

    for begin in range(length):
        if k_dist_arr[begin] > threshold:
            outlier_arr[begin] = 1

    return outlier_arr

def strategyOne(result):
    return;

def KNN_DPC(location, name):
    length = len(location)

    dist, dist_vector = DPC.caculateDistance(length, location)

    rho = localDensity(length, dist)

    delta = DPC.relativeDistance(length, dist, rho)

    fig, ax = plt.subplots()
    plt.clf()
    plt.title(name, size = 18)
    plt.plot(rho, delta, '.', color = 'k')
    plt.xlabel('rho'), plt.ylabel('delta')

    cid = 0

    # 决策图结果
    def on_press(event):
        fig.canvas.mpl_disconnect(cid)

        thRho = event.xdata
        thDel = event.ydata
        print("position:", thRho, thDel)

        #确定聚类中心
        result = np.ones(length, dtype = np.int) * (-1)
        center = 0

        for i in range(length):
            if rho[i] > thRho and delta[i] > thDel:
                result[i] = center
                center = center + 1

        k_dist_arr = k_dist(length, dist)

        threshold = np.average(k_dist_arr)

        outlier_arr = outlier(length, k_dist_arr, threshold)

        for i in range(length):
            if result[i] == -1 and outlier_arr[i] == 0:
                strategyOne()

    cid = fig.canvas.mpl_connect('button_press_event', on_press)

    plt.savefig('result/' + name + '_decision.png', facecolor='white', edgecolor='none')
    plt.show()
