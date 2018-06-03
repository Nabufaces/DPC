# -*- coding: utf-8 -*-

from math import *
from queue import Queue
import heapq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from DPC import DPC
from DPC import draw

def cal_k_arr(length, dist, K):
    k_arr = np.zeros((length, K))
    k_arr_index = np.zeros((length, K))

    for begin in range(length):
        k_arr_index[begin] = list(map(dist[begin].tolist().index, heapq.nsmallest(K + 1, dist[begin])))[1:]

        for i in range(K):
            k_arr[begin][i] = dist[begin][k_arr_index[begin][i]]

    return k_arr, k_arr_index

def localDensity(length, k_arr, K):
    rho = np.zeros((length, 1))

    for begin in range(length):
        for end in range(K):
            rho[begin] += exp(-k_arr[begin][end])

    return rho

def k_dist(length, k_arr):
    k_dist_arr = np.zeros((length, 1))

    for begin in range(length):
        k_dist_arr[begin] = np.max(k_arr[begin])

    return k_dist_arr

def outlier(length, k_dist_arr, threshold):
    # 0为非离群点，1为离群点
    outlier_arr = np.zeros((length, 1))

    for begin in range(length):
        if k_dist_arr[begin] > threshold:
            outlier_arr[begin] = 1

    return outlier_arr

def strategyOne(k_arr_index, outlier_arr, dist, result, result_visited, K):
    flag = True
    for key in result_visited:
        if result_visited[key] == 0:
            result_visited[key] = 1
            flag = False
            break
    if flag:
        return

    queue = Queue()
    for begin in range(K):
        i = int(k_arr_index[key][begin])
        result[i] = result[int(key)]
        queue.put(i)

    while not queue.empty():
        q = queue.get()
        for begin in range(K):
            r = int(k_arr_index[q][begin])
            dist_rj = np.zeros(K)
            for j in range(K):
                dist_rj[j] = dist[r][k_arr_index[r][j]]

            if result[r] == -1 and outlier_arr[r] == 0 and dist[q][r] <= np.mean(dist_rj):
                result[r] = result[q]
                queue.put(r)

    strategyOne(k_arr_index, outlier_arr, dist, result, result_visited, K)

def strategyTwo(k_arr_index, result, length, K, center):
    Nc = []
    Nk = []
    N_index = []
    for begin in range(length):
        if result[begin] == -1:
            count = np.zeros(center + 1)
            for i in range(K):
                c = result[k_arr_index[begin][i]]
                if c != -1:
                    count[c] += 1
            Nc.append(count)
            Nk.append(np.max(count))
            N_index.append(begin)

    Vmax = np.max(Nk)

    # for begin in range(len(Nk)):
    #     if Nk[begin] == Vmax:
    #         if Nk[begin] == K:
    #
    #         elif Nk[begin] > 0 and Nk[begin] < K:



def KNN_DPC(location, name):
    length = len(location)

    dist, dist_vector = DPC.caculateDistance(length, location)

    K = int(input("输入K: "))

    k_arr, k_arr_index = cal_k_arr(length, dist, K)

    rho = localDensity(length, k_arr, K)

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
        result_visited = {}

        for i in range(length):
            if rho[i] > thRho and delta[i] > thDel:
                result[i] = center
                center = center + 1
                result_visited[i] = 0

        k_dist_arr = k_dist(length, k_arr)

        threshold = np.average(k_dist_arr)

        outlier_arr = outlier(length, k_dist_arr, threshold)

        strategyOne(k_arr_index, outlier_arr, dist, result, result_visited, K)

        for i in range(length):
            if result[i] == -1:
                result[i] = DPC.nearestNeighbor(length, dist, rho, result, i)

        # strategyTwo(k_arr_index, result, length, K, center)

        draw.draw(result, location, name)

    cid = fig.canvas.mpl_connect('button_press_event', on_press)

    plt.savefig('result/' + name + '_decision.png', facecolor='white', edgecolor='none')
    plt.show()
