import numpy as np
from sklearn import metrics
def mi(inputFilename,outputFilename):
    input_Data = np.loadtxt(f"{inputFilename}", dtype=int, delimiter=',')
    input_Data = input_Data[:, 2:]
    X=input_Data
    length = X.shape[0]
    kernel = np.zeros((length, length))

    for i in range(length):
        a_vec = X[i, :]
        for j in range(i + 1):
            b_vec = X[j, :]
            kernel[i, j] = metrics.mutual_info_score(a_vec, b_vec)
            kernel[j, i] = kernel[i, j]
    output_Data=kernel
    np.savetxt(f"{outputFilename}", output_Data, fmt="%s", delimiter=',')
    return kernel





