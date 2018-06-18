#-*- coding:utf-8 -*-

from math import *
import numpy as np
import scipy.io as sio
from sklearn import cluster, metrics, preprocessing
from DPC import DPC
from DPC import DPC_Data_Filed
from DPC import KNN_DPC
from DPC import draw

#f = open('./dataSet/s2.txt', 'r')
# f = open('./dataSet/Aggregation.txt', 'r')
# lines = f.readlines()
# dataSet = []
# for line in lines:
#     dataSet.append( [float(i) for i in line.replace('\r','').replace('\n','').split('\t')] )
# dataSet = np.array(dataSet)

# mat读取和处理
load_data = np.array(sio.loadmat('./dataSet/CsimmatNuclearRecept.mat')['matrix'])
load_data = 1 - (load_data + load_data.T) / 2
load_data = preprocessing.MinMaxScaler().fit_transform(load_data)
# DPC.DPC(load_data, 0.04, 'DPC on Enzyme - Target', True)
KNN_DPC.KNN_DPC(load_data, 'KNN-DPC on NuclearRecept - Drug', True)

n_clusters = 15 #33 #7
clustering_algorithms = (
    # ('DBSCAN', cluster.DBSCAN(eps = 1.40, min_samples = 7)), #Aggregation
    # ('DBSCAN', cluster.DBSCAN(eps = 0.625, min_samples = 12)), #D31
    # ('DBSCAN', cluster.DBSCAN(eps = 2.75, min_samples = 10)), #s2
    # ('DBSCAN', cluster.DBSCAN(eps = 0.8, min_samples = 5)), #Flame
    # ('K-Means', cluster.MiniBatchKMeans(n_clusters = 6)),
    # ('AffinityPropagaion', cluster.AffinityPropagation(convergence_iter=30, max_iter=200, damping=0.98)), #0.77
    # ('DPC', DPC.DPC(dataSet, 0.02, 'DPC on compound')),
    # ('KNN-DPC on compound', KNN_DPC.KNN_DPC(dataSet, 'KNN-DPC on compound'))
)

# KNN_DPC.KNN_DPC(dataSet, 'KNN-DPC K=3')
# KNN_DPC.KNN_DPC(dataSet, 'KNN-DPC on Aggregation')1
# KNN_DPC.KNN_DPC(dataSet, 'KNN-DPC K=9')

# DPC.DPC(dataSet, 0.02, 'Aggregation')
# dc = DPC_Data_Filed.DPC_Data_Filed(load_data, 'Aggregation_Data_Filed_Entropy')
# DPC.DPC(load_data, dc, 'DPC_Data_Filed on GPCR - Target', True)
#KNN_DPC.KNN_DPC(dataSet, 'Aggregation_KNN_DPC')
# for algorithm in clustering_algorithms:
#     if 'DPC' in algorithm[0]:
#         continue
#     else:
#         y_pred = algorithm[1].fit_predict(dataSet)
#         print(y_pred)
#         draw.draw(y_pred, dataSet, algorithm[0] + ' on Flame')