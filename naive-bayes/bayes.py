def loadData():
    postingList = [['my', 'dogs', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

#
def createVocaList(dataset):
    vocaSet = set([])
    for document in dataset:
        vocaSet = vocaSet | set(document)  # put all words in every document into the vocalSet
    return list(vocaSet)


if '__main__' == __name__:
    document, lss = loadData()
    lis = createVocaList(document)
    list.sort(lis)
    print(lis)
