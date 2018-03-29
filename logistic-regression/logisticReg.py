from numpy import mat, shape, ones, array, arange, dot
from numpy.ma import exp
import matplotlib.pyplot as plt


def loadData():
    dataX = []
    dataY = []
    fr = open("testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataX.append([1.0, float(lineArr[0]), float(lineArr[1])])
        dataY.append(float(lineArr[2]))
    return dataX, dataY


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


###梯度下降
def gradientAscend(dataX, dataY):
    matX = mat(dataX)
    matY = mat(dataY).transpose()
    print("shape(x)=", shape(matX))
    print("shape(y)=", shape(matY))
    m, n = shape(matX)
    alpha = 0.001
    weights = ones((n, 1))
    print("shape(weights)=", shape(weights))

    for i in range(500):
        h = sigmoid(matX * weights)
        error = (matY - h)
        weights = weights + alpha * matX.transpose() * error
    return weights


###随机梯度下降
def stochasticGradientAscend(dataX, dataY):
    m, n = shape(dataX)
    alpha = 0.01
    weights = ones(n)

    for i in range(150*m):
        i=i%m
        h = sigmoid(sum(dataX[i] * weights))
        error = dataY[i] - h
        # 这里必须使用dot, 用*会报错
        weights = weights + dot(alpha * error, dataX[i])
    return weights


def plotBestFit(weights):
    dataX, dataY = loadData()
    dataArr = array(dataX)  #
    n = shape(dataArr)[0]
    xcord1 = []
    xcord2 = []
    ycord1 = []
    ycord2 = []

    for i in range(n):
        if int(dataY[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c="red", marker="s")
    ax.scatter(xcord2, ycord2, s=30, c="green")
    x = arange(-3.0, 3.0, 0.1)

    # 这里需要先取出来转换为float,否则计算出来的y的type会变成跟weights一样的矩阵
    a, b, c = float(weights[0]), float(weights[1]), float(weights[2])
    y = (-a - b * x) / c

    ax.plot(x, y)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()


if __name__ == "__main__":
    dataX, dataY = loadData()
    print("dataX =", dataX)
    print("dataY =", dataY)

    w = (gradientAscend(dataX, dataY))
    # w = stochasticGradientAscend(dataX, dataY)

    print("*" * 100)
    print("weight=", w)
    plotBestFit(weights=w)
