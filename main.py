#-*- coding:utf-8 -*-

import numpy as np
from sklearn import cluster
from DPC import DPC
from DPC import DPC_Data_Filed

#f = open('./dataSet/D31.txt', 'r')
f = open('./dataSet/Aggregation.txt', 'r')
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

DPC.DPC(dataSet, 0.02, 'Aggregation')
#dc = DPC_Data_Filed.DPC_Data_Filed(dataSet)
#DPC.DPC(dataSet, dc, 'Aggregation_Data_Filed')
#   y_pred = algorithm.fit_predict(dataSet)

    # row_num = int(math.sqrt(len(clustering_algorithms)))
    #
    # plt.subplot(row_num, row_num, plot_num)