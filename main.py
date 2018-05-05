#-*- coding:utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
from itertools import cycle, islice
from DPC import DPC

f = open('./dataSet/D31.txt', 'r')
#f = open('./dataSet/Aggregation.txt', 'r')
#f = open('./dataSet/s1.txt', 'r')
lines = f.readlines()
dataSet = []
for line in lines:
    dataSet.append( [float(i) for i in line.replace('\r','').replace('\n','').split('\t')] )

dataSet = np.array(dataSet)

n_clusters = 33 #7
clustering_algorithms = (
    # ('DBSCAN', cluster.DBSCAN(eps = 0.625, min_samples = 12)),
    # ('K-Means', cluster.MiniBatchKMeans(n_clusters = n_clusters)),
    # ('SpectralClustering', cluster.SpectralClustering(
    #     n_clusters = n_clusters, eigen_solver = 'arpack',
    #     affinity = "nearest_neighbors")),
    # ('DPC', DPC.DPC(dataSet, 0.02))
    # ('DPC-1%', DPC.DPC(dataSet, 0.01)),
    # ('DPC-2%', DPC.DPC(dataSet, 0.02)),
    # ('DPC-3%', DPC.DPC(dataSet, 0.03)),
    # ('DPC-4%', DPC.DPC(dataSet, 0.04))
)

plot_num = 1

DPC.DPC(dataSet, 0.02, 'DPC')

# for name, algorithm in clustering_algorithms:
#
#     if('DPC' in name):
#         y_pred = algorithm
#     else:
#         y_pred = algorithm.fit_predict(dataSet)

    # colors = np.array(list(islice(cycle(['k', 'r', 'y', 'g', 'b', 'c', 'm']),int(max(y_pred) + 1))))
    #
    # row_num = int(math.sqrt(len(clustering_algorithms)))
    #
    # plt.subplot(row_num, row_num, plot_num)
    #
    # plt.title(name, size = 18)
    #
    # plt.scatter(dataSet[:, 0], dataSet[:, 1], marker='.', color = colors[y_pred])
    #
    # plt.xticks(())
    # plt.yticks(())
    # plot_num += 1

# plt.savefig('Cluster-D31.png', facecolor='white', edgecolor='none')
# plt.show()