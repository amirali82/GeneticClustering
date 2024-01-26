import random
from dataSet import geneLength
import numpy as np

collectionSize = 130

collection = []

def generateRandomGene(len):
    res = np.zeros(geneLength, dtype=int)
    for i in range(len):
        res[i] = random.choices([0, 1, 2, 3], weights=[1, 10, 10, 10], k=1)[0]
    return res

def generateCollection():
    for i in range(collectionSize):
        collection.append(generateRandomGene(geneLength))

generateCollection()