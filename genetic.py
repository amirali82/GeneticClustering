import random
from dataSet import geneLength
import numpy as np

mutationRate = 0.5

def crossOver(x, y):
    pos = random.randint(0, geneLength - 1)
    res = np.append(x[:pos], y[pos:])

    return mutation(
        res, 
        random.choices([3, 2, 1, 0], weights=[mutationRate ** 3, mutationRate ** 2, mutationRate, 1], k=1)
    )

'''
    gene codes:
        0 : no cluster
        1 : cluster 0
        2 : cluster 1
        3 : cluster 2
'''

def mutation(x, count):
    for i in range(count[0]):
        pos = random.randint(0, geneLength - 1)
        x[pos] = random.randint(0, 3)
    return x