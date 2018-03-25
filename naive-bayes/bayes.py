# 模拟加载数据
def loadData():
    postingList = [['my', 'dogs', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


# 将所有文档去重、排序,得到我的字典
def createVocaList(dataset):
    vc_set = set([])
    for docu in dataset:
        vc_set = vc_set | set(docu)  # put all words in every document into the vocalSet
    vc_list = list(vc_set)
    list.sort(vc_list)
    return vc_list


# 根据以上字典, 将一句话转换为vector
def sentence2Vec(vocaList, input):
    print("Input sentence:%s" % input)
    vec = [0] * len(vocaList)
    for word in input:
        if word in vocaList:
            vec[vocaList.index(word)] = 1
        else:
            print("The word:%s is not in my Vocabulary!" % word)
    print("Returned vector:%s" % vec)
    return vec