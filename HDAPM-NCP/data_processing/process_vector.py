import math
import numpy as np
import pandas as pd

def zeroone(inputFilename,outputFilename,a,number,path):
    disease_Data = np.loadtxt(f"{inputFilename}", dtype=str, delimiter=',')
    df = pd.read_csv(path, header=None, names=['id', 'DiseaseId'])
    df.set_index('DiseaseId', inplace=True)
    contact_ratio = []
    zero_matrix = []
    for i in range(0,number):
        zero_matrix.append(0)
    for i in range(0, a):
        zero_matrix = []
        for ix in range(0, number):
            zero_matrix.append(0)
        contact_ratio.append(zero_matrix)
    def extract_numbers(text):
        numbers = ''.join([char for char in text if char.isdigit()])
        return numbers

    j = 0
    for row in df.itertuples():
        j = j + 1
        if (j > 0):
            contact_ratio[j - 1][0] = int(extract_numbers(row.Index))
    t = 0
    for xinxi in disease_Data:
        t = t + 1

        if t > 1:
            id = int(extract_numbers(xinxi[0]))
            targetid = int(extract_numbers(xinxi[1]))
            i = int(df.loc[xinxi[0]].id)
            contact_ratio[i - 1][1] = i
            contact_ratio[i - 1][targetid + 1] = 1

    np.savetxt(f"{outputFilename}", contact_ratio, fmt="%s", delimiter=',')

def vectorCount(outputFilename,matrixFilename,matrixNumber):
    vector_Data = np.loadtxt(outputFilename, dtype=int, delimiter=',')
    con = np.zeros((matrixNumber, matrixNumber))
    n = 0
    for vn in vector_Data:
        if not np.all(vn[2:]==0):
            n = n + 1
    sum = 0
    for vx in vector_Data:
        sum = sum + np.linalg.norm(vx[2:], ord=2)
    xishu = n / sum
    def f(x, y, xishu):
        if np.all(x==0):
            return 0
        if np.all(y==0):
            return 0
        a2 = np.linalg.norm(x - y, ord=2)
        a2 = -xishu * a2
        result = math.exp(a2)
        return result
    i = 0
    j = 0
    for v1 in vector_Data:
        t1 = v1[2:]
        i = i + 1
        for v2 in vector_Data:
            t2 = v2[2:]
            j = j + 1
            con[i - 1][j - 1] = f(t1, t2, xishu)
        j = 0
    for i in range(0,matrixNumber):
        con[i][i]=1

    np.savetxt(matrixFilename, con, fmt="%f", delimiter=',')

