from math import exp

import pandas as pd
from numpy import mat, shape, ones


def loadData():
    dataX = []
    dataY = []
    frame = pd.read_table("testSet.txt")

    print(type(frame))
    for i in range(len(frame)):
        dataX.append(list(frame.iloc[i, 0:2]))

    dataY = list(frame.iloc[:, 2])
    print(dataY)
    print(dataX)
    return dataX, dataY


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


def gradientAscent(dataX, labels):
    xMatrix = mat(dataX)
    yMatrix = mat(labels).transpose()
    # print("xMatrix = ", xMatrix)
    # print("yMatrix = ", yMatrix)

    m, n = shape(xMatrix)
    p, q = shape(yMatrix)
    print("shape(x)=", m, "", n)
    print("shape(y)=", p, "", q)

    weights = ones((n, 1))
    print(weights)
    print("shape(weights)=",shape(weights))

    alpha = 0.001
    maxCycles = 500

    for k in range(maxCycles):
        h = sigmoid( weights *xMatrix)
        err = yMatrix - h
        weights = weights + alpha * xMatrix.transpose() * err

    return weights


if __name__ == "__main__":
    x, y = loadData()
    weights = gradientAscent(x, y)
    print(weights)
