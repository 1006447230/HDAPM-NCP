import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def cos(inputFilename,outputFilename):
    input_Data = np.loadtxt(f"{inputFilename}", dtype=int, delimiter=',')
    input_Data=input_Data[:,2:]
    output_Data = cosine_similarity(input_Data)
    output_Data[np.isnan(output_Data)] = 0
    np.fill_diagonal(output_Data, 1)
    np.savetxt(f"{outputFilename}", output_Data, fmt="%s", delimiter=',')
