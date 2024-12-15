import numpy as np
from sklearn.metrics import pairwise_distances

def ja(inputFilename,outputFilename):
    input_Data = np.loadtxt(f"{inputFilename}", dtype=int, delimiter=',')
    input_Data = input_Data[:, 2:]

    output_Data=1 - pairwise_distances(input_Data, metric='jaccard')
    np.savetxt(f"{outputFilename}", output_Data, fmt="%s", delimiter=',')
    


