from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
# importing data

df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df['target'] = iris['target']
# makeing data frame with targets included

df = df.sample(frac = 1).reset_index(drop=True)
# shufflig and reindexing data frame

shuffledTargets = df['target']
df = df.drop(columns=['target'])
# take apart targets from data frame to prevent information leak

geneLength = df.shape[0]
   
def examine(gene):
    cat = [[], [], []]
    for i in range(geneLength):
        if gene[i] != 0:
          cat[gene[i] - 1].append(shuffledTargets[i])
    
    cnt = np.array((3, 3), dtype=int)
    for i in range(3):
        print("cluster", i)
        for j in range(3):
            print("From Class " + j + " : " + cat[i].count(j), end=" ")
        print('\n')
