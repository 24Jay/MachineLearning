from numpy import *

def trainNaiveBayes(trainX,trainY):
    totalDoc = len(trainX)
    totalWord = len(trainX[0])

    # 计算侮辱性文档的概率: p(c=1)
    p_class_1 = sum(trainY)/float(totalDoc)

    # 为了解决有的单词在某类文档没有出现导致对应的概率为0, 所以把每个单词出现的初始次数设置为1
    # p_0_num = zeros(totalWord)
    # p_1_num = zeros(totalWord)

    p_0_num = ones(totalWord)
    p_1_num = ones(totalWord)

    p_0_denom = 2.0
    p_1_denom = 2.0

    for i in range(totalDoc):
        if trainY[i] == 1:
            p_1_num +=trainX[i] #计算每个词汇在侮辱性文档中的总数
            p_1_denom += sum(trainX[i]) #计算所有侮辱性文档的词汇总数
        else:
            p_0_num += trainX[i]
            p_0_denom += sum(trainX[i])

    p_1_vector = p_1_num/p_1_denom
    p_0_vector = p_0_num/p_0_denom

    print("p(W|c=1) : ",p_1_vector)
    print("p(W|c=0) : ",p_0_vector)
    print("p(c=1) : ",p_class_1)
    # 返回p(w0|c=1),p(w1|c=1),p(w2|c=1),....
    # 返回p(w0|c=0),p(w1|c=0),p(w2|c=0),....
    # 返回p(c=1)
    return  p_1_vector,p_0_vector,p_class_1