# -*- coding: utf-8 -*-

from math import *
import sys
import numpy as np
import matplotlib.pyplot as plt
from .draw import draw

MAX = sys.maxsize

# 计算两点距离
def caculateDistance(length, location):
    dist = np.zeros((length, length))
    result = []

    for begin in range(length):
        end = begin + 1
        while end < length:
            d = np.linalg.norm(location[begin] - location[end])
            dist[begin][end] = d
            dist[end][begin] = d
            result.append(d)
            end += 1

    # dist距离矩阵， result距离向量
    return dist, np.array(result)

def caculateDc(dist_vector, percent):
    position = int(len(dist_vector) * percent)
    sortedll = np.sort(dist_vector)
    return sortedll[position] #阈值

# 求点的局部密度(localDensity)
def localDensity(length, dist, dc):
    rho = np.zeros((length, 1))

    for begin in range(length):
        for end in range(length):
            rho[begin] += exp(-(dist[begin][end]/dc) ** 2)

    return rho

# 求样本点i的相对距离
def relativeDistance(length, dist, rho):
    delta = np.ones((length, 1)) * MAX
    maxDensity = np.max(rho)

    for begin in range(length):
        if rho[begin] < maxDensity:
            for end in range(length):
                if rho[end] > rho[begin]:
                    delta[begin] = min(delta[begin], dist[begin][end])
        else:
            delta[begin] = np.max(dist[begin])

    return delta

def nearestNeighbor(length, dist, rho, result, index):
    dd = MAX
    neighbor = -1
    for i in range(length):
        if dist[index, i] < dd and rho[index] < rho[i]:
            dd = dist[index, i]
            neighbor = i

    if result[neighbor] == -1:
        result[neighbor] = nearestNeighbor(length, dist, rho, result, neighbor)
    return result[neighbor]

def detectHalo(length, dist, rho, result, dc):
    pb = np.zeros(length)
    for begin in range(length):
        end = begin + 1
        while end < length:
            if result[begin] != result[end] and dist[begin][end] < dc:
                p_avg = (rho[begin] + rho[end]) / 2
                if p_avg > pb[begin]:
                    pb[begin] = p_avg
                if p_avg > pb[end]:
                    pb[end] = p_avg
            end += 1

    for begin in range(length):
        if rho[begin] < pb[begin]:
            result[begin] = -1
    return result

def DPC(location, percent, name):
    length = len(location)

    dist, dist_vector = caculateDistance(length, location)

    dc = caculateDc(dist_vector, percent)

    rho = localDensity(length, dist, dc)

    delta = relativeDistance(length, dist, rho)

    fig, ax = plt.subplots()
    plt.clf()
    plt.title(name + '  dc:' + str(float('%.6f' % percent)), size = 18)
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

        # 赋予每个点聚类类标
        for i in range(length):
            dist[i][i] = MAX

        for i in range(length):
            if result[i] == -1:
                result[i] = nearestNeighbor(length, dist, rho, result, i)

        result = detectHalo(length, dist, rho, result, dc)

        draw(result, location, name)


    cid = fig.canvas.mpl_connect('button_press_event', on_press)

    plt.savefig('result/' + name + '_decision.png', facecolor='white', edgecolor='none')
    plt.show()
