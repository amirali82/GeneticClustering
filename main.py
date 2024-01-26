from fitnessScorer import getCollectionScore, getAllFitness, getBestGene
from generator import collection, collectionSize
from genetic import crossOver
import numpy as np 
import random
from dataSet import examine

#desiredScore = 95
round = 0

bestGene = np.zeros(150, dtype=int)
currentHighScore = 0

while (round < 50):
    collectionScore = getCollectionScore(collection)

    print("Round", round)
    print("Score", collectionScore)
    
    weights = getAllFitness(collection)

    print(weights)
    print("----------------")
    
    newCollection = []
    for i in range(collectionSize):
        x, y = random.choices(collection, weights=weights, k=2)
        newCollection.append(crossOver(x, y))

    collection = newCollection
    round += 1

    if currentHighScore < collectionScore:
        bestGene = getBestGene(collection, False)

print(bestGene)
bestGene.tofile("cluster.csv", sep=',')
examine(bestGene)
