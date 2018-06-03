#-*- coding:utf-8 -*-

from math import *
import numpy as np
from sklearn import cluster, metrics, datasets
from DPC import DPC
from DPC import DPC_Data_Filed
from DPC import KNN_DPC
from DPC import draw

#f = open('./dataSet/s2.txt', 'r')
f = open('./dataSet/compound.txt', 'r')
lines = f.readlines()
dataSet = []
for line in lines:
    dataSet.append( [float(i) for i in line.replace('\r','').replace('\n','').split('\t')] )

dataSet = np.array(dataSet)

n_clusters = 15 #33 #7
clustering_algorithms = (
    # ('DBSCAN', cluster.DBSCAN(eps = 1.40, min_samples = 7)), #Aggregation
    # ('DBSCAN', cluster.DBSCAN(eps = 0.625, min_samples = 12)), #D31
    # ('DBSCAN', cluster.DBSCAN(eps = 2.75, min_samples = 10)), #s2
    # ('DBSCAN', cluster.DBSCAN(eps = 0.8, min_samples = 5)), #Flame
    # ('K-Means', cluster.MiniBatchKMeans(n_clusters = 6)),
    # ('AffinityPropagaion', cluster.AffinityPropagation(convergence_iter=30, max_iter=200, damping=0.98)), #0.77
    ('DPC', DPC.DPC(dataSet, 0.02, 'DPC on compound')),
    ('KNN-DPC on compound', KNN_DPC.KNN_DPC(dataSet, 'KNN-DPC on compound'))
)

#DPC.DPC(dataSet, 0.02, 'Aggregation')
#dc = DPC_Data_Filed.DPC_Data_Filed(dataSet, 'Aggregation_Data_Filed_Entropy')
#DPC.DPC(dataSet, dc, 'Aggregation')
#KNN_DPC.KNN_DPC(dataSet, 'Aggregation_KNN_DPC')
# for algorithm in clustering_algorithms:
#     if 'DPC' in algorithm[0]:
#         continue
#     else:
#         y_pred = algorithm[1].fit_predict(dataSet)
#         print(y_pred)
#         draw.draw(y_pred, dataSet, algorithm[0] + ' on Flame')