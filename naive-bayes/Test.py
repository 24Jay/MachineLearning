import bayes
import train
from math import log


# 这里的概率转换成对数log
def naiveBayesClassfication(testX, p_1_vector, p_0_vector, p_class_1):
    p1 = log(sum(testX * p_1_vector)) + log(p_class_1)
    p0 = log(sum(testX * p_0_vector)) + log(1 - p_class_1)

    print("p1 = ", p1, ", while p0 = ", p0)
    if p1 > p0:
        return 1
    else:
        return 0

    # if '__main__' == __name__:


# def testNaiveBayesAlgorithm(entry):
if __name__ == "__main__":
    document, trainY = bayes.loadData()
    lis = bayes.createVocaList(document)
    print("My dictionary:\n", lis, "\n")

    trainX = []
    for sentence in document:
        print("************************" * 5)
        vec = bayes.sentence2Vec(lis, sentence)
        trainX.append(vec)
        print("")

    print("\n\n")
    print("************************" * 5)
    print("trainX = ", trainX)
    print("trainY = ", trainY)

    print("\n\n")
    print("************************" * 5)
    p_1_vector, p_0_vector, p_class_1 = train.trainNaiveBayes(trainX, trainY)

    print("/****************************Training Work Completed************************************/")


    entry1 = ["love", "my", "dalmation"]
    vect1 = bayes.sentence2Vec(lis,entry1)
    print(entry1,"classfied as :",naiveBayesClassfication(vect1,p_1_vector,p_0_vector,p_class_1))

    entry2 = ["stupid","garbage"]
    vect2 = bayes.sentence2Vec(lis,entry2)
    print(entry2,"classfied as :",naiveBayesClassfication(vect2,p_1_vector,p_0_vector,p_class_1))
