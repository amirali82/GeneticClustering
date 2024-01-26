from dataSet import df
from generator import collectionSize
from multipledispatch import dispatch
from statistics import stdev, mean
import numpy as np
import math

def getCollectionScore(collection):
    return np.max(
        getAllFitness(collection)
    )

@dispatch(np.ndarray, np.ndarray)
def d(v1, v2):
    return math.sqrt(np.inner((v1 - v2), (v1 - v2)))

@dispatch(int, int)
def d(x : int, y : int):
    v1 = np.array(df.iloc[x])
    v2 = np.array(df.iloc[y])

    return d(v1, v2)

def clusterDistance(index, cluster):
    sum = 0
    for x in cluster:
        sum += d(index, x)
    return sum

def getCentroid(cluster):
    sum = np.zeros(df.shape[1], dtype=np.float64)

    for x in cluster:
        sum += np.array(df.iloc[x])

    return sum / len(cluster)

def getClusterScore(cluster):
    centroid = getCentroid(cluster)

    sum = 0
    for x in cluster:
        sum += d(np.array(df.iloc[x]), centroid)
    
    return sum / len(centroid)

def centroidDistanceSum(clusters):
    cent = []
    for i in range(3):
        cent.append(getCentroid(clusters[i]))
    
    dis = []
    for i in range(3):
        dis.append(
            d(cent[i], cent[(i + 1) % 3])
        )
    return dis

def getFitness(genome):
    clusters = [[], [], []]
    
    for i in range(len(genome)):
        clusters[genome[i] - 1].append(i)

    # res = 0
    # for i in range(len(genome)):
    #     if genome[i] != 0:
    #         a = clusterDistance(i, clusters[genome[i] - 1])

    #         b = 0
    #         for j in range(3):
    #             if genome[i] - 1 != j:
    #                 b += clusterDistance(i, clusters[j])
            
    #         res += (b - a) / max(b, a)
    
    score_list = []
    for i in range(3):
        score_list.append(
            getClusterScore(clusters[i])
        )

    
    # res = 10000 + centroidDistanceSum(clusters) - mean(score_list) 
    noiseCnt = np.count_nonzero(genome == 0)
    dis = centroidDistanceSum(clusters)
    res = max(sum(dis) - (noiseCnt // 5) * 0.005, 0.01)
    return round(res * 100)
    


def getBestGene(collection, printAnswer=True):
    maxIndex = np.argmax(
        getAllFitness(collection)
    )

    if printAnswer:
        print("Best gene:")
        print(collection[maxIndex])

    return collection[maxIndex]

def getAllFitness(collection):
    weights = []
    for gene in collection:
        weights.append(getFitness(gene))
    return weights